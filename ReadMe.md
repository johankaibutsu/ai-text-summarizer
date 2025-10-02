## Live Deployment : https://genai-text-summarizer.streamlit.app/

## Libraries Used

*   **streamlit:** Creates and runs the entire web user interface with simple Python commands.
*   **google-generativeai:** Needed to use Google's Gemini AI.
*   **newspaper3k:** Extracts the main article text and title from a given URL.
*   **validators:** Quickly checks if the user's input is a valid URL format.
*   **lxml_html_clean:** A required dependency that helps `newspaper3k` clean up HTML content.

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
