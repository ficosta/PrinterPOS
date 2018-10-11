from escpos.printer import Usb
from PIL import *
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=13,
    border=0,
)
qr.add_data('FELIPE IASI DE BARROS COSTA DASDASD ASDAasdasdas dasdf asdfasd kfahsdg fkjasdgfkhasdg fhgsd kfhjgsa dhjfgsadhjkgfhjkasgdfjk sadghjf gshkjad gfhjasdg hfjsSD ASDASDASD ASDASDAS')
qr.make(fit=True)

maxsize = (381, 381)

img = qr.make_image(fill_color="black", back_color="white")
img.thumbnail(maxsize)
img.save('test.gif')
""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x0416, 0x5011)
p.image('test.gif')
#p.qr('felipe')
p.text('felipe')
p.text('\n\n')
