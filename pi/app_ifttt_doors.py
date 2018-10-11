import requests
from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = SenseHat()

def joystickUp(event):
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")
    
def joystickDown(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickLeft(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickRight(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickMiddle(event):
    if event.action == ACTION_RELEASED:

     temp = "{}°C".format(sense.get_temperature())
     hum = "{}%".format(sense.get_humidity())
     press = "{}.Ombar".format(sense.get_pressure())

     r = requests.post("https://maker.ifttt.com/trigger/sensors/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?",
                     data = {
                       "value1" : temp,
                       "value2" : hum,
                       "value3" : press          
                           })

     print(temp, hum, press)

sense.stick.direction_up = joystickUp
sense.stick.direction_down = joystickDown
sense.stick.direction_left = joystickLeft
sense.stick.direction_right = joystickRight
sense.stick.direction_middle = joystickMiddle

pause()
