import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=5
)
data = "pies"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color='white')
img.save("nw.png")