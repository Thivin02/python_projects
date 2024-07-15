from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

model_to_use="llama2"
response = client.chat.completions.create(
  model=model_to_use, 
  messages=[
    {
        "role": "system", 
        "content": "You are a professional content creation assistant."},
    {
        "role": "user", 
        "content": "In 1 sentence, what is the best kind of content to create in 2024?"
    },
  ]
)
print(response.choices[0].message.content)

