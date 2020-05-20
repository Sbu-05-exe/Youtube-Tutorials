import tkinter as tk
from tkinter import filedialog, Text
import os

turquoise = '#263d42'

apps = []

if os.path.isfile('save.txt'):
	with open('save.txt','r') as f:
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = tempApps
		# Filter for empty strings
		apps = [app for app in tempApps if app.strip()]
		print(apps)

class App(tk.Tk):
	def __init__(self):
		self = super().__init__()

	def create_widgets():
		canvas = tk.Canvas(root, bg=turquoise)
		canvas.pack(fill='both')

		frame = tk.Frame(root, bg='white')
		frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		openFile = tk.Button(root, text='Open file', padx=10, pady=5, fg='white', bg=turquoise, command = addApp)
		openFile.pack(side='left')

		runApps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg='white', bg=turquoise, command = runApps)
		runApps.pack(side='left')

	def addApp():
		for widget in frame.winfo_children():
			widget.destroy()

			filename = filedialog.askopenfilename(initialdir='/', title='Select FIle', filetypes=(('executables','*.exe'), ('all files', '*.*')))
			apps.append(filename)
			print(filename)
			for app in apps:
				label = tk.Label(frame, text=app, bg='gray',pady=2)
				label.pack()

		def runApps():
			for app in apps:
				os.startfile(app)		

	def run(self):
		self.mainloop()

	def refresh(self):
		for app in apps:
			label = tk.Label(frame, text=app)
			label.pack(side='top', fill='x',ipady=10,pady=1,padx=1)


def main():
	app = App()
	app.title('workflows')
	app.state('zoomed')
	app.run()

	with open('save.txt', 'w') as f:
		for app in apps:
			f.write(app + ',')

if __name__ == '__main__':
	main()

