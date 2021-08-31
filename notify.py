from pyasn1.type.univ import Null
from gmail_api import get_message_by_id
from plyer import notification
from gmail_api import get_message_by_id
from time import sleep


def remove_email_from_sender(sender):
    return sender.split('<')[0][:-1]


def create_body(messages, amount):
    body = "You have {} unread messages.\n".format(amount)
    for msg in messages:
        content = get_message_by_id(msg['id'])
        body += f"{remove_email_from_sender(content['from'])}\n"
    return body


def create_notification(messages, amount):
    title = 'My Gmail Notifier'
    body = create_body(messages, amount)
    notification.notify(title=title, message=body)
