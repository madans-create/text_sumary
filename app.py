import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# -----------------------------
# Streamlit Page Config & Styling
# -----------------------------
st.set_page_config(page_title="Text Summarizer App", page_icon="📝", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
h1 {
    color: #4b0082;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# App Title
# -----------------------------
st.title("📝 Text Summarizer App")
st.markdown("Enter a paragraph, and get a concise summary instantly!")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Settings")
max_sentences = st.sidebar.slider("Max number of sentences in summary", min_value=1, max_value=10, value=3)

# -----------------------------
# Main Layout
# -----------------------------
col1, col2 = st.columns([1,1])

with col1:
    st.header("Enter Text")
    user_input = st.text_area("Type or paste your paragraph here:", height=250)

with col2:
    st.header("Summary Output")
    if st.button("Summarize"):
        if user_input.strip():
            with st.spinner("Summarizing..."):
                # Parse the input text
                parser = PlaintextParser.from_string(user_input, Tokenizer("english"))
                stemmer = Stemmer("english")
                summarizer = LsaSummarizer(stemmer)
                summarizer.stop_words = get_stop_words("english")

                # Generate summary
                summary = summarizer(parser.document, max_sentences)
                summary_text = " ".join([str(sentence) for sentence in summary])

                st.success("✅ Summary generated!")
                st.markdown("### Summary:")
                st.write(summary_text)
        else:
            st.warning("⚠️ Please enter some text to summarize!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("© 2025 Text Summarizer App | Built with Python & Streamlit 💻")
