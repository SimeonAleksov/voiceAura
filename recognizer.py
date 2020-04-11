import time
import speech_recognition as sr

def recognize_from_mic(recognizer, mic):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError
    if not isinstance(mic, sr.Microphone):
        raise TypeError
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        'success': True,
        'error': None,
        'transcription': None
    }

    try:
        response['transcription'] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response['success'] = False
        response['error'] = "API unavalaible"
    except sr.UnknownValueError:
        response['error'] = 'Unable to recognize'
    
    return response