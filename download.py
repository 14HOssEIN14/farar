import os
import sys
from moabb.datasets import BNCI2014_001

print("در حال دانلود دیتاست BNCI2014_001...")
dataset = BNCI2014_001()

# دانلود همه سوژه‌ها
dataset.download()
print("✅ دانلود انجام شد")

# فقط مسیر ذخیره شده را نشان بده
import mne
data_path = mne.get_config('MNE_DATA', default='/home/runner/mne_data')
print(f"\nدیتاست در این مسیر ذخیره شد: {data_path}")

# بررسی وجود فایل‌ها
for root, dirs, files in os.walk(data_path):
    for file in files:
        if file.endswith('.mat'):
            print(f"  ✓ {file}")
