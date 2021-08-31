from gmail_api import get_unread_messages
from notify import create_notification
from time import sleep
from plyer import notification

unread_messages = get_unread_messages()

while True:
    if unread_messages['resultSizeEstimate'] != 0:
        create_notification(unread_messages['messages'],
                            unread_messages['resultSizeEstimate'])
    else:
        notification.notify(title='My Gmail Notifier',
                            message='Você não possui novos emails.')
    sleep(3600)
