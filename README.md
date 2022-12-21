Итоговый проект по автоматизации тестирования. Объект тестирования:https://b2c.passport.rt.ru/ 
Тест-кейсы и описания багов: https://docs.google.com/spreadsheets/d/1CMT3uV5KZXGOpi81A6Wufj5YlkKeSblokf6JqhYlZ08/edit?usp=sharing 

По заданию:

   1. Протестировать требования;
   2. Разработать тест-кейсы (не менее 15);
   3. Провести автоматизированное тестирование продукта (не менее 15 автотестов);
   4. Оформить описание обнаруженных багов.


Для работы автотестов необходимы библиотеки Pytest и Selenium и webdriver Selenium для Chrome 108 версии 
Запустить тесты можно через терминал прописав:
 python3 -m pytest -v --driver Chrome --driver-path chromedriver.exe test_registration_website.py
 python3 -m pytest -v --driver Chrome --driver-path chromedriver.exe test_authorization_website.py

или через Run в PyCharm
