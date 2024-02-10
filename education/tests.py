from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User
from education.models import Course, Lesson, Subscription


class LessonTestCase(APITestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(
            name='test1',
            description='test1'
        )

    def test_get_list_lesson(self):
        response = self.client.get('education:lesson-list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_lesson(self):
        data = {
            'name': 'test2',
            'description': 'test2'
            }
        response = self.client.post('education:lesson-create', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_lesson(self):
        data = {
            'name': 'test3',
            'description': 'test2'
        }
        response = self.client.put('education:lesson-update', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        response = self.client.delete('education:lesson-delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='test12',
            description='test12',

        )

        self.user = User.objects.create(
            email='admin@sky.pro',
            first_name='Dmitriy',
            last_name='Alushkin',
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('12345')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.subscription = Subscription.objects.create(
            user=self.user,
            is_subscribed=True,
            course=self.course
        )

    def test_create_subscription(self):
        data = {
            'user': self.user.pk,
            'is_subscribed': True,
            'course': self.course.pk
        }

        response = self.client.post('education:subscription', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_list(self):
        response = self.client.get('education:subscription')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'user': self.user.pk,
            'is_subscribed': True,
            'course': self.course.pk
        }
        response = self.client.put('education:subscription', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subscription(self):
        response = self.client.delete('education:subscription')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)