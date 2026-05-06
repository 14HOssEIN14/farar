import os
import requests
import math
from pathlib import Path

def download_file(url, output_path):
    """Download file from URL with progress indicator"""
    print(f"Downloading from {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            downloaded += len(chunk)
            if total_size:
                percent = (downloaded / total_size) * 100
                print(f"\rDownloaded: {percent:.1f}%", end='')
    print(f"\nDownloaded to {output_path}")
    return output_path

def split_file(input_file, chunk_size_mb=50):
    """Split file into chunks of specified size (in MB)"""
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert to bytes
    file_size = os.path.getsize(input_file)
    
    print(f"File size: {file_size / (1024*1024):.2f} MB")
    print(f"Splitting into {chunk_size_mb} MB chunks")
    
    num_chunks = math.ceil(file_size / chunk_size)
    base_name = Path(input_file).stem
    extension = Path(input_file).suffix
    
    chunks = []
    with open(input_file, 'rb') as file:
        for i in range(num_chunks):
            chunk_filename = f"{base_name}.part{i+1:03d}{extension}"
            chunk_path = Path("chunks") / chunk_filename
            chunk_path.parent.mkdir(exist_ok=True)
            
            chunk_data = file.read(chunk_size)
            with open(chunk_path, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            
            chunk_size_mb_actual = len(chunk_data) / (1024*1024)
            print(f"Created: {chunk_filename} ({chunk_size_mb_actual:.2f} MB)")
            chunks.append(str(chunk_path))
    
    # Create manifest file
    manifest = {
        'original_file': input_file,
        'original_size': file_size,
        'chunk_size_mb': chunk_size_mb,
        'num_chunks': num_chunks,
        'chunks': [str(Path(c).name) for c in chunks]
    }
    
    import json
    manifest_path = Path("chunks") / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nCreated manifest: {manifest_path}")
    return chunks

def main():
    # Get file URL from environment variable
    file_url = os.environ.get('FILE_URL')
    if not file_url:
        raise ValueError("FILE_URL environment variable not set")
    
    # Download the file
    filename = file_url.split('/')[-1] or 'downloaded_file'
    downloaded_file = download_file(file_url, filename)
    
    # Split into 50MB chunks
    split_file(downloaded_file, chunk_size_mb=50)
    
    print("\n✅ File split successfully into chunks/ directory")
    
    # Optional: remove original file to save space
    os.remove(downloaded_file)
    print("Original file removed to save space")

if __name__ == "__main__":
    main()
