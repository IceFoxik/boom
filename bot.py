from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent
import time

# --- Настройки ---
PHONE_NUMBER = '+7...'  # заменить на нужный номер

# --- Генерация случайного User-Agent ---
ua = UserAgent()
user_agent = ua.random

# --- Настройки браузера ---
options = webdriver.ChromeOptions()

# 🔒 Анонимность
options.add_argument('--incognito')  # режим инкогнито
options.add_argument('--headless')   # без GUI
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-bluetooth')
options.add_argument('--disable-geolocation')
options.add_argument('--disable-media-stream')
options.add_argument('--disable-webgl')
options.add_argument('--disable-javascript')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-features=NetworkService,NetworkServiceWorker')

# 🧴 Маскируемся как обычный пользователь
options.add_argument(f'user-agent={user_agent}')

# --- Запуск браузера ---
driver = webdriver.Chrome(options=options)

try:
    print("🌐 Открытие сайта...")
    driver.get('https://sunlight.net/profile/login/')
    print("📍 Текущий URL:", driver.current_url)

    # Ожидание поля ввода телефона
    phone_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="+7 "]'))
    )
    phone_input.click()
    phone_input.clear()
    phone_input.send_keys(PHONE_NUMBER)
    print("📞 Телефон введён")

    # Ожидание кнопки "Получить код"
    send_code_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Получить код"]]'))
    )
    send_code_button.click()
    print("✅ Кнопка 'Получить код' успешно нажата")

    # Пауза для завершения запроса
    time.sleep(3)

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    driver.quit()
    print("🔚 Браузер закрыт")