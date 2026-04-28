messages = ['Oi', 'Tudo bem?', 'Tudo']

def show_messages(messages):
    for message in messages: print(message)

show_messages(messages)

def send_messages(messages):
    sent_messages = []
    for message in messages:
        sent_messages.append(message)
    return sent_messages

sent_messages = send_messages(messages)
show_messages(messages)
show_messages(sent_messages)