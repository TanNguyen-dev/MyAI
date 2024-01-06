import speech_recognition
import pyttsx3
from datetime import date, datetime
import wikipedia
import os
import requests
import json
import webbrowser
import cv2
import numpy as np

API_KEY = '0e47e4d08669890391f99c5d7e729917'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

# Initialize speech recognition, text-to-speech, and default robot brain
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ''


def FaceRecognition():
    """
    Perform face recognition using the webcam and OpenCV.
    """
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Open the webcam
    vid = cv2.VideoCapture(0)

    while True:
        # Read the frame
        ret, frame = vid.read()

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display the frame
        cv2.imshow('DETECTING FACE', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close all windows
    vid.release()
    cv2.destroyAllWindows()


def weather(city_name):
    """
    Get weather information for the given city using the OpenWeatherMap API.
    """
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(complete_url)
    data = response.json()
    if response.status_code == 200:
        main = data["main"]
        current_temperature = int(main['temp'] - 273.15)
        current_humidity = main["humidity"]
        z = data["weather"]
        weather_description = z[0]["description"]
        robot_brain = (
            "The weather in " + city_name + " now is "
            + str(weather_description)
            + ", The temperature is "
            + str(current_temperature)
            + " Celsius Degree,"
            + "The humidity is "
            + str(current_humidity)
            + " %"
        )
    else:
        robot_brain = "Undefined city"
    return robot_brain


def StartGoogle():
    """Start Google Chrome."""
    Speaking('starting google')
    os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')


def PlayMusic():
    """Play music from the specified directory."""
    music_dir = 'C:\\Allmusic'  # Directory for music
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))


def Wiki():
    """
    Search and return a summary from Wikipedia.
    """
    Speaking('searching on wikipedia')
    Speaking('Tell me the keywords')
    keyword = Listening()
    try:
        print('**Result from wiki**')
        return wikipedia.summary(keyword, sentences=1)
    except:
        print('Some error occurred! Try again.')
        print('')


def Listening():
    """
    Listen for user input using the microphone.
    """
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print('Robot: ...')
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ''

    print('You: ', you)
    return you


def Braining(you):
    """
    Process user input and generate appropriate responses.
    """
    if you == '':
        robot_brain = "Sorry, I can't hear you. Try again"
    elif 'hello' in you:
        robot_brain = "Hi there"
    elif 'today' in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif 'time' in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif 'Wikipedia' in you:
        robot_brain = Wiki()
    elif 'play music' in you:
        robot_brain = 'playing musics'
        PlayMusic()
    elif 'weather' in you:
        robot_brain = 'which city is it'
        print('Robot: ', robot_brain)
        Speaking(robot_brain)
        city_name = Listening()
        robot_brain = weather(city_name)
        while robot_brain == 'Undefined city':
            city_name = input("Robot: Type city's name:")
            robot_brain = weather(city_name)
    elif 'face recognition' in you:
        FaceRecognition()
        robot_brain = 'Opened Face Recognition'
    elif "Facebook" in you:
        webbrowser.open('https://www.facebook.com/', new=1)
        robot_brain = "Ok! Opening Facebook"
    elif 'YouTube' in you:
        webbrowser.open('https://www.youtube.com', new=1)
        robot_brain = "Ok! Opening Youtube"
    elif "Gmail" in you:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=1)
        robot_brain = "Ok! Opening Gmail"
    elif "Spotify" in you:
        webbrowser.open('https://open.spotify.com/?', new=1)
        robot_brain = "OK! Opening Spotify"
    elif 'shut down' in you:
        os.system('shutdown -s')
        robot_brain = 'Shutting down the computer'
    elif 'restart' in you:
        os.system('shutdown -r')
        robot_brain = 'Restarting the computer'
    elif 'game' in you:
        os.system('python flappybird.py')
        robot_brain = 'Opened Flappy Bird'
    elif 'bye' in you or 'stop' in you:
        robot_brain = 'Goodbye User'
    else:
        robot_brain = 'Sorry, I cannot understand you'
    print('Robot: ', robot_brain)
    return robot_brain


def Speaking(robot_brain):
    """Speak the given text using text-to-speech."""
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()


def Main():
    """Main function to run the AI program."""
    print('Welcome to AI 1.0')
    while True:
        you = Listening()
        robot_brain = Braining(you)
        Speaking(robot_brain)
        if robot_brain == 'Bye User':
            break


if __name__ == '__main__':
    Main()
