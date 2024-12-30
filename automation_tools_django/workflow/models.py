import uuid  # 🆔 لإنشاء معرّفات فريدة
from django.utils.timesince import timesince  # ⌛ لحساب الزمن المنقضي
from django.conf import settings  # ⚙️ لإعدادات المشروع
from django.db import models  # 🗃️ لإدارة قواعد البيانات
from user_account.models import User  # 👤 لربط المستخدمين بالبيانات


class Workflow(models.Model):
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="workflows",
        on_delete=models.CASCADE,
        verbose_name="Created By"
    )
    updated_at = models.DateTimeField(auto_now=True)

    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    name = models.CharField(max_length=255, blank=True, null=True, default="")

    class Meta:  # ⚙️ إعدادات النموذج
        # ⬇️ ترتيب السجلات تنازليًا حسب تاريخ الإنشاء
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.name

    def __unicode__(self):  # 🌐 دعم الترميز
        return


class Task(models.Model):

    workflow = models.ForeignKey(
        Workflow, on_delete=models.CASCADE, related_name='tasks')
    # يخزن الإعدادات لكل مهمة
    configuration = models.JSONField()
    # ترتيب المهمة في سير العمل
    order = models.PositiveIntegerField()
    # 🛠️ إعداد حالات مختلفة لحالة الدورة
    OPENVSCODE = "open_vscode"  # 🛎️ خدمات
    OPEN_URL = "open_url"  # 🛎️ فتح رابط
    CLICK_ELEMENT = "click_element"  # 🖱️ النقر على عنصر
    INPUT_TEXT = "input_text"  # 📝 إدخال نص
    WAIT = "wait"  # ⏳ الانتظار

    # ✅ تعريف خيارات الحالة
    STATUS_CHOICES = (
        (OPENVSCODE, "Open Vscode"),  # 🛎️ مواقع تقديم الخدمة
        (OPEN_URL, "Open URL"),  # 🛎️ فتح رابط
        (CLICK_ELEMENT, "Click Element"),  # 🖱️ النقر على عنصر
        (INPUT_TEXT, "Input Text"),  # 📝 إدخال نص
        (WAIT, "Wait"),  # ⏳ الانتظار

    )

    # 🏷️ حقل الحالة في النموذج
    task_type = models.CharField(
        max_length=25,  # ✏️ الحد الأقصى لعدد الأحرف هو 25
        choices=STATUS_CHOICES,  # 🗂️ الخيارات المتاحة للحقل
        default=OPENVSCODE,  # 🛎️ القيمة الافتراضية: مواقع تقديم الخدمة
    )
