from rest_framework import serializers

from courses.models import Cours, Lesson, Payment, Subscription
from courses.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['cours']


class CoursSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    sub_users = serializers.SerializerMethodField()

    class Meta:
        model = Cours
        fields = ['id', 'title', 'preview', 'description', 'lessons_count', 'lessons', 'owner', 'sub_users']

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    def get_sub_users(self, obj):
        sublist = []
        for sub in obj.subscription_set.all():
            sublist.append(sub.owner.email)
        return sublist

