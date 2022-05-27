import time
import requests
import datetime as dt
import schedule

URL_BITRIX24 = 'https://xxxxxxxxx.bitrix24.com/rest/1/xxxxxxx/tasks.task.add'

def make_task_for_holyday():
    """Функция для внесения задачи в Битрикс24 за 3 дня до праздников.
    Необходимо поставить корректное значение в константе URL_BITRIX24"""
    current_date = dt.date.today()
    time_delta = dt.timedelta(days=3)
    three_days_before = current_date - time_delta
    response_isadayoff = requests.get('https://isdayoff.ru/today')

    if response_isadayoff.text == 1:
        fields = {"fields": {"TITLE": "Напоминание о праздничном дне",
                             "DESCRIPTION": "Через 3 дня праздник!",
                             "DEADLINE": three_days_before}
                  }

        post_for_b24 = requests.post(URL_BITRIX24, json=fields)
        return post_for_b24

    schedule.every().day.at("8:30").do(make_task_for_holyday)

    while 1:
        schedule.run_pending()
        time.sleep(1)




