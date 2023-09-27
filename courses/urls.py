from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from courses.views import (CoursViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView,
                           LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView)

app_name = CoursesConfig.name


router = DefaultRouter()
router.register(r'courses', CoursViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
] + router.urls
