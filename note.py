import openai # imports whisper
import os # imports os
import re # imports re for sanitizing the title

from record import AudioRecorder # imports record.py

openai.api_key = os.getenv("OPENAI_API_KEY") # sets the API key

# take the title of the note
title = input("Note Title: ")

include_title = input("Include title in transcription? (y/n): ")

# take in a stream of audio and save it as an audio file
if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.start()
    recorder.stop()

# define the audio file to be transcribed
audio_file= open("audio.wav", "rb")

# saves the response from the transcription (string)
response = openai.Audio.transcribe("whisper-1", audio_file)

transcript = response["text"]

obsidian_vault_path = "C:\\Users\\Gavin\\OneDrive\\Documents\\Obsidian Vault\\"

if include_title == "y":
  obsidian_note = f"# {title}\n\n{transcript}"
else:
  obsidian_note = f"{transcript}"

# Remove or replace invalid characters
sanitized_title = re.sub(r'[\\/*?:"<>|]', '_', title)

with open(f"{obsidian_vault_path}/{sanitized_title}.md", "w") as f:
    f.write(obsidian_note)

print(f"Note saved as {sanitized_title}.md in Obsidian Vault.")