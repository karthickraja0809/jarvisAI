import speech_recognition_api as sr


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return "-"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')

    except Exception as e:
        print("Error:", e)
        return "-"

    return query


# Example usage:
command = take_command()
print("You said:", command)

