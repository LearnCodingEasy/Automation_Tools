# 📄 ملف [ account/account_django/account_django/urls.py ]

# 🌐 تكوين الروابط الرئيسية لمشروع Django
# 🌐 Main URL Configuration for Django Project

# 🔧 استيراد لوحة تحكم الإدارة من Django
from django.contrib import admin

# 🔗 استيراد الدوال path و include من Django لتحديد الروابط
from django.urls import (
    path,
    include,
)

# ⚙️ استيراد إعدادات Django
from django.conf import settings

# 📁 استيراد static لعرض ملفات الوسائط
from django.conf.urls.static import static


urlpatterns = [
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    # 🌐 Include URLs from the 'account' app for API endpoints
    # 🔗 الرابط الأساسي الذي يوجه إلى تطبيق "account" للحصول على النقاط البرمجية
    path("api/", include("user_account.urls")),
    path("api/programs/", include("program.urls")),
    # path("accounts/", include("allauth.urls")),
    #
    # path("api/notifications/", include("notification.urls")),
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    # 🌐 Admin panel for site management
    # 🔑 الرابط للوصول إلى لوحة تحكم الإدارة في Django
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ عرض ملفات الوسائط أثناء التطوير
# 🌐 Serve media files during development
# 🎥 تقوم هذه السطر بإعداد نظام عرض ملفات الوسائط (مثل الصور والفيديوهات) أثناء مرحلة التطوير باستخدام الروابط المحددة في الإعدادات (settings).
