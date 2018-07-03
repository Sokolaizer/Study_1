rawstring = input()
rawlist = rawstring.split('/')
rawlist[0] = rawlist[0].split('.')
ipaddr = list()
a = int(rawlist[1]) % 8
b = int(rawlist[1]) // 8
binmask = b * '11111111.' + (a * '1' + (8 - a) * '0') + (3 - b) * '.00000000'
binmask = binmask.split('.')
for octet in rawlist[0]:
    ipaddr.append(bin(int(octet)))
print(ipaddr)
tmp = '''
Network:
{:<8} {:<8} {:<8} {:<8b}
{:08b} {:08b} {:08b} {:08b}

Mask:
/{}
{:<8} {:<8} {:<8} {:<8}
{:<08} {:<08} {:<08} {:<08}
'''
print(tmp.format(int(rawlist[0][0]),
                 int(rawlist[0][1]),
                 int(rawlist[0][2]),
                 int(rawlist[0][3]),
                 int(rawlist[0][0]),
                 int(rawlist[0][1]),
                 int(rawlist[0][2]),
                 int(rawlist[0][3]),
                 int(rawlist[1]),
                 int(binmask[0], 2),
                 int(binmask[1], 2),
                 int(binmask[2], 2),
                 int(binmask[3], 2),
                 int(binmask[0]),
                 int(binmask[1]),
                 int(binmask[2]),
                 int(binmask[3]),
                 )
)
