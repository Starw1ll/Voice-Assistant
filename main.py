from config import NAME, OTHER_NAMES, SUPERFLUOUS_WORD, USING_PAID_GPT
import speech_to_text
from text_to_speech import speak
from fuzzywuzzy import fuzz
import datetime
import webbrowser
import random
import os
import num2textilka
from paid_gpt import gpt_paid
from free_gpt import gpt_free_g4f




def filter_cmd(raw_voice: str):
    """Удаляет лишние слова и обращения из команды."""
    cmd = raw_voice

    for x in OTHER_NAMES:
        cmd = cmd.replace(x, "").strip()

    for x in SUPERFLUOUS_WORD:
        cmd = cmd.replace(x, "").strip()
    return cmd


def recognize_cmd(cmd: str):
    """Распознаёт наиболее подходящую команду."""
    rc = {'cmd': '', 'percent': 0}
    for c, phrases in COMMANDS_PHRASES.items():
        for phrase in phrases:
            vrt = fuzz.ratio(cmd, phrase)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def current_time():
    now = datetime.datetime.now()
    result = f"Сейчас {num2textilka.num2text(now.hour)} часов {num2textilka.num2text(now.minute)} минут."
    speak(result)


def tell_joke():
    with open("jokes.txt", 'r', encoding='utf-8') as file:
        jokes = file.read().split('---')

    jokes = [joke.strip() for joke in jokes if joke.strip()]
    result = random.choice(jokes)
    speak(result)


def open_browser():
    webbrowser.open("google.com")
    speak("Открываю браузер.")


def open_calculator():
    os.system("calc")
    speak("Открываю калькулятор.")


def open_notepad():
    os.system("notepad")
    speak("Открываю блокнот.")


def open_explorer():
    os.system("explorer")
    speak("Открываю проводник.")


def open_task_manager():
    os.system("taskmgr")
    speak("Открываю диспетчер задач.")


def open_cmd():
    os.system("cmd")
    speak("Запускаю командную строку.")


def open_powershell():
    os.system("powershell")
    speak("Запускаю PowerShell.")


def open_snipping_tool():
    os.system("snippingtool")
    speak("Запускаю инструмент для скриншотов.")


def open_sound_control():
    os.system("sndvol")
    speak("Открываю микшер громкости.")


def open_device_manager():
    os.system("devmgmt.msc")
    speak("Открываю диспетчер устройств.")


def open_registry_editor():
    os.system("regedit")
    speak("Открываю редактор реестра.")


def open_services():
    os.system("services.msc")
    speak("Открываю список служб.")


def open_network_settings():
    os.system("ncpa.cpl")
    speak("Открываю настройки сети.")


def open_display_settings():
    os.system("desk.cpl")
    speak("Открываю настройки экрана.")


def open_mouse_settings():
    os.system("main.cpl")
    speak("Открываю настройки мыши.")


def open_keyboard_settings():
    os.system("control keyboard")
    speak("Открываю настройки клавиатуры.")


def open_power_settings():
    os.system("powercfg.cpl")
    speak("Открываю настройки управления питанием.")


def open_vlc():
    os.system('"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"')
    speak("Запускаю VLC Media Player.")


def open_chrome():
    os.system('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
    speak("Запускаю Google Chrome.")


def open_firefox():
    os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
    speak("Запускаю Mozilla Firefox.")


def open_edge():
    os.system("start msedge")
    speak("Запускаю Microsoft Edge.")


def open_steam():
    os.system('"C:\\Program Files (x86)\\Steam\\Steam.exe"')
    speak("Запускаю Steam.")


def generate_text(prompt: str):
    speak("Что надо сгенерировать?")
    text = input()
    if USING_PAID_GPT:
        result = gpt_paid(text)
    else:
        result = gpt_free_g4f(text)
    speak(result)


def show_help():
    result = (
        "Я могу открыть калькулятор, блокнот, проводник, диспетчер задач, "
        "браузеры, управление звуком, настройки сети, диспетчер устройств, "
        "и многое другое. Спросите меня!"
    )
    speak(result)


# Словарь с командами и их фразами для распознавания
COMMANDS_PHRASES = {
    'help': ['помощь', 'что ты умеешь', 'что ты можешь'],
    'ctime': ['время', 'который час', 'сколько времени'],
    'joke': ['шутка', 'анекдот', 'расскажи шутку'],
    'open_browser': ['открой браузер', 'запусти браузер', 'интернет'],
    'calculator': ['калькулятор', 'посчитай', 'открой калькулятор'],
    'notepad': ['блокнот', 'запиши', 'открой блокнот'],
    'explorer': ['проводник', 'открой папку'],
    'task_manager': ['диспетчер задач', 'открой диспетчер'],
    'cmd': ['командная строка', 'cmd', 'терминал'],
    'powershell': ['powershell', 'пауэршелл'],
    'snipping_tool': ['снимок экрана', 'скриншот'],
    'sound_control': ['звук', 'громкость'],
    'device_manager': ['диспетчер устройств', 'устройства'],
    'registry_editor': ['реестр', 'редактор реестра'],
    'services': ['службы', 'список служб'],
    'network_settings': ['сеть', 'настройки сети'],
    'display_settings': ['настройки экрана', 'экран'],
    'mouse_settings': ['мышь', 'настройки мыши'],
    'keyboard_settings': ['клавиатура', 'настройки клавиатуры'],
    'power_settings': ['управление питанием', 'питание'],
    'vlc': ['vlc', 'видео плеер'],
    'chrome': ['хром', 'google chrome', 'браузер хром'],
    'firefox': ['фаерфокс', 'mozilla'],
    'edge': ['эдж', 'браузер edge'],
    'steam': ['steam', 'стим'],
    'ai': ['искусственный интеллект', 'gpt', 'чатбот']
}

# Связь между командами и функциями
COMMANDS = {
    'help': show_help,
    'ctime': current_time,
    'joke': tell_joke,
    'open_browser': open_browser,
    'calculator': open_calculator,
    'notepad': open_notepad,
    'explorer': open_explorer,
    'task_manager': open_task_manager,
    'cmd': open_cmd,
    'powershell': open_powershell,
    'snipping_tool': open_snipping_tool,
    'sound_control': open_sound_control,
    'device_manager': open_device_manager,
    'registry_editor': open_registry_editor,
    'services': open_services,
    'network_settings': open_network_settings,
    'display_settings': open_display_settings,
    'mouse_settings': open_mouse_settings,
    'keyboard_settings': open_keyboard_settings,
    'power_settings': open_power_settings,
    'vlc': open_vlc,
    'chrome': open_chrome,
    'firefox': open_firefox,
    'edge': open_edge,
    'steam': open_steam,
    'ai': generate_text
}


def execute_cmd(cmd: str):
    action = COMMANDS.get(cmd)
    if action:
        action()
    else:
        speak("Извините, я не понял эту команду.")


def respond(voice: str):
    print(voice)
    if any(x in voice for x in OTHER_NAMES):
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd']:
            execute_cmd(cmd['cmd'])
        else:
            speak("Что вы сказали?")

def start_emma():
    print(f"Голосовой ассистент '{NAME}' запущен!")
    speech_to_text.listen(respond)

start_emma()