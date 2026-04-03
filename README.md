# 📌 AI Blog Generator Agent

AI Blog Generator is a full-stack web application that automates the end-to-end creation of structured blog content. The system accepts user-defined inputs and leverages AI to generate a well-organized article.

This project is enhanced with **CRUD functionality (Create, Read, Update, Delete)**, allowing users not only to generate blogs but also to manage them efficiently.

---

# 🎯 What It Does

Unlike traditional tools that only assist with writing, this application provides a complete workflow:

- Accepts topic, description, audience, tone, and length  
- Generates structured blog content using AI  
- Displays blog in a clean UI  
- Saves generated blogs to a database  
- Allows users to:
  - ✏️ Edit blogs (Update)
  - 🗑️ Delete blogs (Delete)
  - 📚 View all saved blogs (Read)

---

# 🖊️ Inputs

| Field               | Description                               |
|--------------------|-------------------------------------------|
| Blog Topic         | Main subject of the article               |
| Blog Description   | Additional context or direction           |
| Target Audience    | Intended readers                          |
| Tone               | Formal / Professional / Conversational    |
| Blog Length        | Short / Medium / Long                     |
| Keywords (Optional)| SEO keywords                             |

---

# 📤 Outputs

- **Blog Title** — AI-generated  
- **Structured Content** — Introduction + sections  
- **Formatted Blog Preview** — Rendered using HTML  
- **Stored Blogs** — Saved for future access  
- **Editable Content** — Modify previously generated blogs  

---

# ⚙️ How It Works

```
User Input Form
        ↓
Flask Backend Receives Data
        ↓
Prompt is Generated
        ↓
Google Gemini API Generates Blog Content
        ↓
Markdown → HTML Conversion
        ↓
Blog Saved to Database (SQLite)
        ↓
Displayed via Jinja Templates
```

---

# 🛠️ Tech Stack

## Backend
- Python 3.x  
- Flask  
- SQLite (for CRUD operations)  
- Flask-Limiter (rate limiting)

## Frontend
- HTML5  
- CSS3  
- Jinja2 Templates  

## AI Integration
- Google Gemini API (Text Generation)

## Tooling
- Git & GitHub  
- Environment Variables (`.env`)  

---

# 📁 Project Structure

```
AI_BLOG_GENERATOR/
│
├── templates/
│   ├── index.html        # Input form + blog preview
│   ├── blogs.html        # View all saved blogs
│   └── edit.html         # Edit blog page
│
├── tests/                # (Optional testing files)
├── app.py                # Main Flask application (CRUD + AI)
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (NOT pushed)
├── README.md             # Documentation
├── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.9+
- pip
- Internet connection (for AI API)

---

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Blog_Generator.git
cd AI_Blog_Generator
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file:

```
FLASK_ENV=development
FLASK_DEBUG=True
GOOGLE_API_KEY=your_api_key_here
FLASK_SECRET=your_secret_key
```

---

## 4. Run the Application

```bash
python app.py
```

Open:
👉 http://127.0.0.1:5000

---

# 🔄 CRUD Functionality

| Operation | Feature |
|----------|--------|
| Create   | Generate and save blog |
| Read     | View all blogs |
| Update   | Edit blog content |
| Delete   | Remove blog |

---

# ✅ What Works Well

- Clean and responsive UI  
- Fast generation for short/medium blogs  
- Persistent storage using database  
- Full CRUD workflow implemented  
- Rate limiting for controlled usage  

---

# ⚠️ Known Limitations

- Longer blogs take more time (API dependent)  
- No authentication (all users share same data)  
- Image generation not fully implemented (optional enhancement)  
- Requires internet for AI API  

---

# 🔮 Future Improvements

- Add AI image generation per paragraph  
- Export blog as PDF/HTML  
- User login system  
- Blog history per user  
- Improved UI/UX (mobile responsive)  

---

# 🤝 Contributing

Contributions are welcome!

- Fork the repository  
- Create a new branch  
- Submit a pull request  

---

# 👩‍💻 Author

**K M Mythri Gowda**

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

- Flask open-source community  
- Google Gemini AI  
- Hackathon mentors and organizers  
- Open web standards (HTML, CSS)  

---

# 🏆 Final Note

This project demonstrates:

- Full-stack web development  
- API integration  
- CRUD operations  
- Clean UI design  
- Practical problem-solving  
