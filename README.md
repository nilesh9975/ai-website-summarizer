# 🌐 AI Website Summarizer using OpenAI GPT-5 Nano

A Python application that fetches the content of a website, extracts the visible text, and generates a concise AI-powered summary using the OpenAI GPT-5 Nano model.

---

## 📌 Features

- Fetches content from any public website
- Extracts readable text using BeautifulSoup
- Removes scripts, styles, and unnecessary HTML
- Generates concise summaries using OpenAI GPT-5 Nano
- Uses environment variables to securely manage API keys
- Simple and modular Python implementation

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenAI Python SDK
- GPT-5 Nano
- BeautifulSoup4
- Requests
- python-dotenv

---

## 📂 Project Structure

```
website-summarizer/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/website-summarizer.git

cd website-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
python app.py
```

---

## 💻 Example

Input:

```text
Enter website URL:
https://openai.com
```

Output:

```text
OpenAI develops advanced AI models and developer APIs. The website showcases ChatGPT, AI research, product announcements, and resources for building AI-powered applications.
```

---

## 📚 What I Learned

This project helped me learn:

- Working with REST APIs
- Integrating the OpenAI API
- Prompt engineering fundamentals
- Web scraping with BeautifulSoup
- Secure API key management using `.env`
- Writing modular and reusable Python code

---

## 🔮 Future Improvements

- Streamlit web interface
- Support for multiple URLs
- PDF and DOCX export
- Multi-language summaries
- AI-powered question answering
- Async requests for better performance

---

## 📦 Requirements

```text
openai
requests
beautifulsoup4
python-dotenv
```

Or install from:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---


**Nilesh Kumar**

Learning Generative AI, Python, Data Analytics, and AI-powered applications.
