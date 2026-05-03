import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import requests
import time

# ---------------- TEXT TO SPEECH ----------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- SPEECH INPUT ----------------
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print("You:", command)
        return command.lower()
    except Exception as e:
        print(e)
        speak("Please say that again")
        return ""

# ---------------- GREETING ----------------
def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# ---------------- TIME ----------------
def tell_time():
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time_now}")

# ---------------- DATE ----------------
def tell_date():
    date_now = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {date_now}")

# ---------------- WIKIPEDIA / KNOWLEDGE ----------------
def answer_question(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("I couldn't find an answer.")

# ---------------- WEATHER ----------------
def get_weather(city):
    api_key = "YOUR_API_KEY"   # 🔴 Put your API key here
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")
    except:
        speak("Unable to fetch weather details")

# ---------------- EMAIL ----------------
def send_email():
    try:
        speak("What should I say?")
        content = take_command()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"

        server.login(sender_email, sender_password)

        receiver_email = "receiver@gmail.com"
        server.sendmail(sender_email, receiver_email, content)

        server.close()
        speak("Email sent successfully")
    except:
        speak("Failed to send email")

# ---------------- REMINDER ----------------
def set_reminder():
    speak("After how many seconds?")
    seconds = take_command()

    try:
        seconds = int(seconds)
        speak("What should I remind you?")
        message = take_command()

        speak(f"Reminder set for {seconds} seconds")
        time.sleep(seconds)

        speak(f"Reminder: {message}")
    except:
        speak("Sorry, I could not set reminder")

# ---------------- CUSTOM COMMANDS ----------------
def custom_commands(command):
    if "your name" in command:
        speak("I am your personal voice assistant")

    elif "who made you" in command:
        speak("I was created using Python")

# ---------------- MAIN ----------------
def run_assistant():
    greet()
    speak("How can I help you?")

    while True:
        command = take_command()
        custom_commands(command)

        if any(word in command for word in ["hello", "hi", "hey"]):
            speak("Hello! How can I assist you?")

        elif any(word in command for word in ["time", "clock"]):
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            speak("What should I search?")
            query = take_command()
            answer_question(query)

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "weather" in command:
            speak("Tell me the city name")
            city = take_command()
            get_weather(city)

        elif "send email" in command:
            send_email()

        elif "reminder" in command:
            set_reminder()

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command == "":
            continue

        else:
           speak("Let me find that for you")
           answer_question(command)

# ---------------- RUN ----------------
if __name__ == "__main__":
    run_assistant()