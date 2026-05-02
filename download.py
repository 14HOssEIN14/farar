import os
import zipfile
from moabb.datasets import BNCI2014_001
from mne import create_info

def download_and_save():
    print("شروع دانلود دیتاست BNCI2014_001...")
    dataset = BNCI2014_001()
    
    # دانلود همه 9 سوژه
    dataset.download(subject_ids=[1,2,3,4,5,6,7,8,9])
    
    # پیدا کردن مسیر ذخیره شده دیتاست
    data_path = dataset.data_path(subject=1)
    
    # مسیر پوشه اصلی دیتاست
    base_path = os.path.dirname(data_path)
    while not os.path.basename(base_path).startswith('MNE'):
        base_path = os.path.dirname(base_path)
    
    print(f"دیتاست در این مسیر ذخیره شده: {base_path}")
    
    # زیپ کردن کل پوشه دیتاست
    zip_path = '/home/runner/work/eeg-data.zip'
    print(f"در حال زیپ کردن فایل‌ها به {zip_path}...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(base_path))
                zipf.write(file_path, arcname)
    
    print("دانلود و زیپ با موفقیت انجام شد!")
    return zip_path

if __name__ == "__main__":
    download_and_save()
