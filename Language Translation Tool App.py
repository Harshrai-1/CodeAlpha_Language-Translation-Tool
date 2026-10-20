import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

def main():
    st.title("🌐 Language Translation Tool")
    st.write("A simple, interactive web app to translate text between multiple languages using Python, Streamlit, and Deep Translator.")

    # Dictionary of supported languages mapping to ISO language codes
    languages = {
        "Auto Detect": "auto",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Hindi": "hi",
        "Bengali": "bn",
        "Chinese (Simplified)": "zh-CN",
        "Japanese": "ja",
        "Arabic": "ar",
        "Russian": "ru",
        "Portuguese": "pt",
        "Italian": "it"
    }

    # Language selection dropdowns
    col1, col2 = st.columns(2)
    with col1:
        source_lang_name = st.selectbox("Source Language", list(languages.keys()), index=0)
    with col2:
        target_lang_name = st.selectbox("Target Language", [k for k in languages.keys() if k != "Auto Detect"], index=4)

    source_code = languages[source_lang_name]
    target_code = languages[target_lang_name]

    # Input text block
    text_to_translate = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

    # Action button
    if st.button("Translate", type="primary", use_container_width=True):
        if not text_to_translate.strip():
            st.warning("Please enter some text to translate.")
        else:
            try:
                # Perform translation using deep-translator API
                translated_text = GoogleTranslator(
                    source=source_code, 
                    target=target_code
                ).translate(text_to_translate)

                st.subheader("Translated Text:")
                st.success(translated_text)

                # Code block view to enable easy copy functionality
                st.code(translated_text, language=None)

            except Exception as e:
                st.error(f"Translation Error: {e}")

if __name__ == "__main__":
    main()