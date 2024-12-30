
from pathlib import Path

# استيراد مكتبة timedelta عشان نحدد مدة صلاحية التوكين
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jmk%c5(p#gqi-%31-$19dv09!!%obm6rd&@=h!4no@n3e**tjj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS ده المتغير اللي بنحدد فيه الدومينات أو الآيبيهات اللي مسموح لها تشغل المشروع
# URL أو على سيرفر حقيقي (localhost) الموقع اللي بنشتغل عليه سواء كان محلي
WEBSITE_URL = "http://127.0.0.1:8000"
# AUTH_USER_MODEL ده اللي بنحدد فيه موديل المستخدمين اللي شغالين عليه
AUTH_USER_MODEL = "user_account.User"
# SIMPLE_JWT دي إعدادات مكتبة JWT اللي بنستخدمها لإدارة التوكينات
SIMPLE_JWT = {
    # ACCESS_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين الدخول
    # (Access Token)، هنا مدته 30 يوم
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    # REFRESH_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين التحديث
    # (Refresh Token)، هنا مدته 180 يوم
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    # ROTATE_REFRESH_TOKENS ده اللي بيحدد لو التوكين بيتجدد مع كل تحديث للتوكين ولا لأ، هنا مش بيتجدد
    "ROTATE_REFRESH_TOKENS": False,
}
# REST_FRAMEWORK دي إعدادات مكتبة Django Rest Framework
REST_FRAMEWORK = {
    # DEFAULT_AUTHENTICATION_CLASSES دي اللي بتحدد نوع المصادقة الافتراضية اللي هتكون JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # DEFAULT_PERMISSION_CLASSES دي بتحدد الإذن الافتراضي اللي هو أن المستخدم لازم يكون مصدق عليه (Authenticated)
    # rest_framework.permissions.IsAuthenticated
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}
# CORS_ALLOWED_ORIGINS دي بنحدد فيها الأصول المسموح لها تتواصل مع السيرفر بتاعنا
CORS_ALLOWED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
    "http://192.168.1.5:5173",
    "http://127.0.0.1:5173",  # المنفذ الذي يعمل عليه Vite
]
# CSRF_TRUSTED_ORIGINS دي بنحدد فيها الأصول الموثوقة اللي بنسمح لها تستخدم
# CSRF مع السيرفر
CSRF_TRUSTED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
    "http://192.168.1.5:5173",
    "http://192.168.1.5:5174",
]
CORS_ALLOW_CREDENTIALS = True


# ______________ 📺 __________________
# أثناء التطوير
# للسماح بكل الطلبات أثناء التطوير
# استبدل 192.168.1.5 بعنوان IP لجهاز الكمبيوتر.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.1.5"]
# CORS_ALLOW_ALL_ORIGINS = True
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False


# python manage.py runserver 0.0.0.0:8000
# _______________________________

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps
    "user_account",
    "program",
    "workflow",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'automation_tools_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'automation_tools_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
