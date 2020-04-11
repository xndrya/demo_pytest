# -*- coding: utf-8 -*-
import allure
from fixture.session import *


def test_check_letter_sent(app):
    with allure.step('Открыта начальная страница'):
        open_home_page(app)
    with allure.step('Логин'):
        login(app, "t3estov@gmail.com", "1Password-")
    with allure.step('Получение количества отправленных писем до начала теста'):
        sent_letters_count = check_sent_letters_count(app)
    with allure.step('Отправка письма'):
        send_letter(app, "t3estov@gmail.com", random_string("Testing", 20), random_string("Message", 120))
    with allure.step('Получение количества отправленных писем после отправки письма'):
        sent_letters_count_new = check_sent_letters_count(app)
    with allure.step('Проверка что количество отправленных писем увеличилось на единицу'):
        assert sent_letters_count + 1 == sent_letters_count_new
