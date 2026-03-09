import os
import glob
from openai import OpenAI

client = OpenAI()

m4a_files = glob.glob('*.m4a')

if not m4a_files:
    print("No m4a files found.")
    exit(0)

print(f"Found {len(m4a_files)} m4a files.")

for audio_file in m4a_files:
    transcript_file = audio_file.replace('.m4a', '_transcript.txt')
    if os.path.exists(transcript_file):
        print(f"Skipping {audio_file}, transcript already exists.")
        continue
    
    print(f"Transcribing {audio_file}...")
    try:
        with open(audio_file, "rb") as file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1", 
                file=file, 
                response_format="text"
            )
        with open(transcript_file, "w") as f:
            f.write(transcription)
        print(f"Done transcribing {audio_file}.")
    except Exception as e:
        print(f"Failed to transcribe {audio_file}: {e}")
