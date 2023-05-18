import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import numpy as np

# Initialize the mixer
mixer.init()

# Create the main window
window = tk.Tk()
window.title("Probability Project")
window.geometry("240x380")

# Define color constants
BG_COLOR = "black"
BUTTON_COLOR = "skyblue"
LISTBOX_COLOR = "green"
LABEL_COLOR = "white"

# Set the background color of the window
window.configure(bg=BG_COLOR)

# Create a playlist to store the songs
playlist = []
current_song_index = 0


# ...
def add_song():
    """Add songs to the playlist."""
    filetypes = (("MP3 Files", "*.mp3"), ("All files", "*.*"))
    songs = filedialog.askopenfilenames(filetypes=filetypes)
    for song in songs:
        playlist.append(song)
    update_playlist_listbox()





def play_song(index):
    """Play a song from the playlist at the given index."""
    if index < len(playlist):
        mixer.music.stop()  # Stop the currently playing song (if any)
        song = playlist[index]
        mixer.music.load(song)
        mixer.music.play()


# ...

def play_random_song():
    """Play a random song from the playlist."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_index = np.random.randint(len(playlist))
        play_song(random_index)


# ...

def play_all_songs_randomly():
    """Play all songs in the playlist at once in random order."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_order = np.random.permutation(len(playlist))
        played_songs = set()  # Keep track of the played songs
        for index in random_order:
            song = playlist[index]
            if song not in played_songs:
                mixer.music.load(song)
                mixer.music.play()
                while mixer.music.get_busy():
                    continue
                played_songs.add(song)


def play_next_song():
    """Play the next song in the playlist."""
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song(current_song_index)


# Create the GUI elements with color settings
add_button = tk.Button(window, text="Add Song", command=add_song, relief=tk.RAISED, borderwidth=5, bg=BUTTON_COLOR)
add_button.pack()


play_button = tk.Button(window, text="Play Random Song", command=play_random_song, relief=tk.RAISED, borderwidth=5,
                        bg=BUTTON_COLOR)
play_button.pack()

play_all_button = tk.Button(window, text="Play All- Songs Randomly", command=play_all_songs_randomly, relief=tk.RAISED,
                            borderwidth=5, bg=BUTTON_COLOR)
play_all_button.pack()


next_button = tk.Button(window, text="Play Next Song", command=play_next_song, relief=tk.RAISED, borderwidth=5,
                        bg=BUTTON_COLOR)
next_button.pack()

# Create the playlist listbox
playlist_listbox = tk.Listbox(window, bg=LISTBOX_COLOR)
playlist_listbox.pack()


# Function to update the playlist listbox
def update_playlist_listbox():
    """Update the playlist listbox with the current playlist."""
    playlist_listbox.delete(0, tk.END)

    for song in playlist:
        playlist_listbox.insert(tk.END, os.path.basename(song))

    # Schedule the update after 1000 milliseconds (1 second)
    window.after(1000, update_playlist_listbox)


update_playlist_listbox()


# Function to update the song label
def update_song_label():
    """Update the song label with the current and total song count."""
    song_label.config(text="Song {}/{}".format(current_song_index + 1, len(playlist)))

    # Schedule the update after 1000 milliseconds (1 second)
    window.after(1000, update_song_label)


song_label = tk.Label(window, text="", bg=BG_COLOR, fg=LABEL_COLOR)
song_label.pack()

update_song_label()

# Run the main event loop
window.mainloop()
