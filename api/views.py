from rest_framework.decorators import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


class CreateFolder(APIView):
    def post(self, request):
        data = request.data
        serializer = FolderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "data Created", "data": request.data})


class CreateFile(APIView):
    def post(self, request, format=None):
        print("{===========================================")
        data = request.data
        print("🚀 ~ file: views.py ~ line 24 ~ data", data)
        serializer = FileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "data Created"})


class ViewDirectory(APIView):
    def get(self, request, id=None):
        if id:
            file = File.objects.filter(folder=id)
            folder =Folder.objects.filter(folder=id)
            serializers_file = FileSerializer(file, many=True)
            serializers_folder = FolderSerializer(folder , many=True)
            return Response({"folder-data":serializers_folder.data, "file-data":serializers_file.data ,})
        else:
            file = File.objects.filter(folder=None)
            folder = Folder.objects.filter(folder=None)
            serializers_file = FileSerializer(file, many=True)
            serializers_folder = FolderSerializer(folder, many=True)
            return Response({"folder-data":serializers_folder.data , "file-data":serializers_file.data ,})









