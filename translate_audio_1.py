from openai import OpenAI

client = OpenAI()

# Open the audion.m4a file
audio_file = open("audio-portuguese.m4a", "rb")

# Create a transcript from the audio file
response = client.audio.translations.create(
  model = "whisper-1",
  file = audio_file
)

# Extract and print the transcript text
print(response.text)