from tkinter import *


class Ip:
    def __init__(self, ip, mask):
        self.ip = ip.split('.')
        self.mask = mask

    def __str__(self):
        result = ''
        for i in self.ip:
            result += str(i) + '.'
        result = result[:-1]
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


def solver(a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2):
    cfg_file = open('mikcon.txt', 'w')
    in_file = open('Input.txt')
    ext_net = Ip(a1, a2)
    int_net = Ip(b1, b2)
    voip_net = Ip(c1, c2)
    wifi_net = Ip(d1, d2)
    tunnel_int = Ip(e1, e2)
    src_address = Ip(f1, f2)
    for lines in in_file:
        f_lines = lines.format(ext_net=ext_net,
                               int_net=int_net,
                               voip_net=voip_net,
                               wifi_net=wifi_net,
                               tunnel_int=tunnel_int,
                               int_net_pool=int_net.pool(),
                               ext_net_pool=ext_net.pool(),
                               voip_net_pool=voip_net.pool(),
                               wifi_net_pool=wifi_net.pool(),
                               ext_net_dhcp=ext_net.dhcp(),
                               ext_net_gw=ext_net.gw(),
                               int_net_dhcp=int_net.dhcp(),
                               int_net_gw=int_net.gw(),
                               voip_net_dhcp=voip_net.dhcp(),
                               voip_net_gw=voip_net.gw(),
                               wifi_net_dhcp=wifi_net.dhcp(),
                               wifi_net_gw=wifi_net.gw(),
                               src_address=src_address
                               )
        print(f_lines.strip(), file=cfg_file)
    cfg_file.close()
    in_file.close()


def handler():
    a_v1 = entry1.get()
    a_v12 = entry12.get()
    b_v2 = entry2.get()
    b_v22 = entry22.get()
    c_v3 = entry3.get()
    c_v32 = entry32.get()
    d_v4 = entry4.get()
    d_v42 = entry42.get()
    e_v5 = entry5.get()
    e_v52 = entry52.get()
    f_v6 = entry6.get()
    f_v62 = entry62.get()
    solver(a_v1, a_v12, b_v2, b_v22, c_v3, c_v32, d_v4, d_v42, e_v5, e_v52, f_v6, f_v62)


root = Tk()
root.geometry("300x300+300+300")
root.title("Mikrotik Configurator")
frame1 = Frame(root)
frame1.pack(fill=X)

lbl1 = Label(frame1, text="External Network", width=14)
lbl1.pack(side=LEFT, padx=5, pady=5)

entry1 = Entry(frame1)
entry1.pack(side=LEFT, padx=5, expand=True)
entry12 = Entry(frame1)
entry12.pack(side=LEFT, padx=5, expand=True)

frame2 = Frame(root)
frame2.pack(fill=X)

lbl2 = Label(frame2, text="Internal Network", width=14)
lbl2.pack(side=LEFT, padx=5, pady=5)

entry2 = Entry(frame2)
entry2.pack(side=LEFT, padx=5, expand=True)
entry22 = Entry(frame2)
entry22.pack(side=LEFT, padx=5, expand=True)

frame3 = Frame(root)
frame3.pack(fill=X)

lbl3 = Label(frame3, text="VoiceIP Network", width=14)
lbl3.pack(side=LEFT, padx=5, pady=5)

entry3 = Entry(frame3)
entry3.pack(side=LEFT, padx=5, expand=True)
entry32 = Entry(frame3)
entry32.pack(side=LEFT, padx=5, expand=True)

frame4 = Frame(root)
frame4.pack(fill=X)

lbl4 = Label(frame4, text="Wi-Fi Network", width=14)
lbl4.pack(side=LEFT, padx=5, pady=5)

entry4 = Entry(frame4)
entry4.pack(side=LEFT, padx=5, expand=True)
entry42 = Entry(frame4)
entry42.pack(side=LEFT, padx=5, expand=True)

frame5 = Frame(root)
frame5.pack(fill=X)

lbl5 = Label(frame5, text="Tunnel interface", width=14)
lbl5.pack(side=LEFT, padx=5, pady=5)

entry5 = Entry(frame5)
entry5.pack(side=LEFT, padx=5, expand=True)
entry52 = Entry(frame5)
entry52.pack(side=LEFT, padx=5, expand=True)

frame6 = Frame(root)
frame6.pack(fill=X)

lbl6 = Label(frame6, text="Source Address", width=14)
lbl6.pack(side=LEFT, padx=5, pady=5)

entry6 = Entry(frame6)
entry6.pack(side=LEFT, padx=5, expand=True)
entry62 = Entry(frame6)
entry62.pack(side=LEFT, padx=5, expand=True)

okbtn = Button(root, text="Submit", command=handler)
okbtn.pack(fill=X, padx=5, expand=True)
root.mainloop()
