import requests
from stt.record_and_transcribe import record_audio, transcribe_with_whisper
from tts.speak import speak
from scripts import vision_agent


def agent_reply(user_text):
    print("Запит до Mistral:", user_text)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": user_text,
            "stream": False  # відповідь, а не шматками
        }
    )

    result = response.json()
    reply = result.get("response", "").strip()
    print("Mistral:", reply)
    # Зберегти відповідь у текстовий лог-файл
    with open("tests/mistral_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {user_text}\nMistral: {reply}\n\n")
    return reply

def conversation_loop(max_turns=3):
    turn = 0

    while turn < max_turns:
        record_audio()
        user_input = transcribe_with_whisper()
        print("You said:", user_input)

        if user_input.lower().strip() in ["bye", "exit", "вихід"]:
            speak("Goodbye!")
            break

        if "фото" in user_input or "зображення" in user_input or "аналізуй" in user_input:
            speak("Дивлюсь на зображення...")
            labels = vision_agent.analyze_image("media/cat2.JPEG")
            if labels:
                speak("Я бачу: " + ", ".join(labels))
            else:
                speak("Я нічого не розпізнала.")
            continue 

        response = agent_reply(user_input)
        speak(response)

        turn += 1


    print("Session ended after", turn, "turns.")
    speak("Conversation finished. Bye bye!")

if __name__ == "__main__":
    conversation_loop()


  


