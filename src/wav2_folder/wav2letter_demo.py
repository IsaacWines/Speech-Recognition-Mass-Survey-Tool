from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC, pipeline


def transcribe(testing_paths: dict):
    path_type = "local"
    file_type = "wav"
    pipe = pipeline(model="facebook/wav2vec2-large-960h")
    output = pipe(testing_paths[path_type][file_type], chunk_length_s=20)

    return output['text']
    
if __name__ == "__main__":
    testing_paths = {"local": {"mp3": "/workspaces/speech_recognition_libraries/data/country_genre/alone.mp3", "wav": "/workspaces/speech_recognition_libraries/data/country_genre/alone.wav"},"gcs": "gs://song_list/Hank Williams - Alone And Forsaken (Official Audio).mp3" }
    transcribe(testing_paths)