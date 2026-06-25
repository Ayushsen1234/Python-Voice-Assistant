import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

# Speak Function
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

# Listen Function
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        print("Sorry, I could not understand.")
        return ""

# Main Program
if __name__ == "__main__":
    speak("Hey Sir, how may I help you")

    command = take_command()

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "search" in command:
        search_query = command.replace("search", "")
        speak(f"Searching {search_query}")
        webbrowser.open(
            f"https://www.google.com/search?q={search_query}"
        )

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )

    elif "hello" in command:
        speak("Hello Sir")

    else:
        speak("Sorry, I don't understand that command")
