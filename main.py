#-*-coding: utf-8-*-
from tkinter import *
from json import loads, dumps
from random import choice
from codecs import open as copen
from time import sleep

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
		print(self.char)
		label.config(text=self.content[self.char][self.mode])
	def check_result(self, root, label, ans):
		ans = ans.lower()
		if ans == self.char:
			label.config(bg="#51F661")
			root.update()
			sleep(0.01)
			label.config(bg="#F52E2E")
			self.get_random_char(label)


def main():
	kana = Kana()
	root = Tk()
	root.title("Learn kanas")
	root.geometry("500x500")
	mframe = Frame(root, bg="white")
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	letter = Label(mframe, bg="#F52E2E", fg="white",font=("Courier", 16))
	letter.place(relx=0, rely=0.2, relwidth=1, relheight=0.15) #wtf is going on?
	kana.get_random_char(letter)#i am so tired
	entry = Entry(mframe)
	entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)
	check = Button(mframe, text="Check!", command=lambda: kana.check_result(root, letter, entry.get()))
	check.place(relx=0.45, rely=0.85, relwidth=0.1, relheight=0.1)
	root.bind("<Return>", lambda *args, **kwargs:kana.check_result(root, letter, entry.get()))
	root.mainloop()


if __name__ == '__main__':
	main()