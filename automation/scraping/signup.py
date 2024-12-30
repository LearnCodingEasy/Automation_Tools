"""
```
pip install selenium
```

```
pip install webdriver-manager
```

```
pip install pandas
```


"""

# 🚀 استيراد المكتبات المطلوبة

# مكتبة
# Selenium
# للتحكم في المتصفح
from selenium import webdriver

# خدمة لإدارة
# ChromeDriver
from selenium.webdriver.chrome.service import Service

# مدير لتحميل
# ChromeDriver
# تلقائيًا
from webdriver_manager.chrome import ChromeDriverManager


# 🕒 انتظار تحميل العناصر في الصفحة
from selenium.webdriver.support.ui import WebDriverWait

# لتحديد عناصر
# HTML
# باستخدام طرق مختلفة
# (مثل ID أو CLASS)
from selenium.webdriver.common.by import By


# إضافة خطوة لإغلاق المتصفح بعد فترة لتجنب غلقه مبكرًا
import time


"""
WebElement 🛠️: هو الكائن الذي يمثل العنصر في الصفحة ويدعم التفاعل معه (مثل النقر والإرسال والقراءة).

_____________

📖 الاستخدام: يتم استخدام 
WebElement 
للتعامل مع العناصر داخل الصفحة، مثل:

إرسال نصوص إلى مربع إدخال.
النقر على أزرار.
قراءة النصوص الموجودة في العناصر.
"""
from selenium.webdriver.remote.webelement import WebElement

"""
expected_conditions ⏳: هي شروط تُستخدم مع الانتظار الذكي 
WebDriverWait 
للتأكد من أن العنصر جاهز قبل التفاعل معه.

_____________

📖 الاستخدام:

expected_conditions هي مجموعة من الشروط التي يمكن استخدامها مع 
WebDriverWait 
لانتظار حالة معينة للعنصر.

الشروط الشائعة:
presence_of_element_located: انتظار وجود العنصر في DOM.
element_to_be_clickable: انتظار أن يصبح العنصر قابلاً للنقر.
visibility_of_element_located: انتظار ظهور العنصر على الشاشة.

"""
from selenium.webdriver.support import expected_conditions as EC


import pandas as pd


"""
🛠️  إعداد المتصفح  
ChromeDriver باستخدام
WebDriverManager هنا نقوم بإنشاء كائن
ChromeDriverManager واستخدام الدالة
install() لتحميل الإصدار المتوافق
"""
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# تكبير نافذة المتصفح
driver.maximize_window()
print("Starting the browser")


# فتح صفحة
driver.get("http://localhost:5173/login")
print("🖥️ Browser opened")

# طباعة اسم الصفحة
print(f"📝 Page Title {driver.title}")


# Html html
# Css css
# Javascript javascript
# Vue vue

varName = "Css"
VarSurName = "Css 3"
VarEmail = "css@css.com"
VarPassword = "zxc123456789"

# 🕒 First name انتظار تحميل العناصر
FirstName = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[1]/div[1]/input',
        )
    )
)
# FirstName.send_keys("Html")
FirstName.send_keys(f"{varName}")
# print(f"First Name {FirstName}")

# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________

# 🕒 First name انتظار تحميل العناصر
SurName = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[1]/div[2]/input',
        )
    )
)
# SurName.send_keys("Html 5")
SurName.send_keys(f"{VarSurName}")
# print(f"SurName {SurName}")

# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________


# 🕒 Email انتظار تحميل العناصر
Email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[2]/input',
        )
    )
)
# Email.send_keys("html@html.com")
Email.send_keys(f"{VarEmail}")
# print(f"Email {Email}")

# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________

# 🕒 Password1 انتظار تحميل العناصر
Password1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[3]/div/input',
        )
    )
)
Password1.send_keys(f"{VarPassword}")
# print(f"Password1 {Password1}")

# 🕒 Password2 انتظار تحميل العناصر
Password2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div/div[4]/div/input',
        )
    )
)
Password2.send_keys(f"{VarPassword}")
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
Signup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/button',
        )
    )
)
Signup.click()
print(f"✅ Signup {varName} successful ")

time.sleep(10)

# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________


# # الانتظار قبل الإغلاق
# # الانتظار لمدة 1000 ثوانٍ لملاحظة التفاعل
time.sleep(300)


# لجعل الصفحة تبقى مفتوحة
driver.quit()


# Run
# python Automaiton\scraping\signup.py
