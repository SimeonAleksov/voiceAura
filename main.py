import pyautogui
import speech_recognition as sr
from recognizer import recognize_from_mic

pyautogui.PAUSE = 0.5
led_status = False
recognizer = sr.Recognizer()
mic = sr.Microphone()

print('LED status: ')
response = recognize_from_mic(recognizer, mic)
while response['transcription'] is None:
    print("Try again")
    response = recognize_from_mic(recognizer, mic)


if response['transcription'] == 'off':
    print("Turning LEDs off..")
    pyautogui.click('off.png')
elif response['transcription'] == 'turn on':
    print("Turning LEDs on..")
    pyautogui.click('on.png')
    led_status = True

if led_status:
    print("LED mode: ")
    response = recognize_from_mic(recognizer, mic)
    while response['transcription'] is None:
        response = recognize_from_mic(recognizer, mic)
    if response['transcription'] == 'music':
        pyautogui.click('buttons/music.png')
        pyautogui.click('buttons/apply.png')
    elif response['transcription'] == 'static':
        pyautogui.click('buttons/static.png')
        pyautogui.click('buttons/apply.png')
    elif response['transcription'] == 'flash':
        pyautogui.click('buttons/flash.png')
        pyautogui.click('buttons/apply.png')