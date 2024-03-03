import streamlit as st
from transformers import pipeline
from utils import get_text


st.title("PDF Question Answering App")

# File uploader
pdf_file = st.file_uploader("Upload PDF", type=['pdf'])

if pdf_file is not None:
    st.write("PDF uploaded successfully!")

    # Save uploaded PDF to a temporary file
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())
    
    # Display PDF content
    pdf_text = get_text("temp.pdf")
    st.write("PDF Content:")
    st.write(pdf_text)
    # Text input for questions
    question = st.text_input("Ask a question:")
    
    # Button to answer question
    if st.button("Get Answer"):
        # Load pre-trained question answering model
        qa_model = pipeline("text2text-generation")
        
        # Perform question answering
        answer = qa_model(f"question: {question}, context: {pdf_text}")
        
        # Display answer
        st.write("Answer:")
        st.write(answer[0]['generated_text'])