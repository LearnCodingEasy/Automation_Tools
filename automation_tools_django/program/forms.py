# Page [ script_youtube/script_youtube_django/script/forms.py ]

from django.forms import ModelForm

from .models import Program


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'description', 'program_path', 'status',
                  'commands', 'command_line_args', 'window_type',             'project_type',
                  'project_path',  
                  )
