from celery import shared_task

@shared_task
def print_msg():
    print("Hello")
