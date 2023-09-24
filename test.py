# Importar la biblioteca de OpenAI
import openai

openai.api_type = "azure"
openai.api_key = "6b25369971534252bbcee5e488ce59f1"
openai.api_base = "https://openaistkinno.openai.azure.com/"
openai.api_version = "2023-07-01-preview"  # subject to change

# Create a prompt
prompt = "From where is Leonel Messi?"

# Create the completion
response = openai.ChatCompletion.create(
  engine="InnovationGPT2",
  messages=[{
      "role": "system",
    "content": prompt
  }],
  max_tokens=100
)

# Print the output
print(response.choices[0].message.content)


