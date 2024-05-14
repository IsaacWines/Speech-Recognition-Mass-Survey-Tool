import os
from Levenshtein import distance
import time
import sys
import json
import audio_tools
import click
from collections import defaultdict
import lists
import whisper_folder
import vosk_folder
import google_folder
import deepgram_folder
#import pocketsphinx_folder
import wav2_folder

def distance_c(in1,in2): 
    distance_calc = distance(in1, in2)
    return distance_calc

def run(test_path,library):
    start = time.time()
    results = library.transcribe(test_path)
    end = time.time()
    time_calc = end-start
    #print(results)
    return (results, time_calc)

def generate_library_data_setup(library):
    main = {
    "whisper": whisper_folder.whisper_demo,
    "wav2": wav2_folder.wav2letter_demo,
    "vosk": vosk_folder.vosk_demo,
    "google": google_folder.google_speech_demo,
    "deepgram": deepgram_folder.deepgram_local_demo,
    #"pocketsphinx": {pocketsphinx_folder.pocketsphinx_demo
    }
    final = []
    for lib in range(len(library)):
        if any(library[lib] in x for x in ['whisper', 'wav2', 'vosk', 'google', 'deepgram', 'pocketsphinx']):
            final.append(main[library[lib]])
    return final

class Automate:
    def __init__(self, testing_paths, lyric_dict, library):
        self._testing_paths = testing_paths
        self._lyric_dict = lyric_dict
        self.library_choice = library
        path = sys.argv[0]
        head,tail = os.path.split(path)
        self.head = head
        self.custom_lyric_dict = {}
        
    def grab_user_input(self, selection):
        if selection == 'everything':
            self.type = 'everything'
            self.lyrics = list(self._testing_paths.keys())
            
        elif len(selection) == 1:
            if any(selection[0] in x for x in ['country', 'heavy_metal', 'rock', 'hip_hop', 'pop', 'jazz']):
                self.type = 'genre'
                self.lyrics = []
                for song in list(self._testing_paths.keys()):
                    if self._testing_paths[song]['genre'] == selection[0]:
                        self.lyrics.append(song)
            else:
                self.type = 'specific'
                self.lyrics = selection

        elif len(selection) > 1:
            self.lyrics = []
            for current_genre in range(len(selection)):
                if any(selection[current_genre] in x for x in ['country', 'heavy_metal', 'rock', 'hip_hop', 'pop', 'jazz']):
                    self.type = 'genre'
                    for song in list(self._testing_paths.keys()):
                        if self._testing_paths[song]['genre'] == selection[current_genre]:
                            self.lyrics.append(song)
                else:
                    self.lyrics.append(selection[current_genre])
        
        else:
            self.type = 'specific'
            self.lyrics = selection

    def custom(self,link,file_name,artist_name,song_name,genre,token):
        self._lyric_dict = {}

        if not os.path.exists(os.path.join(self.head, "lists", f"{file_name}.json")):
            with open(os.path.join(self.head, "lists", f"{file_name}_custom.json"), "w") as f:
                    temp_list = {file_name: audio_tools.lyric_scraper.Scraper(token).lyric_scraper(artist_name,song_name)}
                    self._lyric_dict.update(temp_list)
                    json.dump(self._lyric_dict, f, indent= 2)
        else:
            with open(os.path.join(self.head, "lists", f"{file_name}.json"), "r") as f:
                self._lyric_dict = json.load(f)

        self._testing_paths = audio_tools.youtube_downloader.custom_download(file_name, link, genre)
        self.type = 'custom'
        self.lyrics = [file_name]
  
    def automate(self):
        temp_song_result_dict = generate_library_data_setup(self.library_choice)
        song_result_dict = {}
        
        try:
            for song in self.lyrics:
                try:
                    lyric = audio_tools.normalize.normalize(self._lyric_dict[song])
                except:
                    lyric = "no lyric found"
                
                for lib in temp_song_result_dict:
                    
                    print(f"\n{lib}", f"_{song}_")
                    print(self._testing_paths[song], "\n")
                    library_string = {
                        whisper_folder.whisper_demo: "whisper_demo",
                        wav2_folder.wav2letter_demo: "wav2letter_demo",
                        vosk_folder.vosk_demo: "vosk_demo",
                        google_folder.google_speech_demo: "google_speech_demo",
                        deepgram_folder.deepgram_local_demo: "deepgram_local_demo",
                        #pocketsphinx_folder.pocketsphinx_demo: "pocketsphinx_demo"
                    }
                    results, time_calc = run(self._testing_paths[song], lib)
                    try:
                        temp = {song: {f"{library_string[lib]}": {"genre": f"{self._testing_paths[song]['genre']}", "results": f"{audio_tools.normalize.normalize(results)}", "lyrics": f"{lyric}", "distance": f"{distance_c(audio_tools.normalize.normalize(results),lyric)}", "time" : f"{time_calc}"}}}
                        print(temp)
                        song_result_dict.update(temp)
                    except Exception as e:
                        print(e)
                    
            return song_result_dict
        except Exception as e:
            print(e)

