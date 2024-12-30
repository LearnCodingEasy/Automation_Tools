# 📄 صفحة [account/account_django/account/models.py]

# 🌟 1️⃣ **from django.contrib import admin**
#     - يتم هنا استيراد الوحدة `admin` من مكتبة Django.
#     - وحدة `admin` توفر لوحة تحكم إدارية جاهزة لإدارة النماذج (Models) والبيانات في المشروع.
#
# 🌟 2️⃣ **from .models import User**
#     - يتم استيراد النموذج (Model) `User` من ملف `models.py` الموجود في نفس التطبيق.
#     - النموذج `User` يُستخدم لتمثيل جدول في قاعدة البيانات يحتوي على معلومات مثل المستخدمين.
#
# 🌟 3️⃣ **admin.site.register(User)**
#     - يتم تسجيل النموذج `User` داخل لوحة التحكم الإدارية باستخدام هذا السطر.
#     - بعد التسجيل، سيظهر النموذج `User` في لوحة التحكم الإدارية، ويمكن للمسؤولين إضافة، تعديل، أو حذف البيانات المتعلقة به.
#     - تسجيل النموذج يجعل إدارة البيانات أكثر سهولة ومرونة من خلال واجهة المستخدم الإدارية.

# 🛠️ استيراد أدوات الإدارة
from django.contrib import admin

# 🌐 استيراد نموذج موقع الويب
from .models import User, FriendshipRequest

# admin.site.register(FriendshipRequest)


# 🖥️ تخصيص عرض النموذج في لوحة الإدارة
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 🌟 الحقول التي ستظهر في قائمة الإدارة
    list_display = (
        "name",
        "surname",
        "is_online",
        "email",
    )

    # 🔍 تمكين البحث عبر الحقول
    search_fields = ("name", "surname")

    # 🗂️ إضافة فلاتر حسب اللغة
    list_filter = ("is_online",)

    # 🔃 ترتيب النتائج حسب الاسم
    ordering = ("name",)

    # 📝 تحديد الحقول التي يمكن تعديلها داخل شاشة تحرير المستخدم
    # fields = ("name", "surname", "email", "is_online")


# 🖥️ تخصيص عرض النموذج في لوحة الإدارة
@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    # 🌟 الحقول التي ستظهر في قائمة الإدارة
    list_display = (
        "created_for",
        "created_by",
        "status",
    )

    # 🔍 تمكين البحث عبر الحقول
    search_fields = ("created_for", "created_by", "status")

    # 🗂️ إضافة فلاتر حسب اللغة
    list_filter = ("status",)

    # 🔃 ترتيب النتائج حسب الاسم
    ordering = ("status",)

    # 📝 تحديد الحقول التي يمكن تعديلها داخل شاشة تحرير المستخدم
    fields = ("created_at", "created_for", "created_by", "status")
