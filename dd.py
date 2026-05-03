import requests
import os
import zipfile
import io

url = "https://sccn.ucsd.edu/eeglab/plugins/Biosig3.8.5.zip"

print("Downloading 80MB file...")
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
r.raise_for_status()

print(f"Downloaded: {len(r.content) / (1024*1024):.1f} MB")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall(".")
    
for item in os.listdir("."):
    if "Biosig" in item and os.path.isdir(item):
        if item != "biosig":
            os.rename(item, "biosig")
        print(f"✅ Created folder: {item} -> biosig")
        
print("Done.")
