from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from courses.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.ru',
            role='user',
            password='1234',
            is_staff=False,
            is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            title='Test',
            description='Test description',
            owner=self.user
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            'title': 'Test',
            'description': 'Test description',
            'link': 'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa'
        }

        response = self.client.post(
            reverse('courses:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_lessons_list(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('courses:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "title": "Test",
                        "preview": None,
                        "description": "Test description",
                        "link": None,
                        "cours": None,
                        "owner": self.user.id
                    }]}
        )

    def test_view_lesson(self):
        """Тестирование вывода урока"""

        response = self.client.get(
            '/lesson/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": "Test",
                "preview": None,
                "description": "Test description",
                "link": None,
                "cours": None,
                "owner": self.user.id
            }
        )

    def test_update_lesson(self):
        """Тестирование изменения урока"""

        data = {
            'title': 'Test update',
            'description': 'Test new description',
            'link': 'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa'
        }

        response = self.client.put(
            '/lesson/update/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": "Test update",
                "preview": None,
                "description": "Test new description",
                "link": 'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa',
                "cours": None,
                "owner": self.user.id
            }
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        response = self.client.delete(
            '/lesson/delete/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.count(),
            0
        )

