from pytube import YouTube
import ffmpeg
import os
import sys
import lists
from audio_tools.audio_manipulator import sample_changer, file_changer
from google.cloud import storage



def upload_to_bucket(blob_name, path_to_file, bucket_name):
    path = sys.argv[0]
    head,tail = os.path.split(path)
    storage_client = storage.Client.from_service_account_json(os.path.join(head,'google_folder','key.json'))
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    return ("gs://" + blob.bucket.name + "/" + blob.name)

def get_uri(blob_name,bucket_name):
    path = sys.argv[0]
    head,tail = os.path.split(path)
    storage_client = storage.Client.from_service_account_json(os.path.join(head,'google_folder','key.json'))
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return ("gs://" + blob.bucket.name + "/" + blob.name)

def check_folders():
    path = sys.argv[0]
    head,tail = os.path.split(path)
    headTwo,tail = os.path.split(head)

    data_folder = os.path.join(headTwo,'data', 'country_genre')
    custom_folder = os.path.join(headTwo,'data', 'custom_songs')
    country_folder = os.path.join(headTwo,'data', 'heavy_metal')
    metal_folder = os.path.join(headTwo,'data', 'hip_hop_genre')
    hip_hop_folder = os.path.join(headTwo,'data', 'jazz_genre')
    jazz_folder = os.path.join(headTwo,'data', 'rock_genre')
    pop_folder = os.path.join(headTwo,'data', 'pop_genre')
    results_folder = os.path.join(headTwo,'data', 'text_results')
    folder_list = [data_folder,country_folder,metal_folder,hip_hop_folder,jazz_folder,pop_folder,results_folder,custom_folder]
    for folder in folder_list:
        if not os.path.exists(folder):
            os.makedirs(folder)

def download(link_list: dict):
    keys_list = list(lists.download_list.get_list().keys())
    testing_paths = {}
    check_folders()
    
    for name in keys_list:
        base_path = link_list[name]['path']
        mp3_path = os.path.join(base_path, f"{name}.mp3")
        mp4_path = os.path.join(base_path, f"{name}.mp4")
        wav_path = os.path.join(base_path, f"{name}.wav")
        link = link_list[name]['link']
        genre = lists.download_list.get_genre(base_path)

        if not os.path.isfile(mp3_path):
            yt = YouTube(link)
            yt.streams.get_audio_only().download(filename=mp4_path)
            try:
                ffmpeg.input(mp4_path).output(mp3_path, acodec='libmp3lame').run()
            except ffmpeg.Error as e:
                print('stdout:', e.stdout.decode('utf8'))
                print('stderr:', e.stderr.decode('utf8'))
                raise e
            os.remove(mp4_path)
            gsuri = upload_to_bucket(f"{name}.mp3",mp3_path,'song_list')
            sample_changer(name, mp3_path, base_path)
            file_changer(name, mp3_path, wav_path, base_path)
        elif not os.path.isfile(wav_path):
            sample_changer(name, mp3_path, base_path)
            file_changer(name, mp3_path, wav_path, base_path)
            gsuri = get_uri(f"{name}.mp3",'song_list')
        else:
            #print(f"{name} already exsists.")
            gsuri = get_uri(f"{name}.mp3",'song_list')

        temp_list = {name: {"genre": genre, "local": {"mp3": mp3_path, "wav": wav_path}, "gcs": f"{gsuri}"}}
        testing_paths.update(temp_list)
    
    return testing_paths

def custom_download(cname, clink, cgenre):
    path = sys.argv[0]
    head,tail = os.path.split(path)
    headTwo,tail = os.path.split(head)
    testing_paths = {}
    check_folders()

    base_path = os.path.join(headTwo,'data', 'custom_songs')
    mp3_path = os.path.join(base_path, f"{cname}.mp3")
    mp4_path = os.path.join(base_path, f"{cname}.mp4")
    wav_path = os.path.join(base_path, f"{cname}.wav")
    link = clink
    genre = cgenre

    if not os.path.isfile(mp3_path):
        yt = YouTube(link)
        yt.streams.get_audio_only().download(filename=mp4_path)
        try:
            ffmpeg.input(mp4_path).output(mp3_path, acodec='libmp3lame').run()
        except ffmpeg.Error as e:
            print('stdout:', e.stdout.decode('utf8'))
            print('stderr:', e.stderr.decode('utf8'))
            raise e
        os.remove(mp4_path)
        gsuri = upload_to_bucket(f"{cname}.mp3",mp3_path,'song_list')
        sample_changer(cname, mp3_path, base_path)
        file_changer(cname, mp3_path, wav_path, base_path)
    elif not os.path.isfile(wav_path):
        sample_changer(cname, mp3_path, base_path)
        file_changer(cname, mp3_path, wav_path, base_path)
        gsuri = get_uri(f"{cname}.mp3",'song_list')
    else:
        #print(f"{name} already exsists.")
        gsuri = get_uri(f"{cname}.mp3",'song_list')

    temp_list = {cname: {"genre": genre, "local": {"mp3": mp3_path, "wav": wav_path}, "gcs": f"{gsuri}"}}
    testing_paths.update(temp_list)
    
    return testing_paths

def get_testingpath():
    return download(lists.download_list.get_list())

if __name__ == "__main__":
    print(download(lists.download_list.get_list()))