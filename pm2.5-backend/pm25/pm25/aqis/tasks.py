import requests

from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="pull_aqis_data",
    ignore_result=True
)
def pull_aqis_data():
    try:
        data = requests.get('http://api.waqi.info/feed/bangkok/?token=a7957760bf3219023ed022371da201db5ba36c26')
        print(data)
        print(data.json())

        # for event in events:
        # event_broker = EventBroker.objects.get(name=event['broker'])
        # event_category = EventCategory.objects.get(name=category)

        # Event.objects.update_or_create(
        #     title=event['title'],
        #     defaults={
        #         'title': event['title'],
        #         'datetime': event['datetime'],
        #         'url': event['url'],
        #         'broker': event_broker,
        #         'category': event_category,
        #     }
        # )

        result_text = 'Updated events!'
    except Exception as e:
        result_text = f'Update Error! {e}'

    return result_text
