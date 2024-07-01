from openai import OpenAI
# Import the tenacity library
from tenacity import (
  retry, 
  wait_random_exponential, 
  stop_after_attempt
)

# Create the OpenAI client
client = OpenAI()

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(messages):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    return response.choices[0].message.content

measurements=[5.2, 6.3, 3.7]
messages = []
# Provide a system message and user messages to send the batch
messages.append({"role": "system", "content": "Convert the measurements from kilometers into miles and format the response into a table"})

# Append measurements to the message
[messages.append({"role": "user", "content": str(i)}) for i in measurements]

response = get_response(messages)
print(response)

