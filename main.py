class Song:
    def __init__(self, author, title, length):
        self.author = author
        self.title = title
        self.length = length


class Player:
    def __init__(self, song_list):
        self.song_list = song_list

    def print_str(self):
        print(('>' * 5 + '♫' * 10 + '<' * 5).center(35))

    def switch_on(self):
        for x in range(1, 11, 2):
            print('♫' * x)
        for y in range(11, 0, -2):
            print('♫' * y)
        print(f'\nWelcome to MP3 Player')
        self.print_str()

    def show_songs(self, song_list):
        for i,song in enumerate(song_list):
            print(f'{i+1}.{song.author} - {song.title}({song.length})')
        self.print_str()

    def add_song(self):
        new_song = Song(
            input("Please input song's author :"),
            input("It's title :"),
            input("And length :")
        )
        song_list.append(new_song)
        self.print_str
        self.show_songs(song_list)

    def remove_song(self):
        index = int(input("Enter song's number :"))
        song_list.pop(index-1)
        self.show_songs(song_list)


song_list = [
    Song('The Black Eyed Peas','Pump It','3:35'),
    Song('DJ Snake','Lean On','2:57'),
    Song('Tiesto','The Motto','2:45')
]