import datetime, sounddevice, wavio, winsound, pyttsx3
from scipy.io.wavfile import *

def Banner(a):
	print("\n"+"#"*57)
	print("#\t\tWelcome to KashY "+a+"\t\t#")
	print("#"*57+"\n\n")

def get_filename():
	Banner("Voice Recorder")
	fname = input("Enter Filename of Recording\t\t:\t")
	time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
	file_name = fname+'-KashY_VR-'+time_stamp+'.mp3'
	return (file_name)

def speak(text):
	t2v = pyttsx3.init()
	voices = t2v.getProperty('voices')
	t2v.setProperty('voice', voices[2].id)
	t2v.say(text)
	t2v.runAndWait()
	
def KashY_VR(filename):
	
	duration_in_sec = input("Enter Duration of Recording in seconds\t:\t")
	
	freq = 17128
	Recording_duration_in_sec = int(duration_in_sec)
	
	Note_text = "Start Recording after Beep Sound ..."
	start_text = "Recording Started"
	End_text = "Recording Stoped and saved as"+filename
	
	
	speak(Note_text)
	winsound.Beep(1000, 100)
	speak(start_text)
	recording = sounddevice.rec(int(Recording_duration_in_sec * freq),samplerate=freq, channels=2)
	sounddevice.wait(0)
	winsound.Beep(1000, 100)
	speak(End_text)
	wavio.write(filename, recording, freq, sampwidth=3)


KashY_VR(get_filename())
