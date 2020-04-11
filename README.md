# Voice AURA
AURA is Asus app for controlling LEDs. Voice AURA is simple python script that runs voice recognition and controls the applications. It uses PyAutoGui, so you have to have the AURA application on the screen somewhere. Sadly, Asus only have SDK for C#, C++ and I can't be bothered to make whole wrapper in python. 

### Installation

Dillinger requires [Python](https://www.python.org/) to run.

Install the libraries.

```sh
$ pip install requirements.txt
```

If you're on windows you might have to download [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) manually and install it.

```sh
$ pip install PyAudio-0.2.11-cp38-cp38-win32.whl
```
Then simply,
```sh
$ python main.py 
```
and start talking.
