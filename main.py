import speech_recognition as sr
import function
from Voice import speak
import time
import extended_function
import sys
import requests
from pydub import AudioSegment
from pydub.effects import normalize
from io import BytesIO

recognizer = sr.Recognizer()
mic = sr.Microphone()


speak("Здраствуйте я ассистент джарвис")

user_commands = {
    "выключи компьютер":function.shutdown_computer,
    "открой оперу":function.open_opera,
    "открой о":function.open_opera,
    "открой youtube":function.open_url_youtube,
    "открой редактор":function.open_vsc,
    "ты здесь":function.bot_odp,
    "закрой оперу":function.close_opera,
    "закрой о":function.close_opera,
    "сверни окна":extended_function.show_desktop,
    "верни окна":extended_function.show_desktop,
    "сверни ок":extended_function.show_desktop,
    "верни ок":extended_function.show_desktop,
    "закрой редактор":function.close_vsc
}

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Слушаю...")
        audio = recognizer.listen(source, phrase_time_limit=5)


        audio_bytes = BytesIO(audio.get_wav_data())
        sound = AudioSegment.from_file(audio_bytes, format="wav")
        sound = normalize(sound)  


        audio_normalized = sr.AudioData(sound.raw_data, sound.frame_rate, sound.sample_width)


    try:
        command = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("Ты сказал:", command)

        if "стоп" in command:
            speak("Выключаюсь")
            time.sleep(0.5)
            sys.exit()

        user_input = command

        if "включи" in command:
            search = command.split("включи", 1)[1].strip()
            query = {'search_query': search}
            req = requests.get("https://www.youtube.com/results", params=query)
            function.search_youtube(req.url)
            


        else:
            for key, action in user_commands.items():
                if key in user_input:
                    action()
                    break

    except Exception as e:
        print("Не понял:", e)
