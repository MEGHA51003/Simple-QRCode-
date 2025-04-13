import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=4
)
qr.add_data(
    " https://thumbs.dreamstime.com/b/hands-hold-vast-universe-filled-planets-stars-emanating-beams-light-illustration-symbolizes-divine-presence-352083780.jpg"
)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")


img.save("image of universe.png")
