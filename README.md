# 🎤 Personal Voice Assistant

A smart **Python-based voice assistant** that can listen, understand, and execute your commands. Built to make daily tasks easier by automating interactions with your computer, apps, and the web using voice commands.

---

## 🛠 Features

* **Voice Recognition** – Uses speech-to-text to understand commands.
* **Task Automation** – Perform tasks like opening apps, searching the web, or reading files.
* **Text-to-Speech** – Responds to the user with clear, natural-sounding voice output.
* **Cross-Platform Compatible** – Works on Windows (requires Python 3.10+).
* **Extensible** – Easily add custom commands and functionalities.

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/Akanksha123-ram/personal-voice-assistant.git
```

2. Navigate into the project folder:

```bash
cd personal-voice-assistant
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

> Make sure `PyAudio` is installed. If not, use the precompiled `.whl` for your Python version.

---

## 📝 Usage

Run the assistant:

```bash
python assistant.py
```

Sample commands you can try:

* "Open Chrome"
* "Search Python tutorials on Google"
* "What’s the weather today?"
* "Play music"

The assistant will respond through voice feedback and execute tasks automatically.

---

## 📂 Project Structure

```
personal-voice-assistant/
│
├─ assistant.py          # Main script to run the voice assistant
├─ commands.py           # Predefined command actions
├─ utils.py              # Helper functions for speech recognition, text-to-speech, etc.
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation
```

---

## 💡 Technologies Used

* **Python 3.13**
* **PyAudio** – Microphone input and audio output
* **SpeechRecognition** – Converts speech to text
* **pyttsx3** – Converts text to speech
* **OS & Webbrowser** – Task execution and automation

---

## 🌟 Future Enhancements

* Integration with **AI APIs** for intelligent responses
* Multi-language support
* Calendar and reminder management
* Home automation features

---

## 👤 Author

**Akanksha123-ram**
[GitHub](https://github.com/Akanksha123-ram)

---

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.
