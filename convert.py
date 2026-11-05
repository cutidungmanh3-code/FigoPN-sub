   import os, base64, urllib.request

   url = os.environ["SUB_URL"]
   old = os.environ["OLD_DOMAIN"]
   new = os.environ["NEW_DOMAIN"]

   req = urllib.request.Request(url, headers={"User-Agent": "clash-verge/v1.7"})
   data = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore").strip()

   def is_b64(s):
       try:
           base64.b64decode(s, validate=True)
           return "://" not in s and "proxies" not in s
       except Exception:
           return False

   if is_b64(data):
       text = base64.b64decode(data).decode("utf-8", errors="ignore")
       text = text.replace(old, new)
       out = base64.b64encode(text.encode()).decode()
   else:
       out = data.replace(old, new)

   open("out.txt", "w", encoding="utf-8").write(out)
