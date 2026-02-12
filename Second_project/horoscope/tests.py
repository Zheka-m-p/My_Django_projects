from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestHoroscope(TestCase):
    # каждая функция внутри тестирует представление
    # self.client = браузер(по сути)
    def test_main_page_works(self):
        response = self.client.get(reverse('horoscope:home_horoscope'))  # ✅
        # response = self.client.get('/horoscope/') # или так можно, но лучше по именам, а не по пути
        # Проверяем: передаем два значения и сравниваем их: статус 200 (всё ок)
        self.assertEqual(response.status_code, 200)
        # аналогично проверяем используется ли правильный шаблон
        self.assertTemplateUsed(response, 'horoscope/index_horoscope.html')

    def test_aries_page_works(self):
        response = self.client.get(reverse('horoscope:sign_zodiac', args=['aries']))

        # Проверяем: статус 200
        self.assertEqual(response.status_code, 200)
        # Проверяем: на странице есть слово "Овен"
        self.assertContains(response, 'Овен')

    def test_invalid_sign_shows_error(self):
        response = self.client.get(reverse('horoscope:sign_zodiac', args=['mars']))
        self.assertEqual(response.status_code, 404)

    # еще тесты мб, но потом...
