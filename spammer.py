from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

repeats = int(input("Enter how many spam do you want.")
              
              
              print("Starting in 6 seconds")
              time.sleep(6)
              print("STARTING")
while i < repeats:
   keyboard.press("a")
   keyboard.release("a")
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   keyboard.press("b")
   keyboard.release("b")
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   keyboard.press("c")
   keyboard.release("c")
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   i += 1
