from tkinter import *
import pygame
from tkinter import filedialog 

root = Tk()
root.title('My mp3 Player')
root.iconbitmap('C:/Users/Andrey/Desktop/MyProjects/python/Lab7/Exercise 2/Images/icon.png')
root.geometry("500x300")

#Initialize Pygame Mixer
pygame.mixer.init()

# Add Song Function
def add_song():
     song = filedialog.askopenfilename(initialdir='Lab7/Exercise 2/Music/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
     
     # Strip out the directory info and .mp3 extension from the song name
     song = song.replace("C:/Users/Andrey/Desktop/MyProjects/python/Lab7/Exercise 2/Music/", "")
     song = song.replace(".mp3", "")
     
     # Add song to listbox
     song_box.insert(END, song)
     
# Play selected Song
def play():
        song = song_box.get(ACTIVE)
        song = f'C:/Users/Andrey/Desktop/MyProjects/python/Lab7/Exercise 2/Music/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

# Stop Playing Current Song
def stop():
        pygame.mixer.music.stop()
        song_box.selection_clear(ACTIVE)

# Pause Current Song
def pause():
        pygame.mixer.music.pause()

# Create Playlist Box
song_box = Listbox(root, bg="orange", fg="white", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Buttons Images
back_button_image = PhotoImage(file='Lab7/Exercise 2/Images/back.png')
forward_button_image = PhotoImage(file='Lab7/Exercise 2/Images/forward.png')
play_button_image = PhotoImage(file='Lab7/Exercise 2/Images/play.png')
pause_button_image = PhotoImage(file='Lab7/Exercise 2/Images/pause.png')
stop_button_image = PhotoImage(file='Lab7/Exercise 2/Images/stop.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_button_image, borderwidth=0)
forward_button = Button(controls_frame, image=forward_button_image, borderwidth=0)
play_button = Button(controls_frame, image=play_button_image, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_button_image, borderwidth=0, command=pause)
stop_button = Button(controls_frame, image=stop_button_image, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=5)
forward_button.grid(row=0, column=1, padx=5)
play_button.grid(row=0, column=2, padx=5)
pause_button.grid(row=0, column=3, padx=5)
stop_button.grid(row=0, column=4, padx=5)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

root.mainloop()
