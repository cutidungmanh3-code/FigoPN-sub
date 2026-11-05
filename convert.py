import os, re, urllib.request

url = os.environ["SUB_URL"]
olds = [x.strip() for x in os.environ["OLD_DOMAIN"].split(",")]
news = [x.strip() for x in os.environ["NEW_DOMAIN"].split(",")]

pattern = re.compile(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
for d in olds + news:
 if not pattern.match(d):
     raise SystemExit("Ten mien khong hop le (chi duoc ten mien thuan): " + d)

req = urllib.request.Request(url, headers={"User-Agent": "clash-verge/v1.7"})
data = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")

for o, n in zip(olds, news):
 data = data.replace(o, n)

open("out.txt", "w", encoding="utf-8").write(data)
