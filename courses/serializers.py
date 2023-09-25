from rest_framework import serializers

from courses.models import Cours, Lesson


class CoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cours
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
