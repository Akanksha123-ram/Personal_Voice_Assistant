# simple_assistant.py
# Minimal voice assistant: wake word "jarvis", basic commands.
# Requires: speechrecognition, pyttsx3, pyjokes, wikipedia
# Install: pip install SpeechRecognition pyttsx3 pyjokes wikipedia

import time
import webbrowser
from datetime import datetime

import pyttsx3
import speech_recognition as sr

try:
    import pyjokes
except Exception:
    pyjokes = None

try:
    import wikipedia
except Exception:
    wikipedia = None

WAKE = "jarvis"

tts = pyttsx3.init()
r = sr.Recognizer()

def speak(text: str):
    print("Assistant:", text)
    tts.say(text)
    tts.runAndWait()
    import pyttsx3
tts = pyttsx3.init(driverName='sapi5')


def listen_once(timeout=5, phrase_time_limit=6):
    """Listen once and return recognized text or None."""
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.6)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        return r.recognize_google(audio)
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
    except Exception:
        return None

def handle_command(cmd: str) -> bool:
    """Return False to stop the assistant, True to continue."""
    text = cmd.lower().strip()
    if text in ("quit", "exit", "stop", "bye"):
        speak("Goodbye.")
        return False

    if "time" in text:
        speak(datetime.now().strftime("It's %I:%M %p."))
        return True

    if "date" in text or "day" in text:
        speak(datetime.now().strftime("Today is %A, %B %d, %Y."))
        return True

    if text.startswith("open "):
        target = text[len("open "):].strip()
        if "." in target or target.startswith(("http://", "https://")):
            if not target.startswith(("http://", "https://")):
                target = "https://" + target
            webbrowser.open(target)
            speak(f"Opening {target}")
        else:
            webbrowser.open(f"https://www.google.com/search?q={target.replace(' ', '+')}")
            speak(f"Searching for {target}")
        return True

    if "wikipedia" in text:
        if wikipedia:
            topic = text.replace("wikipedia", "").strip()
            if not topic:
                speak("What topic should I look up on Wikipedia?")
                return True
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"That topic is too broad. Try being more specific, like {e.options[0]} or {e.options[1]}.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find that page on Wikipedia.")
            except Exception:
                speak("Sorry, there was a problem connecting to Wikipedia.")
        else:
            speak("Wikipedia support is not installed.")
        return True

    if "joke" in text:
        if pyjokes:
            speak(pyjokes.get_joke())
        else:
            speak("I don't have jokes installed.")
        return True

    # fallback
    speak("Sorry, I didn't understand that. I can tell time, date, open websites, search, wikipedia or tell jokes.")
    return True

def main():
    speak(f"Hi — say '{WAKE}' followed by a command, or say 'quit' to exit.")
    running = True
    while running:
        print("Listening for wake word...")
        heard = listen_once(timeout=6, phrase_time_limit=4)
        if not heard:
            print("(no speech detected, you can type a command or press Enter to continue listening)")
            fallback = input("Type command (or Enter to keep listening): ").strip()
            if fallback:
                running = handle_command(fallback)
            continue

        print("Heard:", heard)
        low = heard.lower().strip()
        if low.startswith(WAKE):
            remainder = low[len(WAKE):].strip(" ,.!?")
            if not remainder:
                speak("Yes?")
                cmd = listen_once()
                if not cmd:
                    fallback = input("I didn't catch that — type command (or Enter to cancel): ").strip()
                    if fallback:
                        running = handle_command(fallback)
                    continue
                running = handle_command(cmd)
            else:
                running = handle_command(remainder)
        else:
            print("Wake word not detected. Say 'jarvis' before a command.")

        time.sleep(0.3)

if __name__ == "__main__":
    main()

