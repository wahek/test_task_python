import csv
import json
import logging
import datetime

SECURITY = ['аутентификация', 'Шифрование', 'Защита ', 'Безопасность', 'Конфиденциальность', 'данные ']
REFUNDS = ['Возврат', 'операции', 'Компенсация', 'Возмещение', 'Возвращение', 'деньги  ', 'денег  ', 'средства',
           'денежные', 'верните ']
TROUBLESHOOTING = ['Ремонт', 'Исправление', 'Диагностика', 'Техническое', 'обслуживание', 'Восстановление']
ACCOUNT = ['Регистрация', 'Авторизация', 'Логин', 'Пароль', 'Профиль', 'войти', 'выйти', 'зарегистрироваться', 'выход ',
           'вход  ']
ADVERTISING_AND_COLLABORATION = ['Реклама', 'Партнерство', 'Сотрудничество', 'Спонсорство', 'Маркетинг']
LIMITS = ['Ограничение', 'Лимит', 'Максимум', 'Минимум', 'Предел', 'кончается']
PAYMENTS = ['Оплата ', 'Транзакция', 'Перевод', 'Платеж', 'Валюта', 'деньги  ', 'средства', 'денежные', 'денег  ']
FEATURES = ['Возможность', 'Опции ', 'Сервисы', 'новое', 'функция', 'применение', 'применять']

logging.basicConfig(filename='log_unknown_categories.log', encoding='utf-8', level=logging.WARNING, filemode='w')

logger = logging.getLogger(__name__)


def to_json(filename):
    def deco(func):
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            with open(filename, 'w', encoding='utf-8') as data:
                json.dump(f, data, indent=4)
            return f

        return wrapper

    return deco


@to_json('get.json')
def sorted_categories(filename):
    result_json = {}
    with open(filename, 'r', encoding='utf-8') as data:
        reader = csv.reader(data)

        for string in reader:
            dict_res = dict(sec_count=0,
                            ref_count=0,
                            trb_count=0,
                            acc_count=0,
                            adv_count=0,
                            lim_count=0,
                            pay_count=0,
                            fat_count=0)
            for item in SECURITY:
                if item[:-2].lower() in string[0].lower():
                    dict_res['sec_count'] += 1
            for item in REFUNDS:
                if item[:-2].lower() in string[0].lower():
                    dict_res['ref_count'] += 1
            for item in TROUBLESHOOTING:
                if item[:-2].lower() in string[0].lower():
                    dict_res['trb_count'] += 1
            for item in ACCOUNT:
                if item[:-2].lower() in string[0].lower():
                    dict_res['acc_count'] += 1
            for item in ADVERTISING_AND_COLLABORATION:
                if item[:-2].lower() in string[0].lower():
                    dict_res['adv_count'] += 1
            for item in LIMITS:
                if item[:-2].lower() in string[0].lower():
                    dict_res['lim_count'] += 1
            for item in PAYMENTS:
                if item[:-2].lower() in string[0].lower():
                    dict_res['pay_count'] += 1
            for item in FEATURES:
                if item[:-2].lower() in string[0].lower():
                    dict_res['fat_count'] += 1
            sort_dict = sorted(dict_res.items(), key=lambda x: x[1], reverse=True)
            if sort_dict[0][1]:
                result_json[string[0]] = (sort_dict[0][0][:3],)
                if sort_dict[1][1]:
                    result_json[string[0]] = result_json[string[0]] + (sort_dict[1][0][:3],)
            else:
                result_json[string[0]] = (None,)
                logger.warning(f' | Запрос не попал ни в одну категорию: {string[0]}\n{datetime.datetime.now()}')

    return result_json


if __name__ == '__main__':
    print(sorted_categories('test_task_python/user_support_letters.csv'))
