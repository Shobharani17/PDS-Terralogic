from django.db import models

# Create your models here.
class employees(models.Model):
    name = models.CharField( max_length=600,null=True,blank=True)
    phone = models.TextField(null=True,blank=True)
    email=models.TextField( null=True,blank=True)
    college=models.CharField(max_length=500,null=True,blank=True)
    degree = models.CharField(max_length=252,null=True,blank=True)
    skills=models.TextField( null=True,blank=True)
    designation=models.TextField(null=True,blank=True)
    company=models.TextField(null=True,blank=True)
    file_location=models.CharField(max_length=250, null=True,blank=True)
    text_file_location=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

# class Meta:
#     db_table='employees'


class Upload_files(models.Model):
    files = models.FileField(upload_to="media")
    title = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.title)







# Username: Shobha6
# Password: chinni6
# chrome.exe --user-data-dir="C://Chrome dev session" --disable-web-security