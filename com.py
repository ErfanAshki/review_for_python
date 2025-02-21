import pyqrcode
import png

text = 'slm khoshgele'

qr_code = pyqrcode.create(text)

qr_code.svg('qr_svg', scale=6)

qr_code.png('qr_png.png', scale=6)

