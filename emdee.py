import requests 
import hashlib

URI = "http://docker.hackthebox.eu:30774"
PROXIES = {}

def encrypt(ret):
    start = ret.find("<h3 align='center'>") + 19
    end = ret.find("</h3>")
    md5 = ret[start:end].encode('utf-8')
    encrypted_hash = hashlib.md5(md5).hexdigest()
    return encrypted_hash

session = requests.session()
req = session.get(URI, proxies=PROXIES)
md5 = encrypt(req.text)
req = session.post(URI, data={"hash":md5}, proxies=PROXIES)
print(req.text)
