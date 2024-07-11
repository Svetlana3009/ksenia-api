Задача по UI покрытию:

Сайт (стартовая страница): https://finance.rambler.ru/calculators/converter/
Необходимо реализовать автоматическое получение сконвертированного курса, используя фраемворк playwright/selenium.
 Конвертация должна происходить с параметрами EUR AUD, 10 единиц.
 Результат – значение сконвертированного курса

 *Повышенная сложность
 Реализовать возможность гибко задавать параметры валют и единиц.
Для решения этой задачи можно использовать библиотеку Playwright для автоматизации взаимодействия с веб-страницей. Вот пример кода, который выполняет конвертацию валюты и получает результат:


from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Переходим на стартовую страницу
        await page.goto("https://finance.rambler.ru/calculators/converter/")

        # Выбираем исходную валюту
        await page.click('input[value="EUR"]')

        # Вводим количество единиц
        await page.fill('input[name="amount"]', '10')

        # Выбираем целевую валюту
        await page.click('input[value="AUD"]')

        # Получаем результат конвертации
        result = await page.innerText('span.result')

        print(f"Результат конвертации: {result}")

        # Закрываем браузер
        await browser.close()

asyncio.run(main())
В этом коде мы создаем новый контекст браузера Chromium, переходим на стартовую страницу, выбираем исходную и целевую валюты, вводим количество единиц и получаем результат конвертации.

Для повышения сложности задачи, можно добавить возможность гибкого задания параметров валют и единиц. Например, создать функцию, которая принимает список пар валют и количество единиц для каждой пары, и выполняет конвертацию для всех пар:


async def convert_currencies(pairs, units):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        for pair, unit in zip(pairs, units):
            # Переходим на стартовую страницу
            await page.goto("https://finance.rambler.ru/calculators/converter/")

            # Выбираем исходную валюту
            await page.click(f'input[value="{pair[0]}"]')

            # Вводим количество единиц
            await page.fill(f'input[name="amount"]', str(unit))

            # Выбираем целевую валюту
            await page.click(f'input[value="{pair[1]}"]')

            # Получаем и печатаем результат конвертации
            result = await page.innerText('span.result')
            print(f"Результат конвертации {pair[0]} -> {pair[1]}: {result}")

        # Закрываем браузер
        await browser.close()

# Пример использования функции
convert_currencies([["EUR", "AUD"], ["USD", "RUB"]], [10, 100])
Этот код позволяет выполнять конвертацию для нескольких пар валют с разными количествами единиц.
Сроки выполнения
Ожидаемые сроки: 2 дня
Отправка на проверку
После написания сервиса, нужно загрузить его в гитхаб в публичный репо и скинуть ссылку на почту:  andrew@vortex.foundation
