import streamlit as st
from parser import extract_text_from_pdf
from insights import generate_invoice_summary

st.title("LLM-Powered Invoice Parser + Insights")

uploaded_file = st.file_uploader("Upload PDF invoice", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Text")
    st.text_area("Invoice Text", raw_text, height=200)

    if st.button("Analyze with AI"):
        with st.spinner("Analyzing with LLM..."):
            result = generate_invoice_summary(raw_text)
        st.subheader("Invoice Summary")
        st.markdown(result)
