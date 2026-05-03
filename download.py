"""
prepare_dataset.py
Downloads Lee2019_MI (22 channels, 250Hz, 4s epochs),
zips it, and splits into 100MB chunks for GitHub
"""

from moabb.datasets import Lee2019_MI
from moabb.paradigms import MotorImagery
import numpy as np
import pickle
import os
import zipfile
import shutil

# Settings
OUTPUT_DIR = "Lee2019_MI_dataset"
ZIP_NAME = "Lee2019_MI.zip"
SPLIT_DIR = "Lee2019_MI_splits"
CHUNK_SIZE = 100 * 1024 * 1024  # 100 MB

# Create directories
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SPLIT_DIR, exist_ok=True)

print("Initializing dataset...")
dataset = Lee2019_MI()
paradigm = MotorImagery(
    fmin=4,      # 4 Hz bandpass
    fmax=40,     # 40 Hz bandpass
    tmin=0.0,    # start of trial
    tmax=4.0,    # 4 second epochs
    resample=250 # 250 Hz sampling
)

# Download subject by subject and save individually
print("Downloading subjects...")
for subject in range(1, 55):
    try:
        X, y, meta = paradigm.get_data(
            dataset,
            subjects=[subject]
        )
        
        # Save each subject separately
        subject_file = os.path.join(OUTPUT_DIR, f'subject_{subject:02d}.npz')
        np.savez_compressed(
            subject_file,
            X=X,
            y=y,
            subject=subject
        )
        
        print(f"Subject {subject:02d}/54: {X.shape} - Saved")
        
    except Exception as e:
        print(f"Subject {subject:02d}: FAILED - {e}")

# Also save metadata
meta_file = os.path.join(OUTPUT_DIR, 'metadata.pkl')
with open(meta_file, 'wb') as f:
    pickle.dump({'n_subjects': 54, 'n_classes': 2, 'channels': 22, 'sr': 250}, f)

print("\nCreating zip file...")
# Create zip file
with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, OUTPUT_DIR)
            zipf.write(file_path, arcname)

zip_size = os.path.getsize(ZIP_NAME) / (1024**2)
print(f"Zip created: {zip_size:.2f} MB")

# Split zip into 100MB chunks
print(f"\nSplitting into 100MB chunks...")
with open(ZIP_NAME, 'rb') as f:
    chunk_num = 0
    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:
            break
        chunk_num += 1
        chunk_file = os.path.join(SPLIT_DIR, f'Lee2019_MI.zip.{chunk_num:03d}')
        with open(chunk_file, 'wb') as chunk_f:
            chunk_f.write(chunk)
        chunk_size_mb = len(chunk) / (1024**2)
        print(f"  Chunk {chunk_num:03d}: {chunk_size_mb:.2f} MB")

print(f"\nDone! {chunk_num} chunks created in '{SPLIT_DIR}'")
print("Push these files to GitHub and use merge script to reconstruct.")
