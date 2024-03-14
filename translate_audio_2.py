from openai import OpenAI

client = OpenAI()

# Open the audion.m4a file
audio_file = open("mandarin-full.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(
  model = "whisper-1",
  file = audio_file
)

# Create a request to the API to identify the language spoken
chat_response = response = client.completions.create(
    model = "gpt-3.5-turbo-instruct", 
    prompt = "What is language spoken in the text : " + audio_response.text
 )

print(chat_response.choices[0].text)