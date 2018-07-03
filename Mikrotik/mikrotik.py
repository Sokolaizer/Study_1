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


cfg_file = open('mikcon.txt', 'w')
in_file = open('Input.txt')
ext_net = Ip(input('External Network:'), input('Mask:'))
int_net = Ip(input('Internal Network:'), input('Mask:'))
voip_net = Ip(input('VoiceIP Network:'), input('Mask:'))
wifi_net = Ip(input('Wi-Fi Network:'), input('Mask:'))
tunnel_int = input('Tunnel interface to SAV2-Router:')
src_address = input('Source address:')
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
