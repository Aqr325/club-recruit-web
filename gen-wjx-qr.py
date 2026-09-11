import qrcode
from PIL import Image

url = "https://v.wjx.cn/vm/tA2r4Gx.aspx"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#2563eb", back_color="white").convert("RGB")
img.save("assets/wjx-qr.png")
print("saved assets/wjx-qr.png")
