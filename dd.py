import requests
import os
import zipfile
import io

# لینک‌های احتمالی - اولی رو امتحان کن
urls = [
    "https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_files/biosig4octmat_latest.zip",
    "https://sccn.ucsd.edu/eeglab/plugins/biosig.zip",
    "https://github.com/sccn/biosig/archive/refs/heads/master.zip"
]

for url in urls:
    print(f"Trying: {url}")
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
        print(f"Status: {r.status_code}, Size: {len(r.content)} bytes")
        
        if r.status_code == 200 and len(r.content) > 10000:
            # چک کنه زیپ هست یا نه
            if r.content[:4] == b'PK\x03\x04' or r.content[:4] == b'PK\x05\x06':
                print("Valid ZIP found!")
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(".")
                
                # پیدا کردن پوشه استخراج شده
                for item in os.listdir("."):
                    if os.path.isdir(item) and ("biosig" in item.lower() or "plugin" in item.lower()):
                        if item != "biosig":
                            os.rename(item, "biosig")
                        print(f"✅ Done! Folder: {item} -> biosig")
                        break
                break
            else:
                print("Not a valid ZIP file")
        else:
            print("File too small or not found")
    except Exception as e:
        print(f"Failed: {e}")

print("Finished.")
