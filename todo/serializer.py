from dataclasses import fields
from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'end_date', 'state')
        read_only_fields = ('id', 'created_at')
