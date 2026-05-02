import os
import sys
import glob
from moabb.datasets import BNCI2014_001

print("در حال دانلود دیتاست BNCI2014_001...")
dataset = BNCI2014_001()
dataset.download()
print("✅ دانلود انجام شد")

base_path = '/home/runner/mne_data'
mat_files = glob.glob(f'{base_path}/**/*.mat', recursive=True)

if not mat_files:
    print("❌ فایلی پیدا نشد!")
    sys.exit(1)

print(f"✅ {len(mat_files)} فایل پیدا شد")

os.makedirs('dataset_parts', exist_ok=True)

for mat_file in mat_files:
    file_name = os.path.basename(mat_file)
    base_name = file_name.replace('.mat', '')
    print(f"تقسیم {file_name}...")
    os.system(f'split -b 50m "{mat_file}" "dataset_parts/{base_name}_part_"')

print("✅ همه فایل‌ها تقسیم شدند")
