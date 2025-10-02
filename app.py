import streamlit as st
import google.generativeai as genai
from newspaper import Article
import validators

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Gemini AI Summarizer", layout="wide")

# --- API KEY CONFIGURATION ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.warning("Google API Key not found! Please add it to your Streamlit secrets.")
    st.stop()

# --- GEMINI MODEL ---
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(text_to_summarize):
    prompt = f"""
    You are an expert summarizer. Your task is to provide a concise, easy-to-read summary of the following article.
    The summary should be approximately 3-4 sentences long and capture the main points of the text.

    ARTICLE:
    {text_to_summarize}

    SUMMARY:
    """

    with st.spinner("Gemini AI is crafting a summary..."):
        try:
            # Call the Gemini API
            response = model.generate_content(prompt)
            # Display the result
            st.subheader("Summary:")
            st.success(response.text)
        except Exception as e:
            # Handle potential API errors gracefully
            st.error(f"An error occurred with the Gemini API: {e}")


# --- UI LAYOUT ---
st.title("Gemini AI Article & Text Summarizer")
st.write("Leverage Google's LLM model to get concise summaries from any URL or text.")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["Summarize by Article URL", "Summarize by Blog Text"])

# --- TAB 1: Summarize by URL ---
with tab1:
    st.header("Summarize from a Web Article")
    url = st.text_input("Enter Article URL:", key="url_input")

    if st.button("Summarize URL", key="url_button"):
        if not url.strip():
            st.warning("Please enter a URL.")
        elif not validators.url(url):
            st.error("Invalid URL format. Please enter a valid URL.")
        else:
            try:
                article = Article(url)
                article.download()
                article.parse()

                if not article.text:
                    st.error(
                        "Could not extract article text. The site may be protected or in an unsupported format."
                    )
                else:
                    st.subheader(f"Article Title: {article.title}")
                    generate_summary(article.text)

            except Exception as e:
                st.error(f"Failed to fetch or parse article: {e}")

# --- TAB 2: Summarize by Text ---
with tab2:
    st.header("Summarize from Pasted Text")
    user_text = st.text_area("Enter Text to Summarize:", height=250, key="text_input")

    if st.button("Summarize Text", key="text_button"):
        if not user_text.strip():
            st.warning("Please enter some text to summarize.")
        else:
            generate_summary(user_text)
