

import json
from dotenv import load_dotenv
import logging
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()

def transcribe(AUDIO_FILE: dict):
    with open("deepgram_key.txt", "r") as f:
        key = int(f.read())
    path_type = "local"
    file_type = "mp3"
    try:
        config = DeepgramClientOptions(
            verbose=logging.SPAM,
        )

        deepgram = DeepgramClient(key)

        with open(AUDIO_FILE[path_type][file_type], "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova",
            smart_format=False,
            utterances=True,
            punctuate=False,
            diarize=False,
            paragraphs=True
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        result = response.to_json(indent=4)
        result_json = json.loads(result)
        
        return result_json["results"]["channels"][0]["alternatives"][0]["transcript"]
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    AUDIO_FILE = {"local": {"mp3": "/workspaces/speech_recognition_libraries/data/country_genre/alone.mp3", "wav": "/workspaces/speech_recognition_libraries/alone.wav"} }
    print(transcribe(AUDIO_FILE))