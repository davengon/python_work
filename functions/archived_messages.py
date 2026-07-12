def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    
    return sent_messages

text_messages = ["Hi", "my name is David", "nice meeting you!"]
show_messages(text_messages)
print(send_messages(text_messages[:])) #The : uses a copy of the list thus the original is not affected by the function and its original content remain the same
print(text_messages)