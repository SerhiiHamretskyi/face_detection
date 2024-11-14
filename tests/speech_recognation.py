import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()


def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                # Prompt user for input
                print("Please say something...")

                # Prepare recognizer for input
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

                # Recognize speech using Google
                MyText = r.recognize_google(audio)
                print("You said:", MyText)  # Optional feedback
                return MyText

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            engine.say("Sorry, I did not understand that.")
            engine.runAndWait()


def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    print("Wrote text to file")
    engine.say("Text saved successfully.")
    engine.runAndWait()


while True:
    text = record_text()
    output_text(text)

    # Optional exit condition for the loop
    if text.lower() == "exit":
        print("Exiting...")
        engine.say("Exiting the program.")
        engine.runAndWait()
        break
