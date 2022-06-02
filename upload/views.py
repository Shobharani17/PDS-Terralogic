# from text_file_location.policy import default
from ast import iter_fields, keyword
from importlib import resources
from operator import index
from tkinter.tix import COLUMN
from unicodedata import name
from urllib import response
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from . import models
from . import serializers
import codecs
import os
import csv
import json
import re
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import employees
from django import forms
from django.db import IntegrityError
fs = FileSystemStorage(location='tmp/')
# Serializer
class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = "__all__" 
# Viewset
class UploadFileForm(forms.Form):
    file = forms.FileField()

class employeesViewSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
    
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from Json"""
        file = request.FILES["file"]
        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.json", file_content
        )
        tmp_file = fs.path(file_name)
        Json_file = open(tmp_file, errors="ignore")
        
        reader = json.loads(Json_file.read())
        reader1= json.dumps(reader)
        reader2=reader1.translate(str.maketrans({"[": '', "]": '', "'": ''}))
        file1 = reader2
        content1 = file1.rstrip()  # these are bytes
        file_content1 = ContentFile(content1)
        file_name1 = fs.save(
            "_new.json", file_content1
        )
        tmp_file1 = fs.path(file_name1)
        Json_file1 = open(tmp_file1, errors="ignore")
        
        reader2 = json.loads(Json_file1.read())
        reader2.values()
        for values in reader2.values():
            employees_list = [values]
            employees_list1 = []
            for _id,row in enumerate(employees_list):
                (
                    name,
                    phone,
                    email,
                    college,
                    degree,
                    skills,
                    designation,
                    company,
                    file_location,
                    text_file_location,
                ) = row
                employees_list1.append(
                    employees(
                        # name=name,
                        # phone=phone,
                        # email=email,
                        # college=college,
                        # degree=degree,
                        # skills=skills,
                        # designation=designation,
                        # company=company,
                        # file_location=file_location,
                        # text_file_location=text_file_location,
                    )
                )
            defaults= {'name' : row['name'], 'phone' : row['phone'],
                        'email' : row['email'],'college':row['college'],'degree':row['degree'] ,
                        'skills' : row['skills'], 'designation' : row['designation'],
                        'company' : row['company'], 'file_location' : row['file_location'],
                        'text_file_location' : row['text_file_location']}
            try:
                # obj = employees.objects.get(name=name, email=email)
                obj = employees.objects.get(name=row['name'], email=row['email'])
                for key, value in defaults.items():
                    setattr(obj, key, value)
                obj.save()
            except employees.DoesNotExist:
                new_values = {'name': 'name', 'email': 'email'}
                new_values.update(defaults)
                obj = employees(**new_values)
                obj.save()
        return Response("Successfully uploaded JSON data!!!......")








# from email.policy import default
# from importlib import resources
# from operator import index
# from django.shortcuts import redirect, render
# from rest_framework import viewsets
# from . import models
# from . import serializers
# # from rest_framework.viewsets import ViewSet
# # from rest_framework.response import Response
# # from .serializers import UploadSerializer
# import codecs
# import csv
# # import re
# # import xlrd
# from django.core.files.base import ContentFile
# from django.core.files.storage import FileSystemStorage

# from rest_framework import serializers, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import employees
# from django import forms
# from django.db import IntegrityError
# # class employeesViewset(viewsets.ModelViewSet):
# #     queryset = models.employees.objects.all()
# #     serializer_class = serializers.employeesSerializer

# fs = FileSystemStorage(location='tmp/')


# # Serializer
# class employeesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = employees
#         fields = "__all__"

   


# # Viewset

# # class employeesViewSets(viewsets.ModelViewSet):
# #     queryset = employees.objects.all()
# #     serializer_class = employeesSerializer
# #     @action(detail=False, methods=['POST'])
# #     # file = forms.FileField()
# class UploadFileForm(forms.Form):
#     file = forms.FileField()

# class employeesViewSet(viewsets.ModelViewSet):
#     queryset = employees.objects.all()
#     serializer_class = employeesSerializer
#     @action(detail=False, methods=['POST'])
#     def upload_data(self, request):
#         """Upload data from CSV"""
#         file = request.FILES["file"]

#         content = file.read()  # these are bytes
#         file_content = ContentFile(content)
#         file_name = fs.save(
#             "_tmp.csv", file_content
#         )
#         tmp_file = fs.path(file_name)

#         csv_file = open(tmp_file, errors="ignore")
#         reader = csv.reader(csv_file)
#         next(reader)

#         employees_list = []
#         for _id,row in enumerate(reader):
#             (
#                 name,
#                 phone,
#                 email,
#                 college,
#                 degree,
#                 skills,
#                 designation,
#                 company,
#                 file_location,
#                 text_file_location,
#             ) = row
#             employees_list.append(
#                 employees(
#                     # name=name,
#                     # phone=phone,
#                     # email=email,
#                     # college=college,
#                     # degree=degree,
#                     # skills=skills,
#                     # designation=designation,
#                     # company=company,
#                     # file_location=file_location,                  
#                     # text_file_location=text_file_location,
#                 )
#             )
#             # defaults = {'name':name,'phone':phone,'email':email,
#             #         'college':college,
#             #         'degree':degree,
#             #         'skills':skills,
#             #         'designation':designation,
#             #         'company':company,
#             #         'file_location':file_location,        
#             #         'text_file_location':text_file_location}
#             # try:
#             #     obj = employees.objects.get(name='name', email='email')
#             #     for key, value in defaults.items():
#             #         setattr(obj, key, value)
#             #     obj.save()
#             # except employees.DoesNotExist:
#             #     new_values = {'name': name, 'Email': Email}
#             #     new_values.update(defaults)
#             #     obj = employees(**new_values)
#             #     obj.save() 

#             defaults = {'name' : row[0], 'phone' : row[1],
#                         'email' : row[2], 'college' : row[3], 'degree' : row[4],
#                         'skills' : row[5], 'designation' : row[6], 
#                         'company' : row[7], 'file_location' : row[8]
#                         , 'text_file_location' : row[9]}
#             try:
#                 obj = employees.objects.get(name='name', email='email')
#                 for key, value in defaults.items():
#                     setattr(obj, key, value)
#                 obj.save()
#             except employees.DoesNotExist:
#                 new_values = {'name': 'name', 'email': 'email'}
#                 new_values.update(defaults)
#                 obj = employees(**new_values)
#                 obj.save()

#         # employees.objects.bulk_create(employees_list)

#         return Response("Successfully uploaded the data")

#     @action(detail=False, methods=['POST'])
#     def upload_data_with_validation(self, request):
#         """Upload data from CSV, with validation."""
#         file = request.FILES.get("file")

#         reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
#         data = list(reader)

#         serializer = self.serializer_class(data=data, many=True)
#         serializer.is_valid(raise_exception=True)

#         employees_list = []
#         for row in serializer.data:
#             employees_list.append(
#                 employees(
#                     name=row["name"],                   
#                     phone=row["phone"],
#                     email=row["email"],
#                     college=row["college"],
#                     degree=row["degree"],
#                     skills=row["skills"],
#                     designation=row["designation"],
#                     company=row["company"],
#                     file_location=row["file_location"],
#                     text_file_location=row["text_file_location"],
#                 )
#             )
#             # defaults = {'name':name,'phone':phone,'email':email,
#             #         'college':college,
#             #         'degree':degree,
#             #         'skills':skills,
#             #         'designation':designation,
#             #         'company':company,
#             #         'file_location':file_location,        
#             #         'text_file_location':text_file_location}
#             # try:
#             #     obj = employees.objects.get(name='name', email='email')
#             #     for key, value in defaults.items():
#             #         setattr(obj, key, value)
#             #     obj.save()
#             # except employees.DoesNotExist:
#             #     new_values = {'name': name, 'Email': Email}
#             #     new_values.update(defaults)
#             #     obj = employees(**new_values)
#             #     obj.save() 

#             defaults = {'name' : row[0], 'phone' : row[1],
#                         'email' : row[2], 'college' : row[3], 'degree' : row[4],
#                         'skills' : row[5], 'designation' : row[6], 
#                         'company' : row[7], 'file_location' : row[8]
#                         , 'text_file_location' : row[9]}
#             try:
#                 obj = employees.objects.get(name='name', email='email')
#                 for key, value in defaults.items():
#                     setattr(obj, key, value)
#                 obj.save()
#             except employees.DoesNotExist:
#                 new_values = {'name': 'name', 'email': 'email'}
#                 new_values.update(defaults)
#                 obj = employees(**new_values)
#                 obj.save()

#         # employees.objects.bulk_create(employees_list)

#         return Response("Successfully uploaded the data !!!")

# ======================================================================
    
#     @action(detail=False, methods=['POST','PUT'])
#     def file_upload(self,request):
#         if request.method == "POST":
#             form = UploadFileForm(request.POST, request.FILES)
#             count = 0
#             if form.is_valid():
#                 file = request.FILES["file"]
#                 content = file.read()  # these are bytes
#                 file_content = ContentFile(content)
#                 file_name = fs.save(
#                     "_tmp.csv", file_content
#                 )
#                 tmp_file = fs.path(file_name)
#                 csv_file = open(tmp_file, errors="ignore")
#                 reader = csv.reader(csv_file)
#                 for row in reader:
#                     count += 1

#                     try:
#                         _, p = employees.objects.update_or_create(id = count, defaults = 
#                         {'name' : row[0], 'phone' : row[1],
#                         'email' : row[2], 'college' : row[3], 'degree' : row[4],
#                         'skills' : row[5], 'designation' : row[6], 
#                         'company' : row[7], 'file_location' : row[8]
#                         , 'text_file_location' : row[9]})


#                     except IntegrityError:
#                         return render(request, 'webapp/duplicate_error.html', {'row': row})

#                 return redirect('webapp:index')
#         form = UploadFileForm()
#         return render(
#         request, "webapp/file_upload.html", {"form": form}
#         )


# =====================================================


# # class UploadViewSet(ViewSet):
# #     serializer_class = UploadSerializer

# #     def list(self, request):
# #         return Response("GET API")

# #     def create(self, request):
# #         file_uploaded = request.FILES.get('file_uploaded')
# #         content_type = file_uploaded.content_type
# #         response = "POST API and you have uploaded a {} file".format(content_type)
# #         return Response(response)