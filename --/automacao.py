import pyautogui
import time

# https://pyautogui.readthedocs.io/en/latest/quickstart.html

# posições da tela
print(pyautogui.position())
print(pyautogui.size())

# mouse
time.sleep(2)
pyautogui.click(x=-1390, y=466)

# mouse - botão direito
pyautogui.click(x=-1390, y=466, button="right")

# mouse - botão meio
pyautogui.click(x=-1390, y=466, button="right")

# mouse - quantidade cliques
pyautogui.click(x=-1390, y=466, clicks=3)
