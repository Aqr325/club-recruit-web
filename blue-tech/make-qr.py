import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

token = "?eo_token=168c8d334beca1b389345ec64d198b17&eo_time=1789125751"
base = "https://jkc-club-recruit-web-oodut5jc.edgeone.cool" + token
pages = [
    ("首页", base + "/blue-tech/index.html"),
    ("了解我们", base + "/blue-tech/about.html"),
    ("四大部门", base + "/blue-tech/departments.html"),
    ("加入我们", base + "/blue-tech/join.html"),
]

out_dir = os.path.dirname(os.path.abspath(__file__))
files = []
for label, url in pages:
    qr = qrcode.QRCode(version=5, box_size=12, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2563eb", back_color="#f0f6ff").convert("RGB")
    files.append((label, img))
    img.save(os.path.join(out_dir, f"qr-{label}.png"))

# 主码：首页（扫码进入后可站内跳转）
home = qrcode.QRCode(version=6, box_size=14, border=3, error_correction=qrcode.constants.ERROR_CORRECT_H)
home.add_data(base + "/blue-tech/index.html")
home.make(fit=True)
home.make_image(fill_color="#2563eb", back_color="#f0f6ff").convert("RGB").save(os.path.join(out_dir, "qr-蓝色科技版.png"))

cell = 360
sheet = Image.new("RGB", (cell * 2, cell * 2 + 80), "#f0f6ff")
draw = ImageDraw.Draw(sheet)

try:
    font = ImageFont.truetype("msyh.ttc", 24)
    small = ImageFont.truetype("msyh.ttc", 16)
except Exception:
    font = ImageFont.load_default()
    small = ImageFont.load_default()

positions = [(0, 80), (cell, 80), (0, cell + 80), (cell, cell + 80)]
for i, (label, img) in enumerate(files):
    x, y = positions[i]
    img_resized = img.resize((cell - 80, cell - 80))
    sheet.paste(img_resized, (x + 40, y + 20))
    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((x + (cell - tw) // 2, y + cell - 50), label, fill="#2563eb", font=font)

title = "科创部新伙伴共创计划 · 招新扫码方案"
bbox = draw.textbbox((0, 0), title, font=font)
tw = bbox[2] - bbox[0]
draw.text(((cell * 2 - tw) // 2, 25), title, fill="#2563eb", font=font)

hint = "微信扫码进入首页，点导航可跳转各页面"
bbox = draw.textbbox((0, 0), hint, font=small)
tw = bbox[2] - bbox[0]
draw.text(((cell * 2 - tw) // 2, 56), hint, fill="#64748b", font=small)

sheet.save(os.path.join(out_dir, "qr-preview.png"))
print("Generated:", ", ".join([f"qr-{l}.png" for l, _ in pages]) + ", qr-蓝色科技版.png, qr-preview.png")
