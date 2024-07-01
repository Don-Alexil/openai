from openai import OpenAI

# Create the OpenAI client
client = OpenAI()

# Create the request
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format={"type": "json_object"}

)

# Print the response
print(response.choices[0].message.content)