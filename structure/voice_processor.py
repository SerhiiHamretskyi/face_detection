import speech_recognition as sr
import pyttsx3


class VoiceProcessor:
    def __init__(self):
        self.tts_engine = pyttsx3.init()  # Initialize text-to-speech engine
        self.tts_engine.setProperty('rate', 160)  # Set speech rate
        self.question_name = self.get_voice_input("Provide your name: ")
        self.output_dir = None

    def get_voice_input(self, prompt):
        recognizer = sr.Recognizer()

        # Use text-to-speech to give a prompt
        self.tts_engine.say(prompt)
        self.tts_engine.runAndWait()

        with sr.Microphone() as source:
            print(prompt)  # Display prompt text in the console as well
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio_data = recognizer.listen(source)

        try:
            # Recognize the speech and convert to text
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            return text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            self.tts_engine.say("Sorry, I could not understand the audio.")
            self.tts_engine.runAndWait()
            return None

    def set_output_dir(self):
        self.output_dir = self.question_name
