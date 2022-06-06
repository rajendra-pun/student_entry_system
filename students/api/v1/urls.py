from django.urls import path, include

from rest_framework.routers import DefaultRouter

from students.api.v1.viewsets import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]