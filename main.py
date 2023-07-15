from playsound import playsound
import speech_recognition
import webbrowser
import json

# Initialize the recognizer
LISTENER = speech_recognition.Recognizer()

# opens config file
with open("config.json") as file:
    config = json.load(file)


# the urls for the websites or the absolute path for exe files
# (HAS TO BE THE FULL URL -- GO TO THE WEBSITE AND COPY IT DIRECTLY)
SCHOOL_LINKS = config["SCHOOL_LINKS"]
GAMING_LINKS = config["GAMING_LINKS"]

# the absolute path for the program launchers
# the path has to be for the program executable -- not shortcut
# have path use / not \

# wav file paths
GREETING = config["GREETING"]

# dict that matches the audio resonse that will be played depending on what the user says
RESPONSE_DICT = config["RESPONSE_DICT"]

file.close() # closes config file


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
                audio_clip = LISTENER.listen(source2)
                
                # Using google to recognize audio
                user_phrase = LISTENER.recognize_google(audio_clip)
                user_phrase = str(user_phrase).lower()
    
                result = open_links(user_phrase)
                if result != "empty":
                    return result
                
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
            
        return "school"

    #if user said "game"
    elif "game" in phrase or "gaming" in phrase:
        for link in GAMING_LINKS: #opens links
            webbrowser.open(link)

        return "game"

    elif "no thanks" in phrase:
        return "none"

    else:
        return "empty"

def main():
    open_links("game")
    # wav file path of the initial audio msg
    # play_audio(GREETING)

    # user_response = get_user_input()

    # ai_response = RESPONSE_DICT[user_response]
    # play_audio(ai_response)

    """
    to do list:
        - add audio clips to play when the get_user_input method throws an error
        - write readme
            - add that os.startfile can be replaced with subprocess.Popen()
    """

if __name__ =="__main__":
    main()

