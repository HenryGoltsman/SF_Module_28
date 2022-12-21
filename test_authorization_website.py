import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import correct_email, correct_password, correct_phone, incorrect_password_4, incorrect_password


@pytest.fixture(autouse=True)
def testing():
    # инициализация драйвера
    selenium = webdriver.Chrome()
    selenium.implicitly_wait(10)
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    yield selenium
    selenium.quit()


# ТК-13
# проверка, что пользователь может перейти на страницу авторизации
def test_authorization_13(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Авторизация', print('Тест провален')
    assert selenium.find_element(By.ID, 'kc-login'), print('Тест провален')


# ТК-14
# проверка, что пользователь может открыть чат поддержки на странице авторизации
def test_authorization_14(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на виджет "Поддержка"
    selenium.find_element(By.ID, 'widget_bar').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'widget_sendPre-chat'), print('Тест провален')

# ТК-15
# проверка, что на странице авторизации есть продуктовый слоган
def test_authorization_15(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома', \
        print('Тест провален')


# ТК-16
# проверка, что таб выбора авторизации по номеру
def test_authorization_16(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-phone').text == 'Телефон', print('Тест провален')


# ТК-17
# проверка, что таб выбора авторизации по логину
def test_authorization_17(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Логин"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-login').text == 'Логин', print('Тест провален')

# ТК-18
# проверка, что таб выбора авторизации по почте
def test_authorization_18(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-mail').text == 'Почта', print('Тест провален')

# ТК-19
# проверка, что таб выбора авторизации по лицевому счету
def test_authorization_19(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Лицевой счёт"
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт', print('Тест провален')


# ТК-20
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (электронная почта и пароль)
def test_authorization_20(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректного e-mail
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')


# ТК-21
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (мобильный телефон и пароль)
def test_authorization_21(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')


# ТК-22
# проверка, что введён верный номер телефона, но неверный пароль
def test_authorization_22(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password_4)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Тест провален')


# ТК-23
# проверка, что введена верная электронная почта, но неверный пароль
def test_authorization_23(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Тест провален')


# ТК-24
# проверка, что пользователь может перейти на страницу "Восстановление пароля"
def test_authorization_24(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на кнопку "Забыл пароль"
    selenium.find_element(By.ID, 'forgot_password').click()

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Введите данные и нажмите «Продолжить»', \
        print('Тест провален')

# ТК-25
# проверка, что пользователь может авторизоваться через ВК
def test_authorization_25(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на иконку ВК
    selenium.find_element(By.ID, 'oidc_vk').click()
    time.sleep(1)

    assert selenium.find_element(By.ID, 'oauth_head_info').text == 'Регистрация', \
        print('Тест провален')

# ТК-26
# проверка, что пользователь может авторизоваться через ОК
def test_authorization_26(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на иконку OK
    selenium.find_element(By.ID, 'oidc_ok').click()
    time.sleep(1)


# ТК-27
# проверка, что пользователь может авторизоваться через mail.ru
def test_authorization_27(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на иконку mail.ru
    selenium.find_element(By.ID, 'oidc_mail').click()
    time.sleep(1)



# ТК-28
# проверка, что пользователь может авторизоваться через google
def test_authorization_28(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на иконку google
    selenium.find_element(By.ID, 'oidc_google').click()
    time.sleep(1)



# ТК-29
# проверка, что пользователь может авторизоваться через Yandex
def test_authorization_29(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на иконку Yandex
    selenium.find_element(By.ID, 'oidc_ya').click()
    time.sleep(1)
