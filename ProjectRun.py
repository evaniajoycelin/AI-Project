import tkinter as tk
from tkinter import *
import os
import speech_recognition as sr
import pyttsx3
import pygame
import time
from gtts import gTTS

root = tk.Tk()
root.title("Application Speech Recognition")
kata1 = ""
kata2 = ""
previous1 = "nothingatleastitsreallyanothingnothingyesyouneverknowhowtobreakthecode"
previous2 = "135thiscannotberightrightyouneedtoseethistobreakthecode"


def saved(fileNameDesu):
    global root
    canvas1 = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas1.pack()

    # frame1 = tk.Frame(newWindow, bg="#D3D3D3")
    frame1 = tk.Frame(root, bg="#D3D3D3")
    frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    root.geometry("700x700")

    spasi = Label(frame1, text="\n\n\n\n", font=("Times New Roman", 20), bg="#D3D3D3")
    spasi.pack()

    tulisan1 = Label(frame1, text="File saved as {}".format(fileNameDesu), font=("Times New Roman", 20))
    tulisan1.pack()
    root.update()
    root.after(3000)
    ttsWindow()


def pressed():
    print("it's pressed")


def entryRecognize(entry1, entry2):
    global kata1, kata2
    kata1 = str(entry1.get("1.0", END))
    kata2 = str(entry2.get())
    print(kata1)
    print(kata2)
    tts()


