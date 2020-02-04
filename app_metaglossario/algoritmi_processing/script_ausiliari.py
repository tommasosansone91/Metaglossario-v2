import sys
import time



def printout():

    print("Script richiamato con successo!")
    start_time = time.time()
    return start_time


def printout_input(input):

    start_time = time.time()
    script_name = "Script di conferma"
    print("%s richiamato con successo con il seguente input: %s" % (script_name, input))
    
    return start_time


def finish_sound():
    
    # import winsound
    # duration = 150  # milliseconds
    # freq = 440  # Hz
    # winsound.Beep(freq, duration)
    # winsound.Beep(freq, duration)
    # winsound.Beep(freq, duration)

    from playsound import playsound
    # import os    

    # from django.contrib.staticfiles import finders

    # result = finders.find('static/sounds/1607.mp3')
    # searched_locations = finders.searched_locations

    # # print(searched_locations[0])
    # # print(os.path.join(searched_locations[0]+r'\sounds\1607.mp3'))

    # sound_dir = os.path.join(searched_locations[0]+r'\sounds\1607.mp3')

    # playsound(sound_dir)

    # print("(Suono di fine script eseguito!)")
