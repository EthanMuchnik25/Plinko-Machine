
# importing libraries
import cv2
import numpy as np
import random as rand
import ctypes
import pokemon as pok
import tkinter as tk


# Read Video 
def readVideo(vidName, event):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(vidName)

    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Read until video is completed
    cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # Read until video is completed
    while(cap.isOpened() and not event.is_set()):
        
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        # Display the resulting frame
            frame = cv2.resize(frame, (screen_width, screen_height))
            cv2.imshow('frame', frame)
            
        # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
    # Break the loop
        else:
            break
    
    # When everything done, release
    # the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()

def chooseVideo(event, data):
    #Choosing Vid Logic:
    pokName = -1
    if data.returning == True:
        pokName = data[pokemon_id]
        if (pokName not in pok.finalPok):
            vidName = "../Videos" + "ret"+ pok.evolutionDict[pokName] + ".mp4"
        else:
            vidName = "../Videos" + "boxes.mp4"
    else: # new with vidname corresponding to middle pokemon
        defaultPokList = pok.starterPok
        pokName = pok.evolutionDict[pok.starterPok[rand.randint(0,3)]]
        vidName = "../Videos" + pokName + ".mp4"


    readVideo(vidName, event)

    return ["bulbasaur", "squirtle",pokName, "charmander", "pikachu"]

# Initial Instructions Video
def instructionsVid(event):
    readVideo("defaultVid.mp4", event)

# 
def displayPokYouGot(pokemon,event):
    readVideo("defaultVid.mp4", event)

