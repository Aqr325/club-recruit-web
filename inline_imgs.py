import base64, os
base = r"D:/workbuddy workspace/2026-09-11-16-30-29/club-recruit-web"
def to_datauri(p):
    ext = os.path.splitext(p)[1].lower()
    mime = {".jpg":"image/jpeg",".jpeg":"image/jpeg",".png":"image/png",".gif":"image/gif"}.get(ext,"image/png")
    with open(p,"rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())
assets = {
    "assets/consult-qq-group.jpg": os.path.join(base,"assets","wechat-group.jpg"),
    "assets/signup-qr.png": os.path.join(base,"assets","signup-qr.png"),
    "assets/wjx-qr.png": os.path.join(base,"assets","wjx-qr.png"),
    "assets/qq-group.jpg": os.path.join(base,"assets","wechat-group.jpg"),
}
data = {}
for k,p in assets.items():
    if os.path.exists(p):
        data[k] = to_datauri(p)
        print("OK", k, len(data[k]), "chars")
jp = os.path.join(base,"join.html")
s = open(jp,encoding="utf-8").read()
for k,uri in data.items():
    s = s.replace('src="%s"'%k, 'src="%s"'%uri)
open(jp,"w",encoding="utf-8").write(s)
print("join.html inlined ->", "assets/" in s)
