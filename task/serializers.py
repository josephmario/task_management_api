from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User
# from rest_framework.authtoken.views import Token

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','description', 'status']