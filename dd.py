import requests
import os
import sys
import tarfile
import zipfile

def download_biosig_plugin(output_dir="plugins"):
    """
    Downloads BIOSIG plugin for EEGLAB from official SourceForge repository.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    # لینک مستقیم و درست از SourceForge
    url = "https://sourceforge.net/projects/biosig/files/BioSig%20for%20Octave%20and%20Matlab/biosig4octmat-latest.tar.gz/download"
    
    output_path = os.path.join(output_dir, "biosig4octmat.tar.gz")
    
    print(f"Downloading from: {url}")
    print(f"Saving to: {output_path}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    progress = (downloaded / total_size) * 100
                    print(f"\rProgress: {progress:.1f}%", end='')
        
        print(f"\nDownload completed successfully!")
        
        # استخراج فایل tar.gz
        import gzip
        import shutil
        
        extract_path = os.path.join(output_dir, "biosig")
        os.makedirs(extract_path, exist_ok=True)
        
        with tarfile.open(output_path, "r:gz") as tar:
            tar.extractall(extract_path)
        
        print(f"Extracted to: {extract_path}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_biosig_plugin()
