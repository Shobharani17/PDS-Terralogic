from upload.views import employeesViewSet
from rest_framework import routers
# from webapp.views import UploadViewSet

router = routers.DefaultRouter()
router.register('jsondata',employeesViewSet)