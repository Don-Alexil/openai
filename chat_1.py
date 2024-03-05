from openai import OpenAI

client = OpenAI()

# Create a request to the Completions endpoint
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  max_tokens=150,
  messages = [
    {"role": "system",
     "content": "You are a helpful data science tutor."}, 
    {"role": "user",
     "content": "What is the difference between a for loop and a while loop?"}
  ]
)

print(response.choices[0].message.content)