# 📝 صفحة [account/account_django/account/serializers.py]
#
# 🔄 هذا الملف يحتوي على السيريالايزر (Serializers)، والتي تُستخدم لتحويل البيانات بين النماذج (Models) و JSON.
# 🌟 السيريالايزر مهم في Django Rest Framework لتسهيل التعامل مع البيانات عند إنشاء واجهات برمجة التطبيقات (APIs).

# 🌟 1️⃣ استيراد الإطار لتحويل البيانات
# - يتم استيراد الوحدة `serializers` من مكتبة Django Rest Framework.
from rest_framework import serializers

# 🌟 2️⃣ استيراد النماذج
# - استيراد نماذج البيانات `User` و `FriendshipRequest` من ملف `models.py`.
# - هذه النماذج تمثل جداول البيانات التي سيتم تحويلها عبر السيريالايزر.
from .models import User, FriendshipRequest


# 🧑 3️⃣ **UserSerializer**
# - السيريالايزر المستخدم لتحويل بيانات نموذج `User` إلى JSON والعكس.
# - يستخدم لتحليل البيانات المتعلقة بالمستخدمين عند إرسالها أو استقبالها.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # ✨ النموذج المرتبط بالسيريالايزر
        model = User
        # 🔍 الحقول المراد تضمينها في الاستجابة
        fields = (
            "id",  # 🆔 المعرف الفريد للمستخدم
            "name",  # 👤 الاسم الأول
            "surname",  # 👥 اسم العائلة
            "email",  # 📧 البريد الإلكتروني
            "date_of_birth",  # 🎂 تاريخ الميلاد
            "gender",  # ⚧ الجنس
            "get_avatar",  # 🖼️ رابط صورة الملف الشخصي
            "get_cover",  # 🖼️ رابط صورة الغلاف
            "friends_count",  # 👫 عدد الأصدقاء
            "task_count",  # 📋 عدد المهام
            "date_joined",  # 📅 تاريخ الانضمام
            "date_joined_formatted",  # 🗓️ تنسيق تاريخ الانضمام
            "last_login",  # ⏱️ آخر تسجيل دخول
            "last_login_formatted",  # 🕒 تنسيق تاريخ آخر تسجيل دخول
            "is_online",  # 🔵 حالة الاتصال (متصل أم لا)
            "skills",  #
        )


# 👫 4️⃣ **FriendshipRequestSerializer**
# - السيريالايزر المستخدم لتحويل بيانات طلبات الصداقة إلى JSON والعكس.
# - يحتوي على بيانات المرسل والمعلومات الأساسية عن الطلب.


class FriendshipRequestSerializer(serializers.ModelSerializer):
    # 👤 استخدام `UserSerializer` لعرض معلومات المرسل (قراءة فقط).
    created_by = UserSerializer(read_only=True)

    class Meta:
        # ✨ النموذج المرتبط بالسيريالايزر
        model = FriendshipRequest
        # 🔍 الحقول المراد تضمينها في الاستجابة
        fields = (
            "id",  # معرف الطلب
            "created_by",  # بيانات المرسل
            "status",  # حالة الطلب (مقبول، مرفوض، قيد الانتظار)
        )
