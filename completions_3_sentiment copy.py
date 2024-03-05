from openai import OpenAI

client = OpenAI()

prompt = """
Unbelievably good! // positive
Shoes fell apart on the second use. // negative
The shoes look nice, but they aren't very comfortable. // neutral
Can't wait to show them off!
"""
# Create a request to the Completions endpoint
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=100
)

print(response.choices[0].text)