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

# https://www.youtube.com/watch?v=fPzzlGQxKMo&list=PLbJF4g421wqmWbqLHyJW5nYz0SLzkyYZG&index=4

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


# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________


# html
# css
# javascript
# vue
# vscode
# code1

VarEmail = "code50@code.com"
VarPassword = "zxc123456789"


# 🕒 Email انتظار تحميل العناصر
Email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/form/div/div[2]/div[1]/div[1]/div/div/input',
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
Password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/form/div/div[2]/div[1]/div[2]/div/input',
        )
    )
)
Password.send_keys(f"{VarPassword}")
# print(f"Password1 {Password1}")


# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________

# 🖱️ يقوم click() النقر على العنصر الموجود.
Login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/form/div/div[2]/div[2]/div/div/button',
        )
    )
)
Login.click()
print(f"✅ Login successful ")

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
# python scraping\login.py
