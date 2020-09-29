import speech_recognition as sr
import webbrowser
import pyttsx3
print("welcome to my app\n\n")

print("speak ur choice " , end='')

r = sr.Recognizer()

with sr.Microphone() as source:
    print('start')
    audio = r.listen(source)
    print('stop')

rg = r.recognize_google(audio)


if (("run" in rg) or ("launch" in rg) and ("Linux" in rg) or ("commands" in rg)):
	webbrowser.open("http://http://192.168.1.102/task2.html")
	pyttsx3.speak("Opening a Page  to launch Linux Command")
elif (("run" in rg) or ("launch" in rg) and ("docker" in rg) or ("container" in rg)):
	webbrowser.open("http://192.168.1.102/drun.html")


 
else:
	print("not understand")
