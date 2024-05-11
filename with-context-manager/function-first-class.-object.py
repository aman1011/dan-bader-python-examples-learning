def yell(text):
    return text.upper() + '!'

def greeting(func, text):
    greeting = func(text)
    print(greeting)


greeting(yell, 'I am learning python')
