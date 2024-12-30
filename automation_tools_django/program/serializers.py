# Page [ script_youtube/script_youtube_django/script/serializers.py ]

from rest_framework import serializers

from user_account.serializers import UserSerializer

from .models import Program


class ProgramSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Program
        fields = (
            'id',
            'created_at',
            'created_at_formatted',
            'last_run',
            'created_by',
            'name',
            'description',
            'program_path',
            'status',
            'commands',
            'command_line_args',
            'window_type',
            'project_type',
            'project_path',
        )


class ProgramDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)


class Meta:
    model = Program
    fields = (
        'id',
        'created_at',
        'created_at_formatted',
        'last_run',
        'created_by',
        'name',
        'description',
        'program_path',
        'status',
        'commands',
        'command_line_args',
        'window_type',
        'project_type',
        'project_path',
    )