@click.command()
@click.option("--everything", "-e", is_flag = True, help="Will run everything.")
@click.option("--specific", "-s", multiple = True, help='Enter the short name of the specific song or genre you want transcribed. Run -o to see the list of songs.')
@click.option("--library", "-l", multiple = True, help='Enter the specific library you want to use to transcribe your songs, if not in use all libraries will run.')
@click.option("--output", "-o", help='Enter the name you want your result file to be. Do not use this flag to autocreate file name. The program will create a numbered result file if the file name already exists or if flag has not been called.')
@click.option("--arguments", "-a", is_flag=True, help="Shows a list of the songs. Displays: ['short name', 'real name', 'artist name', 'genre']")
@click.option("--custom", "-c", help="Allows for the use of custom songs to be transcribed. Enter '-c [youtubelink],[desiredsongfilename(No Spaces)],[fullartistname(Spaces Seperated By -)],[fullsongname(Spaces Seperated By -)]\n -c https://www.youtube.com/watch?v=dBN86y30Ufc,willie,Willie-Nelson,On-The-Road-Again")
def main(everything, specific, output, arguments, custom, library):
    path = sys.argv[0]
    head,tail = os.path.split(path)
    headTwo,tail = os.path.split(head)
    
    with open(os.path.join(head, "audio_tools", "lyric_token.txt"), 'r') as f:
        token = str(f.read())

    lyric_data = lists.download_list.get_list()
    youtube_downloader_paths = audio_tools.youtube_downloader.get_testingpath()
    songs = list(youtube_downloader_paths.keys())
    lyric_dict = {}

    if library:
        selected_library = list(library)
    
    else:
        selected_library = ['whisper', 'wav2', 'vosk', 'google', 'deepgram', 'pocketsphinx']

    if everything:
        selection = 'everything'
        click.echo(selection)

    else:
            if specific:
                selection = list(specific)
                click.echo(selection)

            if custom:
                click.echo("Custom Song is selected.")
                custom_link, song_file_name, artist_name, full_song_name = custom.split(",")
                artist_name = artist_name.replace("-", " ")
                full_song_name = full_song_name.replace("-", " ")

    if arguments:
        print("Song List")
        for song in songs:
            print([song, lyric_data[song]['real_name'], lyric_data[song]['artist'], lists.download_list.get_genre(lyric_data[song]['path'])])
        sys.exit(0)
    
    if not os.path.exists(os.path.join(head, "lists", "lyric_list.json")):
        with open(os.path.join(head, "lists", "lyric_list.json"), "w") as f:
                for song in songs:
                    temp_list = {song: audio_tools.lyric_scraper.Scraper(token).lyric_scraper(lyric_data[song]['artist'], lyric_data[song]['real_name'])}
                    lyric_dict.update(temp_list)
                json.dump(lyric_dict, f, indent= 2)
    else:
        with open(os.path.join(head, "lists", "lyric_list.json"), "r") as f:
            lyric_dict = json.load(f)

    if not custom:
        song_results = Automate(youtube_downloader_paths,lyric_dict,selected_library)
        song_results.grab_user_input(selection)
        song_results = song_results.automate()
    else:
        song_results = Automate(youtube_downloader_paths,lyric_dict,selected_library)
        song_results.custom(custom_link,song_file_name,artist_name,full_song_name,"custom",token)
        song_results = song_results.automate()

    if output is None:
        resultjson_path = os.path.join(headTwo, 'data', 'text_results','Song_Results.json')

        counter = 1
        while os.path.isfile(resultjson_path):
            resultjson_path = os.path.join(headTwo, 'data', 'text_results')
            resultjson_path = os.path.join(resultjson_path, f'Song_Results{counter}.json')
            counter += 1

    else:
        resultjson_path = os.path.join(headTwo, 'data', 'text_results',f'{output}.json')

        counter = 1
        while os.path.isfile(resultjson_path):
            resultjson_path = os.path.join(headTwo, 'data', 'text_results')
            resultjson_path = os.path.join(resultjson_path, f'{output}{counter}.json')
            counter += 1

    with open(resultjson_path, 'w') as sr:
        json.dump(song_results, sr, indent= 2)

if __name__ == "__main__":
    main()