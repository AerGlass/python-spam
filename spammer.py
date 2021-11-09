from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


time.sleep(1)
print("this app will send as many spam as you want")

i = 1
while i < 400:
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