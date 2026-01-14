import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.sleep(3)
pyautogui.click(x=760, y=372)
pyautogui.write("pedromacedo89@hotmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("enter")
pyautogui.sleep(3)
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.click(x=801, y=261)
pyautogui.write("MOLO000251")
pyautogui.press("tab")

pyautogui.write("Logitech")
pyautogui.press("tab")

pyautogui.write("Mouse")
pyautogui.press("tab")

pyautogui.write("Periferico")
pyautogui.press("tab")

pyautogui.write("29.50")
pyautogui.press("tab")

pyautogui.write("6.50")
pyautogui.press("tab")

pyautogui.write("NaN")
pyautogui.press("tab")

pyautogui.press("enter")

pyautogui.scroll(5000)


