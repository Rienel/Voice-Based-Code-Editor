import speech_recognition as sr

recognizer = sr.Recognizer()

# Listen for inputs = into string
def record():
    while(1):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.3)
                print("ALL I WANTED WAS -:")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error:", e)

    return

# To text
def output(text):
    f = open("text.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record()
    output(text)