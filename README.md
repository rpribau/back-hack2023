# back-hack2023

<img src = "https://i.imgur.com/WKqz6Xd.png">

NOTE. THIS INCLUDES ALREADY THE FRONT END USING Streamlit

During HackMTY 2023, we created a search engine using the OpenAI API by uploading PDF, xlsx, docx, csv files and ask anything about the current information. You can ask anything about your information from multiple files, specially if you have a lot of files with multiple reports.

## Usage

- We highly recommend making prompts in the same language as the files sent, even if the GPT models can translate the files to any other language, sometimes it can send false answers (or even create answers from nowhere).
- This tool is intended to be used for enterprices but it can be used as a personal tool.

To run the file you will need:

- Python 3.10 or higher.
- Your files (.pdf, .docx, .pptx, .xlsx, or .csv)

Install the following libraries using this command in a Terminal:

```
pip install openai streamlit fitz
```

Open the App.py file and edit this section from the file:

- For Azure OpenAI API
```
# Initialize OpenAI API credentials
openai.api_type = "azure"
openai.api_key = "YOUR_API_KEY"
openai.api_base = "YOUR_AZURE_API_BASE"
openai.api_version = "AZURE_MODEL_VERSION"
```

- For personal/consumer OpenAI API
```
# Initialize OpenAI API credentials
openai.api_type = "gpt-4"
openai.api_key = "YOUR_API_KEY"
```





