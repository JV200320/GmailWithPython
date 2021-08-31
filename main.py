import quickstart

service = quickstart.service

unread_messages = service.users().messages().list(
    userId='me', labelIds='UNREAD').execute()
print("You have {} unread messages.".format(
    unread_messages['resultSizeEstimate']))
for message in unread_messages['messages']:
    content = service.users().messages().get(
        id=message['id'], userId='me', format='full').execute()
    message_info = content['payload']['headers']
    used_info = {}
    for obj in message_info:
        if obj['name'].lower() in ['from', 'subject', 'date']:
            used_info[obj['name'].lower()] = obj['value']
    print("{} talking about {} - {}".format(
        used_info['from'].split('<')[0][:-1], used_info['subject'], used_info['date'][:22]))
