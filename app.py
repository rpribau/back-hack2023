import streamlit as st
import openai
import fitz  # PyMuPDF

# Initialize OpenAI API credentials
openai.api_type = "azure"
openai.api_key = "6b25369971534252bbcee5e488ce59f1"
openai.api_base = "https://openaistkinno.openai.azure.com/"
openai.api_version = "2023-07-01-preview"

# Define the color scheme
primary_color = "#270404"
secondary_color = "#540000"
tertiary_color = "#B60303"

# Apply custom CSS for styling
st.markdown(
    f"""
    <style>
    .stTextInput {{
        background-color: transparent;
        color: {secondary_color};
    }}
    .stButton {{
        background-color: transparent;
        color: {tertiary_color};
    }}
    .stMarkdown {{
        background-color: transparent;
        color: white;
        padding: 10px;
    }}
    .vertical-scroll {{
        overflow-y: auto !important;
        max-height: 400px;
        padding: 10px;
        color: white;
    }}
    .chat-log {{
        background-color: {primary_color};
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }}
    .sidebar {{
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        padding: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("FAMAI")
st.write("Factory Analytics with Machine AI")  # Subtitle

# Create a sidebar for instructions
st.sidebar.title("Instructions")
st.sidebar.write(
    "1. Enter your question or prompt in the text input field."
)
st.sidebar.write(
    "2. Click the 'Get AI Response' button to receive a response."
)
st.sidebar.write(
    "3. The AI response will be displayed in the chatbox."
)
st.sidebar.write("Feel free to ask anything related to your factory analytics!")

# Load PDF file and extract its content
pdf_file_path = 'testFile.pdf'  # Replace with the actual path to your PDF file
pdf_document = fitz.open(pdf_file_path)
pdf_text_content = ""
for page in pdf_document:
    pdf_text_content += page.get_text()

# User input for prompts
user_prompt = st.text_input("Enter your question or prompt:")

# Create a response button
if st.button("Get AI Response"):
    # Combine the file content and user prompt
    combined_prompt = f"This is the PDF content:\n{pdf_text_content}\n\nUser Prompt: {user_prompt}"

    # Generate a response from the chatbot
    response = openai.ChatCompletion.create(
        engine="InnovationGPT2",
        messages=[{"role": "system", "content": combined_prompt}],
        max_tokens=1000
    )

    # Display the user's message in the chat log
    st.markdown(
        f'<div class="chat-log" style="text-align: right;">You: {user_prompt}</div>',
        unsafe_allow_html=True
    )

    # Display the AI's response in the chat log as "FAMAI"
    st.markdown(
        f'<div class="chat-log">FAMAI: {response.choices[0].message.content}</div>',
        unsafe_allow_html=True
    )

# Footer
st.sidebar.markdown(
    "Made with ❤️ by improvise.txt team"
)
