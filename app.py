import streamlit as st
import promptizer
import re
import html

def clean_xml_output(text):
    """Extract XML content from markdown code blocks if present."""
    pattern = r"```(?:xml)?\n?(.*?)\n?```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text

st.set_page_config(page_title="Promptizer", page_icon="▪️", layout="wide")

# Neo-brutalist CSS
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #e0e0e0;
        background-image: radial-gradient(#000000 1px, transparent 1px);
        background-size: 20px 20px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Force text color to black for main elements, but not ALL divs */
    .stApp p {
        color: #000000 !important;
    }
    .stApp label {
        color: #000000 !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 4px solid #000000;
    }
    
    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }
    
    /* Headings */
    h1 {
        font-size: 5rem !important;
        font-weight: 900 !important;
        color: #000000 !important;
        text-transform: uppercase;
        margin-bottom: 1rem !important;
        letter-spacing: -2px;
        text-shadow: 3px 3px 0px rgba(255,255,255,0.8);
    }
    
    h3 {
        background: #000000 !important;
        color: #ffffff !important;
        padding: 15px !important;
        font-size: 1.5rem !important;
        display: inline-block !important;
        border: 2px solid #000000 !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #ffffff !important;
    }

    /* Input fields */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 8px 8px 0px #000000 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        outline: none !important;
        box-shadow: 12px 12px 0px #000000 !important;
        transform: translate(-2px, -2px) !important;
        border-color: #000000 !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #ff00ff !important;
        color: #000000 !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 8px 8px 0px #000000 !important;
        font-weight: 900 !important;
        font-size: 1.5rem !important;
        text-transform: uppercase !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.1s ease-in-out !important;
    }
    .stButton button:hover {
        transform: translate(-2px, -2px) !important;
        box-shadow: 10px 10px 0px #000000 !important;
        background-color: #ff55ff !important;
    }
    .stButton button:active {
        transform: translate(2px, 2px) !important;
        box-shadow: 4px 4px 0px #000000 !important;
    }
    
    /* Custom Code Block Styling - MOST IMPORTANT */
    .neo-code-block {
        background-color: #ffffff !important;
        border: 4px solid #000000 !important;
        padding: 20px !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 1rem !important;
        color: #000000 !important;
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
        box-shadow: 10px 10px 0px #000000 !important;
        margin-top: 10px !important;
        margin-bottom: 20px !important;
        max-height: 600px !important;
        overflow-y: auto !important;
        line-height: 1.5 !important;
    }
    
    /* Ensure all text inside code block is black */
    .neo-code-block * {
        color: #000000 !important;
        background: transparent !important;
    }

    /* Download button alignment */
    div[data-testid="stDownloadButton"] button {
        background-color: #00ff00 !important;
        color: #000000 !important;
        width: 100% !important;
    }
    
    /* Labels */
    label {
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        text-transform: uppercase !important;
        margin-bottom: 0.5rem !important;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("PROMPTIZER")
st.markdown("### RAW TEXT -> XML CONVERTER")

# Sidebar for settings
with st.sidebar:
    st.header("CONFIG")
    model = st.text_input("MODEL", value="gemma3:4b")
    st.markdown("---")
    st.markdown("""
    <div style="border: 2px solid black; padding: 10px; background: white; box-shadow: 4px 4px 0px black;">
        <b>STATUS:</b><br>
        LOCALHOST:11434<br>
        <span style="color: green">● ONLINE</span>
    </div>
    """, unsafe_allow_html=True)

# Main input
prompt_input = st.text_area("INPUT RAW PROMPT", height=150, placeholder="TYPE HERE...")

col1, col2 = st.columns([1, 4])
with col1:
    optimize_btn = st.button("EXECUTE", type="primary")

if optimize_btn:
    if prompt_input:
        with st.spinner("PROCESSING..."):
            try:
                response = promptizer.get_ollama_response(prompt_input, model=model)
                
                if response and "response" in response:
                    raw_output = response["response"]
                    # Clean the output
                    xml_output = clean_xml_output(raw_output)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("### OUTPUT")
                    
                    # Use custom HTML for code block to ensure visibility (bypass Streamlit theme)
                    st.markdown(f"""
                    <div class="neo-code-block">
{html.escape(xml_output)}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Option to download
                    st.download_button(
                        label="DOWNLOAD XML",
                        data=xml_output,
                        file_name="prompt.xml",
                        mime="text/xml"
                    )
                else:
                    st.error("NULL RESPONSE RECEIVED")
                    
            except SystemExit:
                st.error("CONNECTION ERROR: CHECK OLLAMA")
            except Exception as e:
                st.error(f"SYSTEM ERROR: {e}")
    else:
        st.warning("INPUT REQUIRED")
