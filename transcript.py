from openai import OpenAI

client = OpenAI()

# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response = client.audio.transcriptions.create(
  model = "whisper-1",
  file = audio_file
)

# Extract and print the transcript text
print(response.text)