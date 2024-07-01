from openai import OpenAI

client = OpenAI()

# Create a request to the Moderation endpoint
response = client.moderations.create(
  model="text-moderation-latest",
  input="My favorite book is How to Kill a Mockingbird."
)

# Print the category scores
print(response.model_dump())