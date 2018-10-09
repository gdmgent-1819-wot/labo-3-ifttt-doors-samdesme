import requests
from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = SenseHat()

def joystickUp(event):
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?value=frontdooropen")
    
def joystickDown(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?value=")

def joystickLeft(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?value=")

def joystickRight(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?value=")

sense.stick.direction_up = joystickUp
sense.stick.direction_down = joystickDown
sense.stick.direction_left = joystickLeft
sense.stick.direction_right = joystickRight
pause()
