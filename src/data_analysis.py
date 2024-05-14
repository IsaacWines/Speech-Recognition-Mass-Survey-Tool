import json
import matplotlib.pyplot as plt
from matplotlib import gridspec
import audio_tools
import sys, os
import numpy as np

def main():
    deep_key = "deepgram_local_demo"
    whisper_results,vosk_results,wav2_results,google_results,deepgram_results = {},{},{},{},{}
    google_key = "google_speech_demo"
    whisper_key = "whisper_demo"
    vosk_key = "vosk_demo"
    wav2_key = "wav2letter_demo"
    youtube_downloader_paths = audio_tools.youtube_downloader.get_testingpath()
    songs = list(youtube_downloader_paths.keys())

    path = sys.argv[0]
    head,tail = os.path.split(path)

    with open(os.path.join(head,"data","all_deepgram.json"), "r") as deep:
        deepgram_pre_results = json.load(deep)
    with open(os.path.join(head,"data","all_whisper.json"), "r") as whisper:
        whisper_pre_results = json.load(whisper)
    with open(os.path.join(head,"data","all_vosk.json"), "r") as vosk:
        vosk_pre_results = json.load(vosk)
    with open(os.path.join(head,"data","all_wav2.json"), "r") as wav2:
        wav2_pre_results = json.load(wav2)
    with open(os.path.join(head,"data","all_google.json"), "r") as google:
        google_pre_results = json.load(google)

    for song in songs:
        for lib in [deepgram_pre_results,whisper_pre_results,vosk_pre_results,wav2_pre_results,google_pre_results]:
            if lib == deepgram_pre_results:
                result_dict = deepgram_results
                lib_key = deep_key
            if lib == whisper_pre_results:
                result_dict = whisper_results
                lib_key = whisper_key
            if lib == vosk_pre_results:
                result_dict = vosk_results
                lib_key = vosk_key
            if lib == wav2_pre_results:
                result_dict = wav2_results
                lib_key = wav2_key
            if lib == google_pre_results:
                result_dict = google_results
                lib_key = google_key

            dist = int(lib[song][lib_key]["distance"])
            time = round(float(lib[song][lib_key]["time"]),2)
            possible_characters = len(lib[song][lib_key]["lyrics"])
            accuracy = ((possible_characters-dist)/possible_characters)*100
            accuracy = round(accuracy,2)
            accvstime = round(accuracy/time,2)
            temp = {f"{song}": {"distance": dist, "time": time, "accuracy": accuracy, "accvstime" : accvstime, "genre": lib[song][lib_key]["genre"]}}
            result_dict.update(temp)

    lib_sums = {}
    for lib in [deepgram_results,whisper_results,vosk_results,wav2_results,google_results]:
        dist_sum = 0
        time_sum = 0
        avg_acc = 0
        accvstime_sum = 0
        if lib == deepgram_results:
            name = "deepgram"
        if lib == whisper_results:
            name = "whisper"
        if lib == vosk_results:
            name = "vosk"
        if lib == wav2_results:
            name = "wav2"
        if lib == google_results:
            name = "google"
        for song in songs:
            dist_sum += lib[song]["distance"]
            time_sum += lib[song]["time"]
            avg_acc += lib[song]["accuracy"]
            accvstime_sum += lib[song]["accvstime"]
        avg_acc = avg_acc / 75
        temp = {f"{name}": {"dist_sum": round(dist_sum,2), "time_sum": round(time_sum/60,2), "avg_acc": round(avg_acc,2), "accvstime_sum": round(accvstime_sum,2)}}
        lib_sums.update(temp)

    song_sums = {}
    for song in songs:
        dist_sum = 0
        time_sum = 0
        avg_acc = 0
        accvstime_sum = 0
        counter = 0
        for lib in [deepgram_results,whisper_results,vosk_results,wav2_results,google_results]:
            counter += 1
            dist_sum += lib[song]["distance"]
            time_sum += lib[song]["time"]
            avg_acc += lib[song]["accuracy"]
            accvstime_sum += lib[song]["accvstime"]
        avg_acc = avg_acc / counter
        temp = {f"{song}": {"dist_sum": round(dist_sum,2), "time_sum": round(time_sum/60,2), "avg_acc": round(avg_acc,2), "accvstime_sum": round(accvstime_sum,2), "genre": lib[song]["genre"]}}
        song_sums.update(temp)
    
    genre_sums = {} 
    for genre in ["country","metal","hiphop","rock","pop"]:
        dist_sum = 0
        time_sum = 0
        avg_acc = 0
        accvstime_sum = 0
        counter = 0
        for song in songs:
            counter += 1
            if lib[song]["genre"] == genre:
                dist_sum += lib[song]["distance"]
                time_sum += lib[song]["time"]

                avg_acc += lib[song]["accuracy"]
                accvstime_sum += lib[song]["accvstime"]
                avg_acc = avg_acc / counter
        temp = {f"{genre}": {"dist_sum": round(dist_sum,2), "time_sum": round(time_sum/60,2), "avg_acc": round(avg_acc,2), "accvstime_sum": round(accvstime_sum,2)}}
        genre_sums.update(temp)

    song_names = []
    song_distances = []
    song_times = []
    song_accuracy = []
    genre_acc = []
    genre_accuracy = []
    genre_distances = []
    genre_times = []
    lib_time = []
    lib_acc = []
    lib_distance = []
    lib_names = []
    genre_names = []

    for lib in [deepgram_results,whisper_results,vosk_results,wav2_results,google_results]:
        if lib == deepgram_results:
            name = "deepgram"
        if lib == whisper_results:
            name = "whisper"
        if lib == vosk_results:
            name = "vosk"
        if lib == wav2_results:
            name = "wav2"
        if lib == google_results:
            name = "google"
        lib_time.append(lib_sums[name]["time_sum"])
        lib_acc.append(lib_sums[name]["avg_acc"])
        lib_distance.append(lib_sums[name]["dist_sum"])
        lib_names.append(name)

    for genre in ["country","metal","hiphop","rock","pop"]: 
        genre_acc.append(genre_sums[genre]["avg_acc"]) 
        genre_distances.append(genre_sums[genre]["dist_sum"])
        genre_accuracy.append(genre_sums[genre]["avg_acc"])
        genre_times.append(genre_sums[genre]["time_sum"])
        genre_names.append(genre)

    for song in songs:
        song_distances.append(song_sums[song]["dist_sum"])
        song_accuracy.append(song_sums[song]["avg_acc"])
        song_times.append(song_sums[song]["time_sum"])
        song_names.append(song)
    
    
    # accuracy vs time
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.scatter(song_times, song_accuracy)

    plt.ylim(0,100)
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_xlabel('Time (Minutes)')
    ax.set_title('Song Sums: Accuracy vs Time')
    for i, txt in enumerate(song_names):
        ax.text(song_times[i],song_accuracy[i],txt)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\song_accvstime.png")

    # song accuracy boxplot
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_title('Song Accuracy Barplot')
    ax.bar(song_names, song_accuracy, color ='maroon', 
        width = 0.5)
    plt.xticks(rotation=90)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\songacc_box.png")

    # genre accuracy barplot
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_title('Genre Accuracy Barplot')
    ax.bar(["country","metal","hiphop","rock","pop"], genre_acc, color = 'maroon', 
        width = 0.5)
    plt.xticks(rotation=90)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\genreacc_box.png")

    # all songs
    
    for song in songs:
        
        song_name = [f"{song}"]
        temp = {
            #'distance': (float(song_sums[song]["dist_sum"])),
            'time': (float(song_sums[song]["time_sum"])),
            'accuracy': (float(song_sums[song]["avg_acc"])),
            'accuracy vs time': (float(song_sums[song]["accvstime_sum"])),
        }
        fig = plt.figure()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        spec = gridspec.GridSpec(ncols=2, nrows=2,
                                width_ratios=[2, 1], wspace=0.5,
                                hspace=0.5, height_ratios=[1, 2])
        
        x = np.arange(len(song_name))  # the label locations
        width = 0.5  # the width of the bars
        multiplier = 0

        ax = fig.add_subplot()

        for attribute, measurement in temp.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
        ax.set_title(f'{song} summary')
        ax.set_xticks(x + width, song_name)
        ax.legend(loc='upper left', ncols=3)
        plt.savefig(f"C:\\Users\\isaac\\Downloads\\{song}_sum.png")

    # all genres
    for genre in ["country","metal","hiphop","rock","pop"]:
        
        genre_name = [f"{genre}"]
        temp = {
            #'distance': (float(song_sums[song]["dist_sum"])),
            'time': (float(genre_sums[genre]["time_sum"])),
            'accuracy': (float(genre_sums[genre]["avg_acc"])),
            'accuracy vs time': (float(genre_sums[genre]["accvstime_sum"])),
        }
        fig = plt.figure()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        spec = gridspec.GridSpec(ncols=2, nrows=2,
                                width_ratios=[2, 1], wspace=0.5,
                                hspace=0.5, height_ratios=[1, 2])
        
        x = np.arange(len(genre_name))  # the label locations
        width = 0.5  # the width of the bars
        multiplier = 0

        ax = fig.add_subplot()

        for attribute, measurement in temp.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
        ax.set_title(f'{genre} summary')
        ax.set_xticks(x + width, genre_name)
        ax.legend(loc='upper left', ncols=3)
        plt.savefig(f"C:\\Users\\isaac\\Downloads\\{genre}_sum.png")

    # genre acc vs time
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.scatter(genre_times, genre_acc)

    plt.ylim(0,5)
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_xlabel('Time (Minutes)')
    ax.set_title('Genre Sums: Accuracy vs Time')
    for i, txt in enumerate(genre_names):
        ax.text(genre_times[i],genre_acc[i],txt)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\genre_accvstime.png")

    # lib acc bar

    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_title('Library Accuracy Sums')
    ax.bar(lib_names, lib_acc, color = 'maroon', 
        width = 0.5)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\lib_acc_sum.png")

    # all lib
    for lib in lib_names:
        
        lib_name = [f"{lib}"]
        temp = {
            #'distance': (float(song_sums[song]["dist_sum"])),
            'time': (float(lib_sums[lib]["time_sum"])),
            'accuracy': (float(lib_sums[lib]["avg_acc"])),
            'accuracy vs time': (float(lib_sums[lib]["accvstime_sum"])),
        }
        fig = plt.figure()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        spec = gridspec.GridSpec(ncols=2, nrows=2,
                                width_ratios=[2, 1], wspace=0.5,
                                hspace=0.5, height_ratios=[1, 2])
        
        x = np.arange(len(lib_name))  # the label locations
        width = 0.5  # the width of the bars
        multiplier = 0

        ax = fig.add_subplot()

        for attribute, measurement in temp.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
        ax.set_title(f'{lib} summary')
        ax.set_xticks(x + width, lib_name)
        ax.legend(loc='upper left', ncols=3)
        plt.savefig(f"C:\\Users\\isaac\\Downloads\\{lib}_sum.png")
    
    # lib acc vs time
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    ax = fig.add_subplot()
    ax.scatter(lib_time, lib_acc)

    plt.ylim(0,50)
    ax.set_ylabel('Accuracy (Percentage)')
    ax.set_xlabel('Time (Minutes)')
    ax.set_title('Lib Sums: Accuracy vs Time')
    for i, txt in enumerate(lib_names):
        ax.text(lib_time[i],lib_acc[i],txt)
    plt.savefig(f"C:\\Users\\isaac\\Downloads\\lib_accvstime.png")
    
    # print(genre_sums)
    # print()
    # print(lib_sums)
    # input()
    # print(song_sums)

    # input()
    # print(deepgram_results)

    
    # for lib_results in [deepgram_results,whisper_results,vosk_results,wav2_results,google_results]:
    #     print(lib_results)
    #     print()


        

if __name__ == "__main__":
    main()