import requests
import os
import shutil
import zipfile
import io

url = "https://github.com/sccn/biosig/archive/refs/heads/master.zip"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Downloading from GitHub...")
r = requests.get(url, headers=headers, allow_redirects=True)

print("Extracting files...")
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(".")

# تغییر نام پوشه به چیزی ساده
if os.path.exists("biosig-master"):
    shutil.rmtree("biosig", ignore_errors=True)
    os.rename("biosig-master", "biosig")
    print("✅ Renamed folder to 'biosig'")

print("Done! Files in repo:")
for item in os.listdir("."):
    if "biosig" in item.lower():
        print(f"  - {item}")
