from rest_framework import serializers
from .models import Folder, File
from rest_framework.response import Response

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields =[ "folder_name" , "folder"]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["folder", "file", ]
