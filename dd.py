import requests
import os

url = "https://sourceforge.net/projects/biosig/files/BioSig%20for%20Octave%20and%20Matlab/biosig4octmat-latest.tar.gz/download"

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers, allow_redirects=True)

with open("biosig4octmat-latest.tar.gz", "wb") as f:
    f.write(response.content)

print("Done! File size:", os.path.getsize("biosig4octmat-latest.tar.gz"), "bytes")
