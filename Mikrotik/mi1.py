from tkinter import *


class Ip:
    def __init__(self, ip, mask):
        self.ip = ip.split('.')
        self.mask = mask

    def __str__(self):
        result = ''
        for i in self.ip:
            result += str(i) + '.'
        result += '/' + self.mask
        return result

    def net(self):
        result = ''
        for i in self.ip[:-1]:
            result += str(i) + '.'
        return result

    def gw(self):
        return self.net() + '1'

    def dhcp(self):
        return self.net() + '0/' + self.mask

    def pool(self):
        return self.net() + '16-' + self.net() + '223'


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Mikrotik Configurator")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="External Network", width=14)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(side=LEFT, padx=5, expand=True)
        entry12 = Entry(frame1)
        entry12.pack(side=LEFT, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Internal Network", width=14)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(side=LEFT, padx=5, expand=True)
        entry22 = Entry(frame2)
        entry22.pack(side=LEFT, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="VoiceIP Network", width=14)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        entry3 = Entry(frame3)
        entry3.pack(side=LEFT, padx=5, expand=True)
        entry32 = Entry(frame3)
        entry32.pack(side=LEFT, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl4 = Label(frame4, text="Wi-Fi Network", width=14)
        lbl4.pack(side=LEFT, padx=5, pady=5)

        entry4 = Entry(frame4)
        entry4.pack(side=LEFT, padx=5, expand=True)
        entry42 = Entry(frame4)
        entry42.pack(side=LEFT, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)

        lbl5 = Label(frame5, text="Tunnel interface", width=14)
        lbl5.pack(side=LEFT, padx=5, pady=5)

        entry5 = Entry(frame5)
        entry5.pack(side=LEFT, padx=5, expand=True)
        entry52 = Entry(frame5)
        entry52.pack(side=LEFT, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=X)

        lbl6 = Label(frame6, text="Source Address", width=14)
        lbl6.pack(side=LEFT, padx=5, pady=5)

        entry6 = Entry(frame6)
        entry6.pack(side=LEFT, padx=5, expand=True)
        entry62 = Entry(frame6)
        entry62.pack(side=LEFT, padx=5, expand=True)

        okbtn = Button(self, text="Submit")
        okbtn.pack(fill=X, padx=5, expand=True)

    def inserter(value):
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = float(entry1.get())
            b_val = float(b.get())
            c_val = float(c.get())
            inserter(solver(a_val, b_val, c_val))
        except ValueError:
            inserter("Make sure you entered 3 numbers")





def main():
    root = Tk()
    root.geometry("300x300+300+300")
    app = GUI(root)
    root.mainloop()





main()