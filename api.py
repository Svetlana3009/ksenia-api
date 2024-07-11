# Задача по API покрытию:

# Открытое API: https://reqres.in/
#  Необходимо составить позитивные сценарии для тестирования методов:
#  1) GET : SINGLE USER
#  2) POST : CREATE
#  3) PUT : UPDATE
# Автоматизировать данные тестовые сценарии используя фраемворк pytest.
#  С помощью библиотеки allure описать шаги тестирования. Написать assert проверки на статус код и тело ожидаемого ответа.
# Вот примерный код, который может быть использован для тестирования методов API:

import requests
import pytest
from allure_commons_test.report import AllureTestCase

class TestAPICoverage(AllureTestCase):
    @pytest.mark.parametrize("method,url,data", [
        ("GET", "/api/users/2", None),
        ("POST", "/api/users", {"name": "John Doe", "job": "Software Engineer"}),
        ("PUT", "/api/users/2", {"name": "Jane Doe", "job": "UI Designer"})
    ])
    def test_api_coverage(self, method, url, data):
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        else:
            response = requests.put(url, json=data)

        # Проверка статуса кода
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

        # Проверка тела ответа
        expected_body = {"name": "Jane Doe", "job": "UI Designer"}
        actual_body = response.json()
        assert actual_body == expected_body, f"Expected body {expected_body} but got {actual_body}"
