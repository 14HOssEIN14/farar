import requests
import os
import tarfile
import shutil

url = "https://sourceforge.net/projects/biosig/files/BioSig%20for%20Octave%20and%20Matlab/biosig4octmat-latest.tar.gz/download"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Downloading...")
r = requests.get(url, headers=headers, allow_redirects=True)

# ذخیره توی خود ریپازیتوری
with open("biosig.tar.gz", "wb") as f:
    f.write(r.content)

# اکسترکت توی خود ریپازیتوری
print("Extracting...")
with tarfile.open("biosig.tar.gz", "r:gz") as tar:
    tar.extractall(".")

print("Done! فایل‌ها توی ریپازیتوری هستند:")
print(os.listdir("."))
