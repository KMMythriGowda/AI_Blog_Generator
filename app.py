import markdown
from flask import Flask, render_template, request, session, redirect, url_for
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ RATE LIMITER
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

app = Flask(__name__)

# ✅ SESSION SECRET
app.secret_key = os.getenv("FLASK_SECRET", "change_this_secret")

# ✅ RATE LIMITER
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)

# ✅ GEMINI CONFIG
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are an expert professional blog writer."
)

# =========================
# 🟢 DATABASE SETUP
# =========================
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# =========================
# 🟢 AI FUNCTIONS
# =========================
def build_prompt(data: dict) -> str:
    prompt = f"""
Write a {data['tone']} blog.

Topic:
{data['topic']}

Purpose of the blog:
{data['purpose']}

Target audience:
{data['audience']}

Length:
{data['length']} (short ≈ 500 words, medium ≈ 800 words, long ≈ 1200 words)

SEO Keywords to include naturally:
{data['keywords']}

Guidelines:
- Clear structure with headings
- Engaging introduction
- Informative and practical
- Professional language
- Avoid emojis
"""
    return prompt.strip()


def generate_blog(prompt: str) -> str:
    response = model.generate_content(prompt)

    if not response or not hasattr(response, "text") or not response.text:
        raise RuntimeError("Gemini returned empty response")

    return response.text.strip()

# =========================
# 🟢 CREATE + GENERATE
# =========================
@app.route("/", methods=["GET", "POST"])
@limiter.limit("3 per minute")
def index():
    blog = ""
    title = ""

    if "count" not in session:
        session["count"] = 0

    if request.method == "POST":
        session["count"] += 1

        if session["count"] > 5:
            return "Too many requests. Please wait a minute and refresh."

        data = {
            "topic": request.form.get("topic", "").strip(),
            "purpose": request.form.get("purpose", "").strip(),
            "audience": request.form.get("audience", "").strip(),
            "tone": request.form.get("tone", "Professional"),
            "length": request.form.get("length", "medium"),
            "keywords": request.form.get("keywords", "").strip(),
        }

        if not data["topic"]:
            blog = "❌ ERROR: Topic is required."
        else:
            try:
                prompt = build_prompt(data)
                raw_blog = generate_blog(prompt)

                # Extract title (first line)
                title = data["topic"]

                blog = markdown.markdown(raw_blog)

                # ✅ SAVE TO DATABASE
                conn = get_db_connection()
                conn.execute(
                    "INSERT INTO blogs (title, content) VALUES (?, ?)",
                    (title, raw_blog)
                )
                conn.commit()
                conn.close()

            except Exception as e:
                blog = f"❌ Blog generation failed: {str(e)}"

    return render_template("index.html", blog=blog)

# =========================
# 🟢 READ (VIEW BLOGS)
# =========================
@app.route("/blogs")
def view_blogs():
    conn = get_db_connection()
    blogs = conn.execute("SELECT * FROM blogs").fetchall()
    conn.close()
    return render_template("blogs.html", blogs=blogs)

# =========================
# 🟢 UPDATE (EDIT BLOG)
# =========================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_blog(id):
    conn = get_db_connection()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        conn.execute(
            "UPDATE blogs SET title=?, content=? WHERE id=?",
            (title, content, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("view_blogs"))

    blog = conn.execute("SELECT * FROM blogs WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", blog=blog)

# =========================
# 🟢 DELETE
# =========================
@app.route("/delete/<int:id>")
def delete_blog(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM blogs WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("view_blogs"))

# =========================
# 🟢 RUN APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)