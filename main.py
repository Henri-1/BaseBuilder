import pynput, time, random
from pynput.keyboard import Key, Controller as KeyboardController, Listener
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()  # Create the controller
mouse = MouseController()

time.sleep(5)


def press_key(string, wait_time):
    keyboard.press(string)
    time.sleep(wait_time)
    keyboard.release(string)
    #for character in string:  # Loop over each character in the string
     #   keyboard.type(character)  # Type the character
      #  delay = random.uniform(0, 0.1)  # Generate a random number between 0 and 10
       # time.sleep(delay)  # Sleep for the amount of seconds generated


def mouse_click_left():
    mouse.press(Button.left)
    mouse.release(Button.left)


def select_building(part):
    print (0)



mouse_click_left()

press_key('w', 0.5)
keyboard.press(Key.space)
press_key('w', 1)

mouse_click_left()
press_key('w', 1)
# wip
