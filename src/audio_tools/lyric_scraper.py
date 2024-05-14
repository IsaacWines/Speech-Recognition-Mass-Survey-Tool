import lyricsgenius
import os
import re
import sys
class Scraper:

    def __init__(self, token):
        self._token = token

    def get_token(self):
        return self._token
        
    def lyric_scraper(self, artist_name, song_name):
        number_of_tries = 3
        succeeded = False
        while number_of_tries > 0 and not succeeded:
            number_of_tries -= 1
            try:
                genius = lyricsgenius.Genius(self._token)
                artist = genius.search_artist(artist_name, max_songs=0, sort="title")
                song = artist.song(song_name)
                lyrics = song.lyrics
                remove_brackets, remove_embed = r'\[.*?\]', r'\d+|Embed'
                lyrics = re.sub(remove_brackets, '', lyrics)
                lyrics = re.sub(remove_embed, '', lyrics)
                new_line_index = lyrics.find('\n')
                if new_line_index > -1:
                    lyrics = lyrics[new_line_index+1:]
                lyrics = os.linesep.join([line for line in lyrics.splitlines() if line])
                succeeded = True
            except Exception as e:
                print(e)
        if not succeeded:
            lyrics = "No lyric found."
            print("No lyric found.")
    
        return lyrics

if __name__ == "__main__":
    path = sys.argv[0]
    head,tail = os.path.split(path)
    with open(os.path.join(head, "lyric_token.txt"), 'r') as f:
        token = str(f.read())
    finished_lyrics = Scraper(token).lyric_scraper("Micheal Jackson", "Billie Jean")
    print({'test': normalize.normalize(finished_lyrics)})
    