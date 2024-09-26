from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# פתיחת דפדפן (למשל Chrome)
driver = webdriver.Chrome()

# טוען דף עם קישורים לסרטונים
video_links = [
    "https://www.youtube.com/watch?v=sJG9oBAzn00",  # החלף עם מזהה הסרטון הראשון
    "https://www.youtube.com/watch?v=uUx0j_TnDCw",  # החלף עם מזהה הסרטון השני
    "https://www.youtube.com/watch?v=iz9vAK3TH_E"   # החלף עם מזהה הסרטון השלישי
]

# פותח את הסרטון הראשון
driver.get(video_links[0])
pyautogui.press("k")
time.sleep(15)  # מחכה לטעינת הדף

# הוספת סרטון שני
driver.get(video_links[1])
time.sleep(0.1)
pyautogui.press('shift')
pyautogui.press('>')
time.sleep(15)  # מחכה לטעינת הדף

# הוספת סרטון שלישי במהירות שונה
driver.get(video_links[2])
time.sleep(0.1)  # מחכה לטעינת הדף
# pyautogui.press('k')  # מתחיל את הסרטון מחדש
pyautogui.press('shift')
pyautogui.press('>')
# השהייה של מספר שניות לראות את התוצאה
time.sleep(60)  # תוכל לשנות את הזמן לפי הצורך

# סגירת הדפדפן
driver.quit()