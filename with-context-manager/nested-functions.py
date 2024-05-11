def whisper(text):
    return text.lower() + '...'

def speak(text):
    result = whisper(text)
    return result

# Assigning 'whisper' function as an attribute to 'speak' function
speak.whisper = whisper

# Test the speak function
result = speak("Hello")
print(result)  # Output: "hello..."

# Accessing the 'whisper' attribute
print(speak.whisper("HELLO"))  # Output: "hello..."
