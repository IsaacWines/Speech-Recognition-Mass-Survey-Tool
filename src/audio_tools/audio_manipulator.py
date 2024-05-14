from pydub import AudioSegment

def file_changer(name, song, wav_path, path):
    load_song = AudioSegment.from_mp3(song)
    load_song.export(wav_path, format="wav")
    print(f"successfully changed {name} to wav file.")

def sample_changer(name, song, path):
    load_song = AudioSegment.from_mp3(song)
    edited_song = load_song.set_frame_rate(44100)#.set_channels(1)
    edited_song.export(song, format="mp3")
    print(f"successfully changed {name}'s sample rate.")

if __name__ == "__main__":
    testing_paths = {"alone": {"local": "/workspaces/speech_recognition_libraries/data/country_genre/alone.mp3","gcs": "gs://song_list/Hank Williams - Alone And Forsaken (Official Audio).mp3" },
             "jolene": {"local": "/workspaces/speech_recognition_libraries/data/country_genre/jolene.mp3","gcs": "gs://song_list/Dolly_Parton_-_Jolene.mp3" },
             "road": {"local": "/workspaces/speech_recognition_libraries/data/country_genre/road.mp3","gcs": "gs://song_list/Willie-Nelson-On-The-Road-Again.mp3" },
             "dance": {"local": "/workspaces/speech_recognition_libraries/data/country_genre/dance.mp3","gcs": "gs://song_list/The Dance - Garth Brooks.mp3" },
             "gamble": {"local": "/workspaces/speech_recognition_libraries/data/country_genre/gamble.mp3","gcs": "gs://song_list/Kenny Rogers - The Gambler.mp3" }
             }
    for x in testing_paths:
        #file_changer(x,testing_paths[x]["local"])
        print(x)
        sample_changer(x,testing_paths[x]["local"])

        