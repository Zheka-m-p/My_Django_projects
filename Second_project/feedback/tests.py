from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class FeedbackRedirectTests(TestCase):
    def setUp(self):
        # 1. Создаем тестового пользователя для проверки логина
        self.user = User.objects.create_user(username='testuser', password='password123')

        # 2. Правильные пути согласно твоим urls.py
        self.feedback_url = reverse('feedback:home')  # это твой path('', views.index, name='home')
        self.login_url = reverse('users:login_user')  # это твой login_user
        self.register_url = reverse('users:register_user')  # это твой register_user

    def test_need_login_page_shows_correct_next_links(self):
        """Проверяем, что неавторизованный юзер видит кнопки с правильным ?next=/feedback/"""
        response = self.client.get(self.feedback_url)

        # Проверяем, что ссылка на логин содержит путь возврата
        expected_login_link = f'href="{self.login_url}?next={self.feedback_url}"'
        self.assertContains(response, expected_login_link)

        # Проверяем, что ссылка на регистрацию тоже содержит путь возврата
        expected_register_link = f'href="{self.register_url}?next={self.feedback_url}"'
        self.assertContains(response, expected_register_link)

    def test_login_redirects_back_to_feedback_home(self):
        """Проверяем, что после ввода пароля юзера кидает обратно на форму отзыва"""
        # Имитируем переход на логин с параметром next
        # и последующую отправку формы (POST)
        response = self.client.post(
            self.login_url,
            {
                'username': 'testuser',
                'password': 'password123',
                'next': self.feedback_url  # Это имитирует скрытое поле <input type="hidden">
            },
            follow=True
        )

        # Проверяем, что в итоге мы оказались на странице /feedback/
        # (или там, где у тебя feedback:home)
        self.assertRedirects(response, self.feedback_url)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_registration_url_carries_next_param(self):
        """Проверяем, что если юзер ушел на регистрацию, параметр next не потерялся в ссылке"""
        response = self.client.get(f"{self.register_url}?next={self.feedback_url}")

        # Проверяем, есть ли на странице регистрации ссылка на вход с тем же next
        # (чтобы юзер мог передумать и все равно вернуться)
        login_with_next = f'href="{self.login_url}?next={self.feedback_url}"'
        self.assertContains(response, login_with_next)
