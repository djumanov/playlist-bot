from tinydb import TinyDB, Query


class PlaylistDatabase:
    def __init__(self, db_name: str) -> None:
        self.db = TinyDB(db_name, indent=4, separators=(',', ':'))
        self.users = self.db.table('users')
        self.playlists = self.db.table('playlists')
        self.songs = self.db.table('songs')
        self.playlist_songs = self.db.table('playlist_songs')
        self.status = self.db.table('status')

    def add_user(self, user_id: str, username: str) -> bool:
        """
        Add a new user to the users table
        """
        if self.is_user(user_id):
            return False
        new_user = {'user_id': user_id, 'username': username}
        self.users.insert(new_user)
        self.status.insert({'user_id': user_id, 'status': 'regular'})
        return True
    
    def view_users(self) -> list:
        """
        Get all users
        """
        return self.users.all()

    def is_user(self, user_id) -> bool:
        """
        Check user
        """
        q = Query()
        return self.users.get(q.user_id == user_id)

    def get_status(self, user_id):
        """
        get user status
        """
        q = Query()
        return self.status.get(q.user_id == user_id)['status']
    
    def update_status(self, user_id: str, status: str):
        """
        Change user status
        """
        q = Query()
        return self.status.update({'status': status}, q.user_id == user_id)


    def add_playlist(self, playlist_name: str, user_id: int):
        """
        Add a new playlist to the playlists table
        """
        playlist = self.is_playlist(playlist_name, user_id)
        if playlist:
            return playlist

        new_playlist = {'playlist_name': playlist_name, 'user_id': user_id}
        id = self.playlists.insert(new_playlist)
        return self.songs.get(doc_id=id)

    def view_playlists(self, user_id: str) -> list:
        """
        Get all playlists
        """
        q = Query()
        return self.playlists.search(q.user_id == user_id)

    def is_playlist(self, playlist_name: str, user_id: str) -> bool:
        """
        Check playlist
        """
        q = Query()
        return self.playlists.get(q.playlist_name == playlist_name, q.user_id == user_id)


    def add_song(self, playlist: int, file_id: str, title:str, performer:str):
        """
        Add a new song to the songs table
        """
        song = self.is_song(playlist, file_id)
        if song:
            return song
        new_song = {'playlist': playlist, 'file_id': file_id, 'title': title, 'performer': performer, 'playlist': playlist}
        self.songs.insert(new_song)
        return True

    def is_song(self, playlist: int, file_id: str) -> bool:
        """
        Check song
        """
        q = Query()
        return self.songs.get(q.playlist == playlist, q.file_id == file_id)

    def add_song_to_playlist(self, song_id: int, playlist_id: int):
        """
        Add a song to a playlist
        """
        return self.playlist_songs.insert({'song_id':song_id,'playlist_id':playlist_id})
        
    def get_playlists_of_user(self,user_id:int):
        """
        Retrieve all playlists created by a user
        """
        User = Query()
        playlists_of_user = self.playlists.search(User.owner == user_id)
        return playlists_of_user
    
    def get_songs_of_playlist(self,playlist_id:int):
        """
        Retrieve all songs in a given playlist
        """
        Song = Query()
        songs_of_playlist = self.playlist_songs.search(Song.playlist_id == playlist_id)
        return songs_of_playlist
        
    def remove_song_from_playlist(self,song_id:int,playlist_id:int):
        """
        Remove a song from a playlist
        """
        Song = Query()
        self.playlist_songs.remove((Song.song_id == song_id) & (Song.playlist_id == playlist_id))
        print(f"song_id: {song_id} has been removed from playlist_id: {playlist_id}")

