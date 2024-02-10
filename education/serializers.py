from rest_framework import serializers
from education.models import Course, Lesson, Subscription
from education.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LinkValidator(field='link_to_the_video'),
        ]


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    subscribe = SubscriptionSerializer(source='subscribe_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    def get_subscribe(self, obj):
        return obj.subscribe_set.all()

    class Meta:
        model = Course
        fields = '__all__'








