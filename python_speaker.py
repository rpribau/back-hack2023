# Import the ZeroMQ module
import zmq
import openai
import fitz

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

# Print the message
print("Received: %s" % prompt.decode())

msg = prompt.decode()

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

