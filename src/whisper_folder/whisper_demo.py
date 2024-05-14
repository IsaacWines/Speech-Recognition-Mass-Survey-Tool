import whisper

def transcribe(testing_paths: dict):   
    path_type = "local"
    file_type = "mp3"
    model = whisper.load_model("base")
    #print(testing_paths[path_type][file_type])
    result = model.transcribe(testing_paths[path_type][file_type])
    results = result["text"]
    return results

if __name__ == "__main__":
    testing_paths = {"local": {"mp3": "/workspaces/speech_recognition_libraries/data/country_genre/alone.mp3", "wav": "/workspaces/speech_recognition_libraries/alone.wav"},"gcs": "gs://song_list/Hank Williams - Alone And Forsaken (Official Audio).mp3" }
    
    print(transcribe(testing_paths))