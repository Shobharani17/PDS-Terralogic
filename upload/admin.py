from django.contrib import admin
from .models import employees, Upload_files
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(employees)
class userDat(ImportExportModelAdmin):
    pass


admin.site.register(Upload_files)