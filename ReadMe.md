# Gemini AI Summarizer - Local Setup

## Prerequisites

- Python 3.8+
- Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/).

## 1. Clone Repository

```bash
git clone <repo_url>
cd <repo_name>
```

## 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
# On Windows use: .\venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure API Key

1.  Create the file: `.streamlit/secrets.toml`

2.  Add your API key to it like this:
    ```toml
    # .streamlit/secrets.toml
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
    ```

## 5. Run the Application

```bash
streamlit run app.py
```
