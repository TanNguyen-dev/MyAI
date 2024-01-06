# AI Personal Assistant

## Overview

Welcome to the AI Personal Assistant project! This Python program serves as a virtual assistant capable of performing various tasks, including weather inquiries, music playback, web browsing, face recognition, and more. The system integrates speech recognition, text-to-speech, and external APIs to provide a dynamic and interactive user experience.

## Features

- **Voice Interaction:** Communicate with the assistant through speech recognition.
  
- **Task Automation:**
  - *Weather Information:* Retrieve real-time weather details for a specified city using the OpenWeatherMap API.
  - *Music Playback:* Play music from a designated directory.
  - *Web Browsing:* Open popular websites such as Facebook, YouTube, Gmail, and Spotify.
  - *Face Recognition:* Utilize the webcam for face recognition.
  - *Game Launch:* Start a simple game of Flappy Bird.
  - *System Control:* Shut down or restart the computer.

- **Information Retrieval:**
  - *Wikipedia Search:* Obtain a summary from Wikipedia based on user input.
  - *Date and Time:* Retrieve the current date and time.

## Technologies Used

- **Speech Recognition:** Utilizes the SpeechRecognition library for recognizing spoken words.
  
- **Text-to-Speech:** Employs the pyttsx3 library to convert text into spoken words.
  
- **OpenWeatherMap API:** Fetches real-time weather information.

- **Web Scraping:** Utilizes webbrowser module for opening specified websites.

- **Computer Vision:** Incorporates OpenCV for face recognition using the webcam.

## Getting Started

To run this code and experience the functionalities of the AI Personal Assistant, follow these steps:

1. **Clone Repository:** 
   - Open your preferred Python environment.
   - Clone the repository by executing the following command:
     ```
     git clone https://github.com/TanNguyen-dev/AI_Personal_Assistant.git
     ```

2. **Install Dependencies:**
   - Install the required libraries using:
     ```
     pip install SpeechRecognition pyttsx3 opencv-python wikipedia requests
     ```

3. **Run the Program:**
   - Navigate to the cloned repository in your Python environment.
   - Execute the program using:
     ```
     python MyAI.py
     ```

4. **Interact with the Assistant:**
   - Speak commands and inquiries to interact with the AI Personal Assistant.

Thank you for exploring the AI Personal Assistant! For any questions or improvements, feel free to reach out.
