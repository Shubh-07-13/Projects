class playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")
    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else: 
            print(f"'{song}' not found in playlist.")
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, songs in enumerate(self.songs,1):
                print(f"{i} - {songs}")
        else:
            print("No songs yet. Add some!")
    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")
song = playlist("Road Trip Mix", "Pop")
while True:
    print("\n1. Add Song 2. Remove Song 3. View Playlist 4. Delete & Quit")
    c = input("Enter your choice: ")
    if c == "1":
        e = input("Enter your song: ")
        song.add_song(e)
    elif c == "2":
        e = input("Remove your song: ")
        song.remove_song(e)
    elif c == "3":
        song.display()
    elif c == "4":
        del song
        break
    else:
        print("This is an invalid input.")