from django.db import models

# Create your models here.
class Folder(models.Model):
    folder_name = models.CharField(max_length=100)
    folder = models.ForeignKey('self', on_delete=models.CASCADE , null=True ,related_name='+')
    
    def __str__(self):
        return self.folder_name # TODO

class File(models.Model):
    folder = models.ForeignKey(Folder , on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to ='uploads/', null=True)

    def __str__(self):
        return str(self.file)
