#-*-coding: utf-8-*-
from tkinter import *
from json import loads, dumps
from random import choice
from codecs import open as copen
from time import sleep
from winsound import PlaySound, SND_ASYNC

def playsound(file):
	PlaySound(file, SND_ASYNC)


def load_content(file):
		try:
			with open(file, "r", encoding="utf-8") as f:
				return loads(f.read())
		except:
			return -1
class Kanji:
	def __init__(self, kanji="source\\basic_kanji.json"):
		self.kanji = load_content(kanji)

	def get_random_char(self, label, hiragana):
		ck = choice(list(self.kanji)) #ck = current kanji
		label.config(text=choice(list(self.kanji)))
		#print(self.kanji[ck][1])
		hiragana.config(text="Pronunciation: {}".format(", ".join(self.kanji[ck][0])))

	def check_result(self, root, label, entry, hiragana):
		ans = entry.get()
		ans = ans.strip().lower()
		current_kanji = label["text"]
		current_answers = self.kanji[current_kanji][1]
		#print(current_answers)
		entry.delete(0, "end")
		#print(ans)
		if ans in current_answers: #you fucking idiot
			playsound("source\\correct.wav")
			label.config(bg="#51F661")
			root.update()
			sleep(0.1)
			label.config(bg="#FA5858")
			self.get_random_char(label, hiragana) 
		else:
			playsound("source\\wrong.wav")
			label.config(bg="#F52E2E")
			root.update()
			sleep(0.1)
			label.config(bg="#FA5858")




class Kana:
	def __init__(self, kana="source\\alphabet.json",  mode=1):
		self.kana = load_content(kana)
		#self.kanji = self.load_content(kanji) || 
		self.mode = mode
		self.char = ""
		if self.kana == -1:
			print("There was a problem loading the file.")
			exit()

	def get_random_char(self, label):
		self.char = choice(list(self.kana))
		#print(self.char)
		label.config(text=self.kana[self.char][self.mode])

	def check_result(self, root, label, entry):
		ans = entry.get()
		ans = ans.strip().lower()
		entry.delete(0, "end")
		if ans == self.char:
			playsound("source\\correct.wav")
			label.config(bg="#51F661")
			root.update()
			sleep(0.1)
			label.config(bg="#FA5858")
			self.get_random_char(label)
		else:
			playsound("source\\wrong.wav")
			label.config(bg="#F52E2E")
			root.update()
			sleep(0.1)
			label.config(bg="#FA5858")

class Menu:
	def __init__(self):
		self.closed = False

	def select_mode(self):
		root = Tk()
		root.title("Main Menu")
		root.geometry("800x450")
		root.protocol("WM_DELETE_WINDOW", lambda *args, **kwargs:self.__on_close(root))
		mframe = Frame(root, bg="white")
		mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
		title = Label(mframe, bg="white", font='Helvetica 18 bold', fg="black", text="Main Menu")
		title.place(relx = 0.3, rely=0.1, relwidth=0.4, relheight=0.1)
		hiragana = Button(mframe, text="Hiragana", bg="#FA5858",font="Helvetica 14 bold", fg="white", command=lambda: self.start(root, 1))
		hiragana.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)
		katakana = Button(mframe, text="Katakana", bg="#FA5858", font="Helvetica 14 bold", fg="white", command=lambda: self.start(root, 0))		
		katakana.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
		kanji = Button(mframe, text="Kanji", bg="#FA5858", font="Helvetica 14 bold", fg="white", command=lambda: self.start(root,2))
		kanji.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)
		root.mainloop()

	def start(self, root, mode):
		root.destroy()
		if mode == 2:
			kanji()
		else:
			run(mode)

	def __on_close(self, root):
		root.destroy()
		self.closed = True

def close(root):
	root.destroy()
	menu.closed = True


def kanji():
	characters = Kanji()
	root = Tk()
	root.title("Learn kanji")
	root.geometry("800x450")
	root.protocol("WM_DELETE_WINDOW", lambda *args, **kwargs:close(root))
	mframe = Frame(root, bg="white")
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	ltitle = Label(mframe, bg="white", fg="black", font=("Courier", 20), text="Kanji")
	ltitle.place(relx=0, rely=0.05, relwidth=1, relheight=0.1)
	letter = Label(mframe, bg="#FA5858", fg="white",font=("Courier", 16))
	letter.place(relx=0, rely=0.2, relwidth=1, relheight=0.15) 
	hiragana = Label(mframe, bg="white", fg="black", font=("Courier", 16))
	hiragana.place(relx=0.25, rely= 0.7, relwidth=0.5, relheight=0.14)	
	characters.get_random_char(letter, hiragana)
	background = Label(mframe, bg="#FA5858")
	background.place(relx=0.25, rely=0.48, relwidth=0.5, relheight=0.14)
	entry = Entry(mframe)
	entry.place(relx=0.34, rely=0.5, relwidth=0.2, relheight=0.1)
	check = Button(mframe, text="Check!", command=lambda: characters.check_result(root, letter, entry, hiragana))
	check.place(relx=0.55, rely=0.5, relwidth=0.1, relheight=0.1)
	root.bind("<Return>", lambda *args, **kwargs:characters.check_result(root, letter, entry, hiragana))
	go_back = Button(root, bg="#FA5858", fg="white", text="<-", command=lambda:root.destroy())
	go_back.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.05)
	root.mainloop()


def run(m):
	kana = Kana(mode=m)
	if m == 1:
		title = "Hiragana"
	else:
		title = "Katakana"
	root = Tk()
	root.title("Learn kana")
	root.protocol("WM_DELETE_WINDOW", lambda *args, **kwargs:close(root))
	root.geometry("800x450")
	mframe = Frame(root, bg="white")
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	ltitle = Label(mframe, bg="white", fg="black", font=("Courier", 20), text=title)
	ltitle.place(relx=0, rely=0.05, relwidth=1, relheight=0.1)
	letter = Label(mframe, bg="#FA5858", fg="white",font=("Courier", 16))
	letter.place(relx=0, rely=0.2, relwidth=1, relheight=0.15) 
	kana.get_random_char(letter)
	background = Label(mframe, bg="#FA5858")
	background.place(relx=0.25, rely=0.48, relwidth=0.5, relheight=0.14)
	entry = Entry(mframe)
	entry.place(relx=0.34, rely=0.5, relwidth=0.2, relheight=0.1)
	check = Button(mframe, text="Check!", command=lambda: kana.check_result(root, letter, entry))
	check.place(relx=0.55, rely=0.5, relwidth=0.1, relheight=0.1)
	root.bind("<Return>", lambda *args, **kwargs:kana.check_result(root, letter, entry))
	go_back = Button(root, bg="#FA5858", fg="white", text="<-", command=lambda:root.destroy())
	go_back.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.05)
	root.mainloop()


if __name__ == '__main__':
	menu = Menu()
	while not menu.closed:
		menu.select_mode()