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

"""
Name        |     Surname             | Email                   | Password 
html        |     html5               | html@html.com           | zxc123456789
css         |     css3                | css@css.com             | zxc123456789
javascript  |     ES6                 | javascript@javascript.com             | zxc123456789
vue         |     vue3                | vue@vue.com             | zxc123456789
npm         |     npm                 | npm@npm.com             | zxc123456789
php         |     php                 | php@php.com             | zxc123456789
sql         |     sql                 | sql@sql.com             | zxc123456789
"""
# إنشاء 100 مستخدمين
for i in range(1, 100):
    # 🕒 First name انتظار تحميل العناصر
    # تعبئة الاسم الأول
    FirstName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[1]/div[1]/input',
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
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[1]/div[2]/input',
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
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[2]/input',
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
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[3]/div/input',
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
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[4]/div/input',
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

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ClickOnDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[6]/div/div[1]',
            )
        )
    )
    ClickOnDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    YeerForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div/div/div/div/button',
            )
        )
    )
    YeerForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ChopseYeerForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseYeerForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ChopseMontheForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div[2]/span[1]',
            )
        )
    )
    ChopseMontheForDay.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ChopseDayForDay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="pv_id_3_panel"]/div/div/table/tbody/tr[1]/td[4]/span',
            )
        )
    )
    ChopseDayForDay.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ClickOnMonthe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[6]/div/div[2]',
            )
        )
    )
    ClickOnMonthe.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
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

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    ClickOnYear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[6]/div/div[3]',
            )
        )
    )
    ClickOnYear.click()

    # 🖱️ يقوم click() النقر على العنصر الموجود.
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

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    # اختيار الجنس
    ChopseGender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[8]/div[2]',
            )
        )
    )
    ChopseGender.click()

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________

    # 🖱️ يقوم click() النقر على العنصر الموجود.
    # النقر على زر التسجيل
    Signup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/button',
            )
        )
    )
    Signup.click()
    print(f"✅ User {i} created successfully")

    # انتظار قليل قبل الانتقال للمستخدم التالي
    time.sleep(3)

    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    # __________________________________________________
    print("✅ All users created successfully")

# إغلاق المتصفح
driver.quit()

# python scraping\generate_users_ling.py


def wait_and_send_keys(driver, xpath, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.send_keys(value)


def wait_and_click(driver, xpath, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()


users_data = [
    {
        "first_name": "html",
        "last_name": "html5",
        "email": "html@html.com",
        "password": "zxc123456789",
    },
    {
        "first_name": "css",
        "last_name": "css3",
        "email": "css@css.com",
        "password": "zxc123456789",
    },
    # ... بقية المستخدمين ...
]