def tts():
    global kata1, kata2, previous1, previous2
    myobj = gTTS(text=kata1, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    fileName1 = kata2 + ".mp3"

    if fileName1 != previous1 or kata1 != previous2:
        pygame.mixer.music.load("dummy_do_not_delete.mp3")
        myobj.save(fileName1)

    print(fileName1)

    # Playing the converted file

    pygame.mixer.music.load(fileName1)
    pygame.mixer.music.play()

    # pygame.mixer.music.rewind()

    previous1 = fileName1
    previous2 = kata1
    saved(fileName1)

    # os.system("\"{}\"".format(fileName1))


def ttsWindow():
    global root
    # newWindow = tk.Toplevel(root)
    # canvas1 = tk.Canvas(newWindow, height=700, width=700, bg="#263D42")
    canvas1 = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas1.pack()

    # frame1 = tk.Frame(newWindow, bg="#D3D3D3")
    frame1 = tk.Frame(root, bg="#D3D3D3")
    frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    root.geometry("700x700")

    tulisan1 = Label(frame1, text="Input Text ", font=("Times New Roman", 20))
    tulisan1.pack()

    # entry1 = tk.Entry(frame1)
    ##    entry1.bind('<FocusOut>', entryRecognize)
    # entry1.place(width=150,height=50)
    # entry1.pack()

    entry1 = Text(frame1, height=4, width=20)
    entry1.pack()

    ##    teks=Text(frame1,height=4,width=20)
    ##    teks.pack()

    spasi = Label(frame1, text="", font=("Times New Roman", 20), bg="#D3D3D3")
    spasi.pack()

    tulisan2 = Label(frame1, text="File Name to save ", font=("Times New Roman", 20))
    tulisan2.pack()

    entry2 = tk.Entry(frame1)
    entry2.pack()

    ##    teks1=Text(frame1,height=1,width=20)
    ##    teks1.pack()

    # tts(entry1String, entry2String)

    ##    myobj = gTTS(text=entry1String, slow=False)
    ##
    ##        # Saving the converted audio in a mp3 file named
    ##        # welcome
    ##
    ##    fileName1 = teks1.get() + ".mp3"
    ##    myobj.save(fileName1)
    ##
    ##        # Playing the converted file
    ##    os.system("start {}.mp3".format(fileName))

    # buttons1 =Button(frame1, text="Get to Speech", padx=10, pady=5, fg="white", bg="#263D42",command=newWindow.destroy)
    buttons1 = Button(frame1, text="Get to Speech", padx=10, pady=5, fg="white", bg="#263D42",
                      command=lambda: entryRecognize(entry1, entry2))
    # canvas1.destroy
    # newWindow.destroy
    buttons1.pack()

    spasi2 = Label(frame1, text="\n\n", font=("Times New Roman", 20), bg="#D3D3D3")
    spasi2.pack()

    buttons2 = Button(frame1, text="Go back", padx=10, pady=5, fg="white", bg="#263D42", command=mainMenu)
    buttons2.pack()
    # canvas1.destroy
    # newWindow.destroy


def mainMenu():
    global root

    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    root.geometry("700x700")

    tulisan = Label(frame, text="Welcome to Our Application \n ================================",
                    font=("Times New Roman", 20), bg="white")
    tulisan.pack()

    button1 = tk.Button(frame, text="Spech to Text(STT)", padx=10, pady=5, fg="white", bg="#263D42", command=sttWindow)
    button1.pack()
    # button1.bind("<Button-1>", pressed())

    button2 = tk.Button(frame, text="Text to Speech(TTS)", padx=10, pady=5, fg="white", bg="#263D42", command=ttsWindow)
    button2.pack()
    # button2.bind("<Button-1>", pressed())

    button3 = tk.Button(frame, text="QUIT", padx=10, pady=5, fg="white", bg="#263D42", command=lambda: credit(0))
    button3.pack()


def saveToText(frame, speechtext, name_file):
    global root
    name_file1 = name_file + ".txt"
    file1 = open(name_file1, "w+")
    file1.write(speechtext)
    file1.close()
    tulisan1 = Label(frame, text="Data succesfully saved as {} ".format(name_file1), font=("Times New Roman", 20))
    tulisan1.pack()
    root.update()
    root.after(2000)
    mainMenu()


def saveRecognize(frame, speechtext):
    print(speechtext)
    tulisan1 = Label(frame, text="Input File Name ", font=("Times New Roman", 20))
    tulisan1.pack()

    entry1 = tk.Entry(frame)
    entry1.pack()

    buttons_yes = Button(frame, text="Save", padx=10, pady=5, fg="white", bg="#263D42",
                         command=lambda: [tulisan1.pack_forget(), entry1.pack_forget(), buttons_yes.pack_forget(),
                                          buttons_no.pack_forget(), saveToText(frame, speechtext, str(entry1.get()))])
    buttons_yes.pack()

    buttons_no = Button(frame, text="Cancel", padx=10, pady=5, fg="white", bg="#263D42", command=mainMenu)
    buttons_no.pack()


def sttWindow():
    global root
    # newWindow = tk.Toplevel(root)
    # canvas1 = tk.Canvas(newWindow, height=700, width=700, bg="#263D42")
    canvas1 = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas1.pack()

    # frame1 = tk.Frame(newWindow, bg="#D3D3D3")
    frame1 = tk.Frame(root, bg="#D3D3D3")
    frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    root.geometry("700x700")

    spasi = Label(frame1, text="\n\n\n\n", font=("Times New Roman", 20), bg="#D3D3D3")
    spasi.pack()

    tulisan_ready = Label(frame1, text="Getting Ready.... ", font=("Times New Roman", 20))
    tulisan_ready.pack()
    print("before speak sleep")
    # root.after(1000)
    print("after speak sleep")
    tulisan_timeover = Label(frame1, text="Time over, processing the speech.... ", font=("Times New Roman", 20))

    tulisan_sorry = Label(frame1, text="Sorry, I did not get that", font=("Times New Roman", 20))
    tulisan_asksave = Label(frame1, text="Do you want to save the text ?", font=("Times New Roman", 20))

    # THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_
    # time.sleep(1)
    root.update()
    r = sr.Recognizer()
    i = 0

    print("not adjust")

    with sr.Microphone() as source:
        print("before adjust")
        r.adjust_for_ambient_noise(source, duration=5)
        print("ready to speak")
        tulisan_ready.pack_forget()
        tulisan_speak = Label(frame1, text="Speak Now (Listening).... ", font=("Times New Roman", 20))
        tulisan_speak.pack()
        root.update()
        audio_text = r.listen(source)
        print("after listen")
        # tulisan_speak.pack_forget()
        tulisan_speak.pack_forget()
        tulisan_timeover.pack()
        root.update()
        print("timeover")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            tulisan_text = Label(frame1, text="You Said: {} ".format(text), font=("Times New Roman", 20))
            text = r.recognize_google(audio_text)
            tulisan_text.pack()
            i = 0
        except:
            tulisan_sorry.pack()
            i = 1

    tulisan_timeover.pack_forget()

    if i == 0:
        tulisan_asksave.pack()

        buttons_confirm = Button(frame1, text="Save", padx=10, pady=5, fg="white", bg="#263D42",
                                 command=lambda: entryRecognize(entry1, entry2))
        buttons_no2 = Button(frame1, text="Nevermind, go back to main menu", padx=10, pady=5, fg="white", bg="#263D42",
                             command=lambda: entryRecognize(entry1, entry2))

        buttons_yes = Button(frame1, text="Yes, save to txt", padx=10, pady=5, fg="white", bg="#263D42",
                             command=lambda: [saveRecognize(frame1, text), tulisan_text.pack_forget(),
                                              tulisan_asksave.pack_forget(), buttons_yes.pack_forget(),
                                              buttons_trys.pack_forget(), buttons_no.pack_forget()])
        buttons_yes.pack()

        buttons_trys = Button(frame1, text="Speak again", padx=10, pady=5, fg="white", bg="#263D42",
                              command=lambda: sttWindow())
        buttons_trys.pack()

        buttons_no = Button(frame1, text="No, go back to main menu", padx=10, pady=5, fg="white", bg="#263D42",
                            command=mainMenu)
        buttons_no.pack()

    ##        if (save_text == 'Y' or save_text == 'y'):
    ##            name_file = input("File name ? ")
    ##            name_file1 = name_file + ".txt"
    ##            file1 = open(name_file1, "w+")
    ##            file1.write(text)
    ##            file1.close()
    ##            print("Data has been saved")
    if i == 1:
        buttons_try = Button(frame1, text="Try again", padx=10, pady=5, fg="white", bg="#263D42",
                             command=lambda: sttWindow())
        buttons_try.pack()
        buttons_back = Button(frame1, text="Return to main menu", padx=10, pady=5, fg="white", bg="#263D42",
                              command=lambda: mainMenu())
        buttons_back.pack()

    # THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_THIS IS THE CODE_


def credit(step):
    global root
    canvas1 = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas1.pack()

    # frame1 = tk.Frame(newWindow, bg="#D3D3D3")
    frame1 = tk.Frame(root, bg="white")
    frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    root.geometry("700x700")

    for x in range(0, step - 3):
        spasi = Label(frame1, text=" ", font=("Times New Roman", 18), bg="white")
        spasi.pack()

    if step >= 3:
        tulisan_kelompok = Label(frame1, text="Made by group:", font=("Times New Roman", 18))
        tulisan_kelompok.pack()

    if step >= 2:
        tulisan_kelompok = Label(frame1, text="Abigail Vania (2101637005)", font=("Times New Roman", 18))
        tulisan_kelompok.pack()

    if step >= 1:
        tulisan_kelompok = Label(frame1, text="Evania Joycelin (2101667405)", font=("Times New Roman", 18))
        tulisan_kelompok.pack()

    if step >= 0:
        tulisan_kelompok = Label(frame1, text="Kelvin Samuel Seciawang (2101663092)", font=("Times New Roman", 18))
        tulisan_kelompok.pack()

    # tulisan_kelompok = Label(frame1, text="Made by group: \nAbigail Vania\nEvania Joycelin\nKelvin Samuel Seciawang",font=("Times New Roman",20))

    root.update()
    root.after(500)
    if step == 9:
        root.after(2000)
        root.destroy()
    else:
        credit(step + 1)


myobj = gTTS(text="o", slow=False)

# Saving the converted audio in a mp3 file named
# welcome

fileName1 = "dummy_do_not_delete.mp3"
myobj.save(fileName1)

pygame.mixer.init()
root.resizable(0, 0)
mainMenu()
root.mainloop()

root.mainloop()
