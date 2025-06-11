![Voice Agent Diagram](./1.pdf)

Requirements:

	•	Python 3.10
	•	ffmpeg (for Whisper)
	•	Installed Python packages from requirements.txt
	•	Ollama (installed and running)
	•	Downloaded model: mistral (or another model of your choice)

 Model Setup:

        You need to have the Mistral model available in Ollama:  
        ollama run mistral
        You can leave this running in a separate terminal window, or start the Ollama server:
        ollama serve

🎧 How it works:

	1.	🎙️ Records 5 seconds of audio from your microphone
	2.	🧠 Transcribes it using Whisper locally
	3.	💬 Sends the transcribed text to a local Mistral model via Ollama API
	4.	🗣️ Speaks the response using pyttsx3 text-to-speech

⸻

🧪 To Run the Agent:

    Activate your virtual environment, then:
    python -m scripts.conversation_loop

This will start a loop that records → transcribes → asks the model → replies back three times or until you say “exit” / “bye” / “вихід”.


💡 Notes:

	•	The audio is saved temporarily as output.wav.
	•	You can customize the number of turns or recording duration in the conversation_loop.py script.
	•	The agent uses Whisper for transcription and pyttsx3 for TTS — everything runs locally.
