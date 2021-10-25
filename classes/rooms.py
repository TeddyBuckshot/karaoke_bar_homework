class Rooms:
    def __init__(self,room_no):
        self.room_no = room_no
        self.songs = []
        self.guests = []

    
    def check_in(self, guest):
        self.guests.append(guest.guest_name)
        print(self.guests)

    def check_out(self, guest):
        self.guests.remove(guest.guest_name)
        print(self.guests)
    
    def add_song(self, song):
        self.songs.append(song.artist_name)
        print(song.artist_name)
        print(song.song_name)
        print(self.songs)
        

