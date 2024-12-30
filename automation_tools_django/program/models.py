import uuid  # 🆔 لإنشاء معرّفات فريدة
from django.utils.timesince import timesince  # ⌛ لحساب الزمن المنقضي
from django.conf import settings  # ⚙️ لإعدادات المشروع
from django.db import models  # 🗃️ لإدارة قواعد البيانات
from user_account.models import User  # 👤 لربط المستخدمين بالبيانات


class Program(models.Model):
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_run = models.DateTimeField(auto_now=True, verbose_name="Last Run")
    created_by = models.ForeignKey(
        User,
        related_name="scripts",
        on_delete=models.CASCADE,
        verbose_name="Created By"
    )

    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    description = models.TextField(
        blank=True, null=True, verbose_name="Description")
    program_path = models.CharField(
        max_length=512, blank=True, null=True, verbose_name="Program Path")
    status = models.BooleanField(
        default=False, verbose_name="Not Active Status")
    commands = models.TextField(blank=True, null=True, verbose_name="Commands")
    # الأوامر الممررة عند التشغيل
    command_line_args = models.TextField(
        blank=True, null=True, verbose_name="Command Line Arguments")

    # 🛠️ إعداد حالات مختلفة لحالة الدورة
    NEWWINDOW = "new window"
    CURRENTWINDOW = "current window"

    # ✅ تعريف خيارات الحالة
    STATUS_CHOICES = (
        (NEWWINDOW, "--new-window"),
        (CURRENTWINDOW, "Current Window"),
    )

    # نوع النافذة
    window_type = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=NEWWINDOW,
    )
    project_path = models.CharField(
        max_length=512, 
        blank=True, 
        null=True, 
        verbose_name="Project Path",
        default=""
    )
    project_type = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Project Type", 
        default=""
    )



    class Meta:  # ⚙️ إعدادات النموذج
        # ⬇️ ترتيب السجلات تنازليًا حسب تاريخ الإنشاء
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.name

    def __unicode__(self):  # 🌐 دعم الترميز
        return
