# 📌 AI Blog Generator Agent (Web App)

AI Blog Generator is a web application designed to automate the end-to-end creation of structured blog content. The system accepts a user-defined topic and contextual parameters, then leverages AI to produce a coherent, well-organized article accompanied by semantically relevant images for each section.

The application addresses the challenge of content creation at scale by eliminating the need for manual writing and visual sourcing. It is built with a modular Flask backend, a responsive web interface, and integrates AI-based text and image generation into a unified workflow.

---

# 🎯 What It Does

Most blog creation tools either assist with writing or provide visuals — rarely both. This application combines both capabilities seamlessly:

* Accepts a topic, description, audience, tone, and length as input
* Generates a complete blog with title, introduction, and structured sections
* Creates AI-generated images for every paragraph, placed contextually
* Displays a live preview on the same page
* Allows exporting the blog for external use

---

# 🖊️ Inputs

| Field               | Description                               |
| ------------------- | ----------------------------------------- |
| Blog Topic          | Main subject of the article               |
| Blog Description    | Additional context or content direction   |
| Target Audience     | Intended readers                          |
| Tone                | Formal / Informal / Technical / Narrative |
| Blog Length         | Short / Medium / Long                     |
| Keywords (Optional) | SEO or focus keywords                     |

---

# 📤 Outputs

* **Blog Title** — Automatically generated
* **Structured Article** — Introduction + multiple sections
* **AI-Generated Images** — One per paragraph, semantically aligned
* **Live Preview** — Displayed instantly in browser
* **Export Options** — HTML / Markdown / PDF

---

# ⚙️ How It Works

```
User Input Form
        ↓
Flask Backend Processes Input
        ↓
AI Model Generates Blog Content
        ↓
Each Paragraph → Image Generation Model
        ↓
Text + Images Combined via Jinja2 Templates
        ↓
Rendered Blog Preview in Browser
```

---

# 🛠️ Tech Stack

### Backend

* Python 3.x
* Flask
* Jinja2

### Frontend

* HTML5
* CSS3

### AI Integration

* Text Generation Models
* Image Generation Models

### Tooling

* Git & GitHub
* Environment Variables (`.env`)

---

# 📁 Project Structure

```
AI_BLOG_GENERATOR/
│
├── templates/
│   └── index.html        # Input form + blog preview UI
│
├── tests/                # Unit and integration tests
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

* Python 3.9+
* pip
* Modern web browser

---

## 1. Clone the Repository

```bash
git clone https://github.com/KMMythriGowda/AI_Blog_Generator.git
cd AI_Blog_Generator
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
# Add your AI API keys below
# OPENAI_API_KEY=your_key_here
```

---

## 4. Run the Application

```bash
python app.py
```

Open your browser and visit:
👉 http://127.0.0.1:5000

---

# ✅ What Works Well

* Fast generation for short and medium-length blogs
* Accurate paragraph-to-image alignment
* Clean and responsive UI on desktop
* Relevant and structured content output

---

# ⚠️ Known Limitations

* Longer blogs increase generation time due to multiple AI calls
* Image quality depends on the underlying AI model
* Export options may be limited in current version
* Requires internet connection for AI services

---

# 🔮 Planned Improvements

* Higher-quality and more context-aware image generation
* Regenerate specific paragraphs or images
* Full export support with embedded images (HTML + PDF)
* Improved mobile responsiveness
* User authentication and saved blog history

---

# 🤝 Contributing

Contributions are welcome!

* Fork the repository and submit pull requests
* Open issues for bugs, suggestions, or improvements
* Maintain consistency with existing code structure

---

# 👩‍💻 Author

**K M Mythri Gowda**

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

* Flask and the open-source Python community
* AI research community for text and image generation
* Hackathon organizers and mentors
* Open web standards (HTML & CSS)

---
