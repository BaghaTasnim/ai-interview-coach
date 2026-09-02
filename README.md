#  AI Interview Coach

An AI-powered interview coach that helps you practice technical and HR interviews with real-time feedback.

> Built with Python, Streamlit, and Groq — as part of my AI Engineer learning journey.

##  Features

-  **Multiple interview topics** — AI/ML, Python, Data Science, HR, or any custom topic
-  **PDF upload** — upload your course or document and get questions based on its content
-  **Real-time AI feedback** — after each answer you get:
  - What was good
  -  What was missing
  -  A better answer
  -  Score out of 10
-  **Interview history** — every session is saved locally in `history.json`

##  Tech Stack

| Technology | Purpose |
|---|---|
| `Python` | Core language |
| `Streamlit` | Web UI without HTML/CSS |
| `Groq API` | LLM for generating questions and feedback |
| `pypdf` | Extract text from uploaded PDFs |
| `python-dotenv` | Secure API key management |

##  Setup

### 1. Clone the repository
```bash
git clone https://github.com/BaghaTasnim/ai-interview-coach.git
cd ai-interview-coach
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
1. Go to [console.groq.com](https://console.groq.com) and create an account
2. Generate an API key
3. Create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

### 5. Run
```bash
streamlit run app.py
```

##  Project Structure

```
ai-interview-coach/
├── app.py              ← Streamlit UI
├── interviewer.py      ← AI interview logic
├── history.json        ← saved interview sessions (auto-generated)
├── requirements.txt
├── .env                ← API key (not pushed to GitHub)
├── .env.example
└── .gitignore
```

##  What I learned

- Designing system prompts for specific AI personas
- Managing conversation history for multi-turn interactions
- Building web UIs with Streamlit using Python only
- Processing and extracting text from PDF files
- Persisting data locally using JSON