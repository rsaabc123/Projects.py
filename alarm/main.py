#2-9-25
#alarm clock

import time
import datetime
import pygame # suppress greeting messages -> terminal -> pip show pygame -> location -> _init_.py

sound_file = "meow.wav"

def alarm_sound():
    pygame.mixer.init()
    cat_meow = pygame.mixer.Sound(sound_file)
    cat_meow.play()
    pygame.time.wait(2000) # time in milliseconds -> wait for 2 secs
    pygame.quit()

def set_alarm(alarm_time):
    print(f'\n*alarm set for {alarm_time}*')
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'\ncurrent time: {time.ctime()}')
        if current_time == alarm_time:
            print('\n*WAKE UP*')
            alarm_sound()
            break
        time.sleep(1)

def time_format_check(time_str):
    try:
        datetime.datetime.strptime(time_str,'%H:%M:%S')
        return True
    except ValueError:
        return False

def main():
    if __name__ == "__main__":
        print(f'\ncurrent time: {time.ctime()}')
        while True:
            print('enter alarm time (e.g., 8:30:00, 16:30:00)')
            alarm_time = input('>')
            if time_format_check(alarm_time):
                set_alarm(alarm_time)
            else:
                print('enter in valid time format (e.g., 8:30:00, 16:30:00) :]')

    else:
        print("run the program in the main file")

main()