from openai import OpenAI

client = OpenAI()

instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the Completions endpoint
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  max_tokens=150,
  messages = [
    {"role": "system",
     "content": "You are a helpful python programmer."}, 
    {"role": "user",
     "content": instruction}
  ]
)

print(response.choices[0].message.content)