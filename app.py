import streamlit as st
from parser import extract_text_from_pdf
from insights import generate_invoice_summary

st.set_page_config(page_title="LLM-Powered Invoice Parser", layout="centered")

# 💼 Title & Description
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>📄 LLM-Powered Invoice Parser + Insights</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #666;'>Upload a PDF invoice and let AI extract, analyze, and summarize the key details for you.</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# 📤 File Uploader
st.markdown("### 📤 Upload Your Invoice")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("🔍 Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)

    st.markdown("### 📝 Extracted Invoice Text")
    st.text_area("Raw Text from PDF", raw_text, height=200)

    if st.button("🚀 Analyze with AI", use_container_width=True):
        with st.spinner("🤖 Analyzing with LLM..."):
            result = generate_invoice_summary(raw_text)

        st.markdown("---")
        st.markdown(
            "<h3 style='color:#2E8B57;'>📊 Invoice Summary</h3>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div style='background-color:#f9f9f9; padding:15px; border-radius:10px; border: 1px solid #ccc;'>{result}</div>",
            unsafe_allow_html=True
        )
else:
    st.markdown("🟡 Please upload a PDF file to begin.", unsafe_allow_html=True)

# 🔚 Footer
st.markdown("<br><hr style='border:0.5px solid #ddd'><p style='text-align:center; color:gray;'>© 2025 Unsungfields AI • Powered by LLM</p>", unsafe_allow_html=True)
