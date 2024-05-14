import os
from pocketsphinx import Pocketsphinx, get_model_path

def transcribe(testing_paths: dict):
    model_path = get_model_path()
    config = {
        'hmm': os.path.join(model_path, 'en-us'),
        'lm': os.path.join(model_path, 'en-us.lm.bin'),
        'dict': os.path.join(model_path, 'cmudict-en-us.dict')
    }

    ps = Pocketsphinx(**config)
    audio_file_path = testing_paths['wav']
    ps.decode(audio_file=audio_file_path, buffer_size=2048, no_search=False, full_utt=False)

    recognized_text = ps.hypothesis()
    print(f"Recognized text: {recognized_text}")

if __name__ == "__main__":
    transcribe({"local": {'wav': './data/country_genre/alone.wav'} }
)

