from playsound import playsound
import speech_recognition
import webbrowser
import os
import subprocess

# Initialize the recognizer
LISTENER = speech_recognition.Recognizer()

# the urls for the websites
# HASD TO BE THE FULL URL -- GO TO THE WEBSITE AND COPY IT DIRECTLY
SCHOOL_LINKS = []
GAMING_LINKS = ["https://www.chess.com/home", "https://www.youtube.com/"]

# the absolute path for the program launchers
# the path has to be for the program executable -- not shortcut
SCHOOL_PROGRAMS = []
GAMING_PROGRAMS = ["C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe"]


def play_audio(filepath : str):
    """
    plays an audio clip from a wav file

    filepath: the filepath of the wav file
    """
    playsound(filepath)
   
def get_user_input():
    """
    Listens for the user to say a phrase and then converts that phrase into text.
    if the user said a key word, stop listening
    """

    # Loop infinitely for user to speak
    while(1):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with speech_recognition.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                LISTENER.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                print("talk noiw")
                audio_clip = LISTENER.listen(source2)
                
                # Using google to recognize audio
                user_phrase = LISTENER.recognize_google(audio_clip)
                user_phrase = str(user_phrase).lower()
    
                if open_links(user_phrase):
                    print("done")
                    break
                
        except speech_recognition.RequestError as e:
            print("You are currently not connected to the internet, could not request results; {0}".format(e))

            
        except speech_recognition.UnknownValueError:
            print("please speak into the mic")

def open_links(phrase : str):
    """
    Checks if the user said a key word and opens the appropriate links / programs

    Return:
        boolean: whether the while loop should end
    """

    # if the user said "school"
    if "school" in phrase:
        for link in SCHOOL_LINKS: #opens links
            webbrowser.open(link)

        for program in SCHOOL_PROGRAMS: #runs programs
            subprocess.Popen([program])

        return True

    #if user said "game"
    elif "game" in phrase or "gaming" in phrase:
        for link in GAMING_LINKS: #opens links
            webbrowser.open(link)

        for program in GAMING_PROGRAMS: #runs programs
            subprocess.Popen([program])
        
        return True

    elif phrase.__contains__("no thanks"):
        return True

    else:
        return False

def main():
    
    # wav file name and file path of the initial audio msg
    audio_file_name = "ryan_01.wav"
    file_path = os.path.abspath(audio_file_name)

    play_audio(file_path)
    get_user_input()

    # requires import threading
    # filepath = "C:/Users/JP/OneDrive/Desktop/Personal Code/Power On Audio/ryan_01.wav"
    # t1 = threading.Thread(target=play_audio, args=(filepath,))
    # t1.start()
    # print("no thread")

    # t2 = threading.Thread(target=print_thread)
    # t2.start()

if __name__ =="__main__":
    main()

