import pyttsx3
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfile



class Main(Frame):
    def __init__(self, master):
        """ Intislizaiton and running the GF """
        super(Main,self).__init__(master)
        self.grid()
        self.root = master
        self.main()



    def main(self):
        self.lbl = Label(self, text = 'What would you like to vokolize?')
        self.lbl.grid(row = 0, column = 1, columnspan = 3)

        self.bttn1 = Button(self, text = 'The text I will enter', command = self.enter_text )
        self.bttn1.grid(row = 1, column = 0, columnspan = 2)

        self.lbl_or = Label(self, text = 'or')
        self.lbl_or.grid(row = 1, column = 2)

        self.bttn2 = Button(self, text = 'File(txt)', command = self.file)
        self.bttn2.grid(row = 1, column = 3, sticky = 'W' )

    def file(self):
        self.lbl.destroy()
        self.bttn1.destroy()
        self.lbl_or.destroy()
        self.bttn2.destroy()

        self.back2 = Button(self, text='Back', command=self.back2)
        self.back2.grid(row=0, column=0, sticky='W')

        self.bttn4 = Button(self, text = 'Open file', command = self.open_file_and_say)
        self.bttn4.grid(row = 1, column = 0, sticky = 'W')

    def open_file_and_say(self):
        self.file = askopenfile('r').read()
        print(self.file)
        if len(self.file)> 0:

            engine = pyttsx3.init()
            engine.say(self.file)
            engine.runAndWait()
        else:
            showerror(title="Error", message="SoSi HeR!")

    def enter_text(self):
        self.lbl.destroy()
        self.bttn1.destroy()
        self.lbl_or.destroy()
        self.bttn2.destroy()

        self.back = Button(self, text = 'Back', command = self.back)
        self.back.grid(row = 0, column = 0, sticky = 'W')

        self.lbl2 = Label(self, text='Input some text below, to say it..')
        self.lbl2.grid()

        self.ent = Entry(self)
        self.ent.grid()

        self.bttn3 = Button(self, text='Say', command=self.entered_text)
        self.bttn3.grid()

    def back2(self):
        self.back2.destroy()
        self.bttn4.destroy()

        self.main()

    def back(self):
        self.back.destroy()
        self.lbl2.destroy()
        self.ent.destroy()
        self.bttn3.destroy()
        self.main()

    def entered_text(self):
        text = self.ent.get()

        if len(text) > 0:

            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        else:
            showerror(title = "Error", message = "SoSi HeR!")

def run():
    root = Tk()
    root.title("Sayer")
    root.geometry("260x110")
    app = Main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
else:
    print('Sock cock')
