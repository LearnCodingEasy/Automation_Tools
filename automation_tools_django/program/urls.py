# Page [ script_youtube/script_youtube_django/script/urls.py ]

from django.urls import path

from . import api

urlpatterns = [
    path("program_list/", api.program_list, name="program_list"),
    path("program_create/", api.program_create, name="program_create"),
    path("program_list/<uuid:id>/", api.program_list_dashboard,
         name="program_list_dashboard", ),
    path("run/<uuid:id>/", api.run_program,
         name="run_program"),
    path("open_vscode/", api.open_vscode,
         name="open_vscode"),


    # path("program_list/script_detail/<uuid:pk>/", api.script_detail, name="script_detail"
    # ),
    # path("program_list/script_edit/<uuid:pk>/", api.script_edit, name="script_edit"),
    # path("program_list/script_delete/<uuid:pk>/", api.script_delete, name="script_delete"
    # ),
]
