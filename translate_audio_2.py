from openai import OpenAI

client = OpenAI()

# Open the audion.m4a file
audio_file = open("mandarin-full.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "Act as Work Bank report auditor"

# Create a translation from the audio file
response = client.audio.translations.create(
  model = "whisper-1",
  prompt = prompt,
  file = audio_file
)

# Extract and print the transcript text
print(response.text)