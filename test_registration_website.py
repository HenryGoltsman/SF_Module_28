import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import correct_name, correct_surname, correct_email, correct_password, correct_code, incorrect_name, \
    incorrect_surname, incorrect_email, incorrect_password, incorrect_code, incorrect_name_2, incorrect_surname_2, \
    incorrect_email_2, incorrect_password_2, incorrect_name_3, incorrect_surname_3, incorrect_email_3, \
    incorrect_password_3, incorrect_password_4, correct_phone


@pytest.fixture(autouse=True)
def testing():
    # инициализация драйвера
    selenium = webdriver.Chrome()
    selenium.implicitly_wait(10)
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    yield selenium
    selenium.quit()


# ТК-1
# проверка, что пользователь может перейти на страницу регистрации
def test_registration_1(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Регистрация', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Личные данные', print('Тест провален')
    assert selenium.find_element(By.XPATH, '//button[@type="submit"]'), print('Тест провален')


# ТК-2
# Проверка, что пользователь может изучить "пользовательское соглашение"
def test_registration_2(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на ссылку "пользовательское соглашение"
    selenium.find_element(By.LINK_TEXT, 'пользовательского соглашения').click()
    time.sleep(10)

    assert selenium.find_element(By.LINK_TEXT, 'пользовательского соглашения'), print('Тест провален')


# ТК-3
# проверка, что пользователь может открыть чат поддержки, перейдя на страницу регистрации
def test_registration_3(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'widget_bar')))

    # запустить чат поддержки
    selenium.find_element(By.ID, 'widget_bar').click()
    time.sleep(2)

    assert selenium.find_element(By.ID, 'widget_sendPre-chat'), print('Тест провален')


# ТК-4
# проверка регистрации на сайте с корректными данными
def test_registration_4(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # ввод данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(correct_name)
    # ввод данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(correct_surname)
    # Ввод данных в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'address').send_keys(correct_email)
    # ввод данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(correct_password)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    # ввод кода, который будет получен по электронной почте
    selenium.find_element(By.ID, 'rt-code-0').send_keys(correct_code)

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Подтверждение email', print('Тест провален')


# TK-5
# проверка регистрации пользователя с некорректным вводом всех полей в виде цифр
def test_registration_5(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # ввод некорректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(incorrect_name)
    # ввод некорректных данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(incorrect_surname)
    # ввод некорректных данных в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'address').send_keys(incorrect_email)
    # ввод некорректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(incorrect_password)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)


# ТК-6
# проверка регистрации пользователя с некорректным вводом некоторых полей
def test_registration_6(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # ввод корректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(correct_name)
    # ввод корректных данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(correct_surname)
    # Ввод некорректных данных в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'address').send_keys(incorrect_email)
    # ввод некорректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(incorrect_password)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)

    # ТК-7
    # проверка регистрации пользователя с некорректным вводом всех полей (только спецсимволы)
    def test_registration_7(testing):
        selenium = testing
        # открытие сайта
        selenium.get('https://b2c.passport.rt.ru')

        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

        # нажимаем на кнопку "Зарегистрироваться"
        selenium.find_element(By.ID, 'kc-register').click()
        # ввод некорректных данных в поле "Имя"
        selenium.find_element(By.NAME, 'firstName').send_keys(incorrect_name_2)
        # ввод некорректных данных в поле "Фамилия"
        selenium.find_element(By.NAME, 'lastName').send_keys(incorrect_surname_2)
        # ввод некорректных данных в поле "E-mail или мобильный телефон"
        selenium.find_element(By.ID, 'address').send_keys(incorrect_email_2)
        # ввод некорректных данных в поле "Пароль"
        selenium.find_element(By.ID, 'password').send_keys(incorrect_password_2)
        # ввод данных в поле "Подтверждение пароля"
        selenium.find_element(By.ID, 'password-confirm').send_keys(incorrect_password_2)
        # нажимаем на кнопку "Зарегистрироваться"
        selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)


# ТК-8
# проверка регистрации пользователя с некорректным вводом всех полей (русская и английская раскладка)
def test_registration_8(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # ввод некорректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(incorrect_name_3)
    # ввод некорректных данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(incorrect_surname_3)
    # ввод некорректных данных в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'address').send_keys(incorrect_email_3)
    # ввод некорректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password_3)
    # ввод некорректных данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(incorrect_password_3)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)


# ТК-9
# проверка регистрации пользователя с вводом неверного кода доступа
def test_registration_9(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')
    # ожидание 10 секунд для загрузки страницы

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    selenium.find_element(By.ID, 'kc-register').click()
    # ввод данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(correct_name)
    # ввод данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(correct_surname)
    # Ввод данных в поле "E-mail или мобильный телефон". В данном случае вводим мобильный телефон
    selenium.find_element(By.ID, 'address').send_keys(correct_phone)
    # ввод данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(correct_password)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    # ввод некорректного кода
    selenium.find_element(By.ID, 'rt-code-0').send_keys(incorrect_code)
    time.sleep(5)


# ТК-10
# проверка, что если пользователь ввёл в поле "Подтверждение пароля", отличный от пароля "Новый пароль, то под полем "Подтверждение" отображается "Пароли не совпадают"
def test_registration_10(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # ввод корректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(correct_name)
    # ввод корректных данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(correct_surname)
    # ввод корректных данных в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'address').send_keys(correct_email)
    # ввод корректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(incorrect_password_4)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)


# ТК-11
# проверка регистрации пользователя, который уже зарегистрирован
def test_registration_11(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')
    # ожидание 10 секунд для загрузки страницы

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))

    selenium.find_element(By.ID, 'kc-register').click()
    # ввод данных в поле "Имя"
    selenium.find_element(By.NAME, 'firstName').send_keys(correct_name)
    # ввод данных в поле "Фамилия"
    selenium.find_element(By.NAME, 'lastName').send_keys(correct_surname)
    # Ввод данных в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'address').send_keys(correct_email)
    # ввод данных в поле "Пароль"
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.ID, 'password-confirm').send_keys(correct_password)
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)


# ТК-12
# Проверка, что на странице регистрации есть продуктовый слоган
def test_registration_12(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')
    # ожидание 10 секунд для загрузки страницы
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.ID, 'kc-register').click()
    # поиск продуктового слогана
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома'
