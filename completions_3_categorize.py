from openai import OpenAI

client = OpenAI()

prompt = """
Categorize the following companies in the following categories Tech, Energy, Luxury Goods, or Investment: 
Apple, Microsoft, Saudi Aramco, Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, and LVMH
"""
# Create a request to the Completions endpoint
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=100, 
  temperature = 0.5
)

print(response.choices[0].text)