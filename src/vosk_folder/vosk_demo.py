import subprocess, os, json
from vosk import Model, KaldiRecognizer
import sys

class Transcriber():
    # add a folder called pretrained_models and store the vosk model in there to use.
    def __init__(self, model_path):
        self.model = Model(model_path)

    def fmt(self, data):
        data = json.loads(data)

        return {
            
            "text": data["text"]
        }

    def sub_transcribe(self, filename):
        SAMPLE_RATE = 16000
        CHUNK_SIZE = 4000
        rec = KaldiRecognizer(self.model, SAMPLE_RATE)
        rec.SetWords(True)

        if not os.path.exists(filename):
            raise FileNotFoundError(filename)

        transcription = []
        ffmpeg_command = [
                "ffmpeg",
                "-nostdin",
                "-loglevel",
                "quiet",
                "-i",
                filename,
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-f",
                "s16le",
                "-",
            ]

        with subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE) as process:

            while True:
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                
                if rec.AcceptWaveform(data):
                    transcription.append(self.fmt(rec.Result()))

            transcription.append(self.fmt(rec.FinalResult()))

        text = []
        for x in transcription:
            text.append(''.join(str(x["text"])))
        results = ' '.join(str(e) for e in text)
    
        return results
        
def transcribe(testing_paths: dict):
    path_type = "local"
    file_type = 'mp3'
    path = sys.argv[0]
    head,tail = os.path.split(path)
    head2,tail = os.path.split(head)
    head3,tail = os.path.split(head2)
    model_path = os.path.join(head3, "pretrained_models", "vosk-model-en-us-0.22")
    print(model_path)
    transcriber = Transcriber(model_path)
    transcription = transcriber.sub_transcribe(testing_paths[path_type][file_type])
    return transcription


if __name__ == "__main__":
    # filename = "/workspaces/speech_recognition_libraries/data/test_wav/the-gettysburg-address.mp3"
    

    # transcriber = Transcriber(model_path)
    # transcription = transcriber.transcribe(filename)
    # print(transcription)
    transcribe({"local": {"mp3": "/workspaces/speech_recognition_libraries/data/country_genre/islands.mp3", "wav": "/workspaces/speech_recognition_libraries/data/country_genre/islands.wav"}})