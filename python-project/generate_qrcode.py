import qrcode
import sys

arguments=sys.argv



input_URL = arguments[1]

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("img/url_qrcode.png")

print(qr.data_list)
