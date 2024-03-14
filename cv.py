from openai import OpenAI

client = OpenAI()

# Create a request to the Completions endpoint
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  max_tokens=4096,
  messages = [
    {"role": "system",
     "content": "You Senior Sofware Engineeer specialized in Java."}, 
    {"role": "user",
     "content": f"""Compose a CV for 13 years of experience having the following points: 
        - solving suport problems 
        - remove technical debt 
        - integratio of new developpers 
      """}
  ]
)

print(response.choices[0].message.content)