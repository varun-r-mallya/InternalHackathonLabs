import qrcode
from random import randint

binary_str = "".join(str(randint(0, 1)) for _ in range(512)) #binary dump goes here
print(binary_str)
data = ''
for i in range(0, len(binary_str), 8):
    print(hex(int(binary_str[i:i+8], 2)))
    data += chr(int(binary_str[i:i+8], 2))

QRCodefile = "MUOQRCode.png"

QRimage = qrcode.make(data)

QRimage.save(QRCodefile)