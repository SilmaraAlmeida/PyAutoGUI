import pyautogui
import time

# https://pyautogui.readthedocs.io/en/latest/quickstart.html

pyautogui.PAUSE = 0.5 #semrpe dps de cada comando <pyautogui> ele vai fazer uma pausa

# posições da tela
# print(pyautogui.position())
# print(pyautogui.size())

# # mouse
# time.sleep(2)
# pyautogui.click(x=-1390, y=466)
# # mouse - botão direito
# pyautogui.click(x=-1390, y=466, button="right")
# # mouse - botão meio
# pyautogui.click(x=-1390, y=466, button="right")
# # mouse - quantidade cliques
# pyautogui.click(x=-1390, y=466, clicks=3)

pyautogui.moveTo(x=-1103, y=395, duration=0.4)
pyautogui.click()
