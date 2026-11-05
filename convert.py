import os, urllib.request

url = os.environ["SUB_URL"]
olds = os.environ["OLD_DOMAIN"].split(",")
news = os.environ["NEW_DOMAIN"].split(",")

req = urllib.request.Request(url, headers={"User-Agent": "clash-verge/v1.7"})
data = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")

for o, n in zip(olds, news):
   data = data.replace(o.strip(), n.strip())

open("out.txt", "w", encoding="utf-8").write(data)
