from rest_framework import serializers

from courses.models import Cours, Lesson, Payment
from courses.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class CoursSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Cours
        fields = ['id', 'title', 'preview', 'description', 'lessons_count', 'lessons', 'owner']

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
