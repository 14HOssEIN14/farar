import os
import glob
from moabb.datasets import BNCI2014_001
import mne

# ایجاد پوشه دانلود
os.makedirs('bnci_raw', exist_ok=True)
os.makedirs('bnci_gdf_files', exist_ok=True)

# تنظیم مسیر برای MNE
mne.utils.set_config('MNE_DATA', os.path.abspath('bnci_raw'), set_env=True)

print("در حال دانلود دیتاست...")
dataset = BNCI2014_001()
dataset.download()

# پیدا کردن فایل‌های GDF اصلی
print("جستجوی فایل‌های GDF...")
gdf_files = glob.glob('bnci_raw/**/*.gdf', recursive=True)

if not gdf_files:
    print("فایل GDF پیدا نشد. شاید فرمت .mat باشه. جستجو برای .mat...")
    gdf_files = glob.glob('bnci_raw/**/*.mat', recursive=True)

print(f"تعداد فایل‌ها: {len(gdf_files)}")

# کپی فایل‌ها به پوشه مقصد با اسم ساده
for src in gdf_files:
    fname = os.path.basename(src)
    dst = os.path.join('bnci_gdf_files', fname)
    os.system(f'cp "{src}" "{dst}"')
    print(f"کپی شد: {fname}")

print("همه فایل‌ها آماده‌ی push هستند.")
