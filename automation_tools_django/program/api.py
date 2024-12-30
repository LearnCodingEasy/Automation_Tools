# Page [ script_youtube/script_youtube_django/script/api.py ]

from django.http import JsonResponse
import subprocess
import os
from uuid import UUID

from django.db.models import Q
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from user_account.models import User
from user_account.serializers import UserSerializer

from .forms import ProgramForm
from .models import Program
from .serializers import ProgramSerializer
# , ScriptDetailSerializer

#
from rest_framework.response import Response


# @authentication_classes([])
# @permission_classes([])
# Program List
@api_view(["GET"])
def program_list(request):
    programs = Program.objects.all()
    # طباعة البرامج في وحدة التحكم
    # print(programs)
    # print(request)
    serializer = ProgramSerializer(programs, many=True)
    return JsonResponse(serializer.data, safe=False)


@authentication_classes([])
@permission_classes([])
@api_view(["POST"])
def program_create(request):
    # Handling the Script Form and Attachment Form
    form = ProgramForm(request.POST)
    # Proceed with the Script form if it's valid
    if form.is_valid():
        program = form.save(commit=False)
        program.created_by = request.user
        program.save()
        # If there's an attachment, associate it with the script
        # Increment user's script count
        user = request.user
        user.save()

        # Serialize the script and return as JSON response
        serializer = ProgramSerializer(program)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # If form validation fails, return error response
        # errors = form.errors.as_json()
        errors = {
            "program_errors": form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


@api_view(["GET"])
def program_list_dashboard(request, id):
    user = User.objects.get(pk=id)
    programs = Program.objects.filter(created_by_id=id)

    program_serializer = ProgramSerializer(programs, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse(
        {
            "programs": program_serializer.data,
            "user": user_serializer.data,
        },
        safe=False,
    )

# API لتشغيل برنامج معين


@api_view(["GET"])
def run_program(request, id):
    try:
        # التأكد أن المعرف UUID صالح
        # uuid_id = UUID(id, version=4)
        program = Program.objects.get(pk=id)
        # قراءة المسار والخيارات
        project_path = program.project_path if program.project_path else ""
        program_path = program.program_path
        # window_type = "--new-window"
        window_type = "--new-window" if program.window_type == "new window" else "current-window"
        # command_line_args = "." or ""
        command_line_args = f"project-path={
            project_path}" if project_path else ""
        print(f"Running program from path: {
              program_path} with project path: {project_path}")
        print(f"Window type: {window_type}, Command line args: {
              command_line_args}")

        # التحقق من وجود المسار
        if not program_path:
            return JsonResponse({"error": "Program path not found."}, status=400)

        # التأكد من أن المسار المشروع موجود
        if not os.path.exists(project_path):
            return JsonResponse({"error": "Project path does not exist."}, status=404)

        print(f"Program Path: {program_path}")
        print(f"Window Type: {window_type}")
        print(f"Project Path: {project_path}")
        print(f"Command Line Args: {command_line_args}")

        # تشغيل البرنامج
        # subprocess.Popen([program_path, window_type,
        #                   command_line_args], shell=True)
        subprocess.Popen(["code", project_path], shell=True)

        return JsonResponse(
            {"status": "success", "message": f"Program '{program.name}' is running."}
        )

    except Program.DoesNotExist:
        return JsonResponse({"error": "Program not found."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Invalid UUID format."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["GET"])
def open_vscode(request):
    try:
        result = subprocess.run(
            ["where", "code"], capture_output=True, text=True)
        # ✅ التحقق من نجاح العثور على المسار
        if result.returncode == 0:
            # عرض المسار إذا تم العثور على البرنامج
            print("✅ VS Code found:", result.stdout.strip())
        else:
            # رسالة خطأ إذا لم يتم العثور على البرنامج
            print("❌ VS Code not found. Make sure it is installed.")
        # 🚀 فتح Visual Studio Code في نافذة جديدة
        subprocess.Popen(
            [
                # المسار المباشر لتشغيل البرنامج
                "C:\\Users\\learn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "--new-window",  # فتح نافذة جديدة
                ".",  # فتح المجلد الحالي
            ]
        )
        return JsonResponse(
            {"status": "success", "message": f"Program  is running."}
        )

    except Program.DoesNotExist:
        return JsonResponse({"error": "Program not found."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Invalid UUID format."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# @api_view(["DELETE"])
# def script_delete(request, pk):
#     script = Script.objects.filter(created_by=request.user).get(pk=pk)
#     user = request.user
#     user.script_count = user.script_count - 1
#     user.save()
#     script.delete()
#     return JsonResponse({"message": "script deleted"})


# @api_view(["GET"])
# def script_detail(request, pk):
#     script = Script.objects.get(pk=pk)
#     user = script.created_by

#     user_serializer = UserSerializer(user)

#     script_serializer = ScriptDetailSerializer(script)
#     return JsonResponse(
#         {
#             "script": script_serializer.data,
#             "user": user_serializer.data,
#         },
#         safe=False,
#     )


# @api_view(["GET", "PUT"])
# def script_edit(request, pk):
#     # Get the script object to update
#     script = get_object_or_404(Script, pk=pk, created_by=request.user)

#     if request.method == "GET":
#         # Serialize the script data and return as JSON
#         serializer = ScriptSerializer(script)
#         return JsonResponse(serializer.data, status=200)  # HTTP 200 OK

#     elif request.method == "PUT":
#         # Handling the Script Form, Attachment Form, and Video Form
#         form = ScriptForm(request.data, instance=script)
#         attachment_form = AttachmentForm(request.data, request.FILES)
#         video_form = VideoForm(request.data, request.FILES)

#         # Update the attachment if valid
#         attachment = None
#         if attachment_form.is_valid():
#             attachment = attachment_form.save(commit=False)
#             attachment.created_by = request.user
#             attachment.save()

#         # Update the video if valid
#         video = None
#         if video_form.is_valid():
#             video = video_form.save(commit=False)
#             video.created_by = request.user
#             video.save()

#         # Proceed with updating the script if valid
#         if form.is_valid():
#             script = form.save()

#             # Associate updated attachment and video with the script
#             if attachment:
#                 script.attachments.add(attachment)
#             if video:
#                 script.videos.add(video)

#             # Serialize the updated script and return as JSON response
#             serializer = ScriptSerializer(script)
#             return JsonResponse(serializer.data, status=200)  # HTTP 200 OK
#         else:
#             # If form validation fails, return error response
#             errors = {
#                 "script_errors": form.errors,
#                 "attachment_errors": attachment_form.errors,
#                 "video_errors": video_form.errors,
#             }
#             return JsonResponse({"error": errors}, status=400)
