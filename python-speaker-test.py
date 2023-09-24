# Import the ZeroMQ module
import zmq
import openai
import fitz
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from softtek_llm.chatbot import Chatbot
from softtek_llm.models import OpenAI
from softtek_llm.cache import Cache
from softtek_llm.vectorStores import PineconeVectorStore
from softtek_llm.embeddings import OpenAIEmbeddings
from softtek_llm.schemas import Filter
import pandas as pd
import os
import  jpype     
import  asposecells     



# Load csv file

loader = CSVLoader(file_path='report.csv')  
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("report.csv")
workbook.save("report.txt")
jpype.shutdownJVM()

# Create a context object
context = zmq.Context()

# Import OpenAI credentials
openai.api_type = "azure"
openai.api_key = "6b25369971534252bbcee5e488ce59f1"
openai.api_base = "https://openaistkinno.openai.azure.com/"
openai.api_version = "2023-07-01-preview" 

# Create a replier socket
sock = context.socket(zmq.REP)

# Bind to the JavaScript client
sock.bind("tcp://127.0.0.1:3000")

# Receive a request message
prompt = sock.recv()

# Create a question-answering chain using the index

# Print the message
print("Received: %s" % prompt.decode())

msg = prompt.decode()

# Use the chain to generate a response based on the prompt as a question
# Create the completion
response = openai.ChatCompletion.create(
  engine="InnovationGPT2",
  messages=[{
      "role": "system",
    "content": msg
  }],
  max_tokens=1000
)

# Print the output
print(response.choices[0].message.content)

# Send a reply message
sock.send_string(response.choices[0].message.content)
