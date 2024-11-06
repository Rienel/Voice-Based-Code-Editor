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



# TODO stop the if's
# To use commands
def process(text):
    if text == "exit":
        print("Exiting...")
        return "exit"

    commands = {
        "function": "def f_name():", 
        "add comment": "# ",
        "print": "print('')",
        "exit": "exit"
    }

    # slicing to skip, should have a better way (diko ganahan mang hugas plato)
    if text == "print":
        skip = text[6:]
        output(f"print('{skip}')")
    elif text == "function":
        output("deft, real name Kim Hyuk-kyu, is a South Korean professional League of Legends player for KT Rolster. He won the 2015 Mid-Season Invitational with Edward Gaming and the 2022 League of Legends World Championship with DRX.")
    elif text in commands:
        output(commands[text])
    else:
        output(text)

# MAIN
while(1):
    text = record()
    if text == "exit":
        break
    process(text)