#-*-coding: utf-8-*-
from tkinter import *
from json import loads, dumps
from random import choice
from codecs import open as copen
from time import sleep
from winsound import PlaySound, SND_ASYNC

def playsound(file):
	PlaySound(file, SND_ASYNC)

class Kana:
	def __init__(self, file="alphabet.json", mode=1):
		self.load_content(file)
		self.mode = mode
		self.current_char = ""
		if self.content == -1:
			print("There was a problem loading the file.")
			exit()

	def load_content(self, file):
		try:
			with open(file, "r", encoding="utf-8") as f:
				self.content = loads(f.read())
		except:
			self.content = -1

	def get_random_char(self, label):
		self.char = choice(list(self.content))
		#print(self.char)
		label.config(text=self.content[self.char][self.mode])

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
		root.geometry("500x500")
		root.protocol("WM_DELETE_WINDOW", lambda *args, **kwargs:self.__on_close(root))
		mframe = Frame(root, bg="white")
		mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
		title = Label(mframe, bg="white", font='Helvetica 18 bold', fg="black", text="Main Menu")
		title.place(relx = 0.3, rely=0.1, relwidth=0.4, relheight=0.1)
		hiragana = Button(mframe, text="Hiragana", bg="#FF9760",font="Helvetica 14 bold", fg="black", command=lambda: self.start(root, 1))
		hiragana.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)
		katakana = Button(mframe, text="Katakana", bg="#FF9760", font="Helvetica 14 bold", fg="black", command=lambda: self.start(root, 0))		
		katakana.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
		root.mainloop()

	def start(self, root, mode):
		root.destroy()
		run(mode)

	def __on_close(self, root):
		root.destroy()
		self.closed = True


def run(m):
	kana = Kana(mode=m)
	root = Tk()
	root.title("Learn kana")
	root.geometry("500x500")
	mframe = Frame(root, bg="white")
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	letter = Label(mframe, bg="#FA5858", fg="white",font=("Courier", 16))
	letter.place(relx=0, rely=0.2, relwidth=1, relheight=0.15) 
	kana.get_random_char(letter)
	entry = Entry(mframe)
	entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)
	check = Button(mframe, text="Check!", command=lambda: kana.check_result(root, letter, entry))
	check.place(relx=0.45, rely=0.85, relwidth=0.1, relheight=0.1)
	root.bind("<Return>", lambda *args, **kwargs:kana.check_result(root, letter, entry))
	root.mainloop()


if __name__ == '__main__':
	menu = Menu()
	while not menu.closed:
		menu.select_mode()