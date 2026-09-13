import base64, os, re

base = r"D:/workbuddy workspace/2026-09-11-16-30-29/club-recruit-web"
join_path = os.path.join(base, "join.html")

# Generate WeChat group QR base64 data URI
qr_path = os.path.join(base, "assets", "wechat-group.jpg")
ext = os.path.splitext(qr_path)[1].lower()
mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}.get(ext, "image/png")
with open(qr_path, "rb") as f:
    wechat_uri = f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"

with open(join_path, "r", encoding="utf-8") as f:
    s = f.read()

# Replace the first JPEG data URI (consult QQ group QR) with WeChat group QR
s = re.sub(r'<img src="data:image/jpeg;base64,[^"]*"', f'<img src="{wechat_uri}"', s, count=1)

# Update text content
s = s.replace("扫码咨询 QQ 群 114732666，扫码填写腾讯问卷报名登记", "扫码咨询微信群，扫码填写腾讯问卷报名登记")
s = s.replace("加入 QQ 咨询群，有问题随时问学长学姐", "加入微信咨询群，有问题随时问学长学姐")
s = s.replace("群号：114732666", "科技创新工作室招新群（微信群）")
s = s.replace("复制群号 📋", "复制群名 📋")
s = s.replace("如果二维码无法识别，可复制群号 114732666 手动搜索", "如果二维码无法识别，可联系管理员或同学邀请入群")

# Update copy button JS
s = s.replace("var text = '114732666';", "var text = '科技创新工作室招新群';")
s = s.replace("show('已复制群号：' + text)", "show('已复制群名：' + text)")

with open(join_path, "w", encoding="utf-8") as f:
    f.write(s)

print("join.html updated: QQ group -> WeChat group")
