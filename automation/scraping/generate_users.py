from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# إعداد المتصفح
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# فتح صفحة التسجيل
driver.get("http://localhost:5173/login")
print("🖥️ Browser opened")


# إنشاء 100 مستخدمين
for i in range(10, 50):
    # 🕒 First name انتظار تحميل العناصر
    # تعبئة الاسم الأول
    FirstName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div[1]/input',
            )
        )
    )
    FirstName.send_keys(f"code {i}")
    # print(f"First Name {FirstName}")

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🕒 First name انتظار تحميل العناصر
    # تعبئة اسم العائلة
    SurName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div[2]/input',
            )
        )
    )
    SurName.send_keys(f"code {i}")
    # print(f"SurName {SurName}")

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🕒 Email انتظار تحميل العناصر
    # تعبئة البريد الإلكتروني
    Email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[2]/input',
            )
        )
    )
    Email.send_keys(f"code{i}@code.com")
    # print(f"Email {Email}")

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🕒 Password1 انتظار تحميل العناصر
    # تعبئة كلمة المرور
    Password1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[3]/div/input',
            )
        )
    )
    Password1.send_keys("zxc123456789")
    # print(f"Password1 {Password1}")

    # 🕒 Password2 انتظار تحميل العناصر
    # تعبئة كلمة المرور
    Password2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[4]/div/input',
            )
        )
    )
    Password2.send_keys("zxc123456789")
    # print(f"Password2 {Password2}")

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود [Clik On Day Input]
    ClickOnDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3"]',
            )
        )
    )
    ClickOnDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. [ Click On 2024 ]
    YeerForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div/div/div/div/button',
            )
        )
    )
    YeerForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. [ click On Year 2020 ]
    ChopseYeerForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseYeerForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. [ Click On MANTH 01 ]
    ChopseMontheForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseMontheForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click On Day 01
    # '//*[@id="pv_id_3_panel"]/div/div/table/tbody/tr[1]/td[4]/span', 01
    # '//*[@id="pv_id_3_panel"]/div/div/table/tbody/tr[2]/td[3]/span', 07
    ChopseDayForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="pv_id_3_panel"]/div/div/table/tbody/tr[2]/td[3]/span')
        )
    )
    ChopseDayForDay.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click In Input Monht
    ClickOnMonthe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_4"]/input',
            )
        )
    )
    ClickOnMonthe.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click On Manth 01
    ChopseMontheForMonthe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_4_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseMontheForMonthe.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click On Input Year
    ClickOnYear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_5"]/input',
            )
        )
    )
    ClickOnYear.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click On Year 2020
    ChopseYearForYear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_5_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseYearForYear.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click On Gender
    # اختيار الجنس
    ChopseGender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="ingredient2"]',
            )
        )
    )
    ChopseGender.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود. Click Button To Send
    # النقر على زر التسجيل
    Signup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[1]/div/div/form/div/div[2]/div[2]/div/button',
            )
        )
    )
    Signup.click()
    print(f"✅ User {i} created successfully")

    # 🕒 انتظار قليل قبل الانتقال للمستخدم التالي
    time.sleep(10)

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    print("✅ All users created successfully")

# إغلاق المتصفح
driver.quit()

# python scraping\generate_users.py
