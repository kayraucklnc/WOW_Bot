import pyautogui,time

five = []

for i in range(6):
    time.sleep(1.5)
    five.append((pyautogui.position()[0],pyautogui.position()[1]))
    print(pyautogui.position())
    time.sleep(1.3)
print(five)
