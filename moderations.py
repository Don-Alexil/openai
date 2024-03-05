from openai import OpenAI

client = OpenAI()

# Create a request to the Completions endpoint
response = client.moderations.create(
  model="text-moderation-latest",
  input="My favorite book is How to Kill a Mockingbird."
)

print(response.model_dump())