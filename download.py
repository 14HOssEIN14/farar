import os
import zipfile
import sys
import glob

print("در حال پیدا کردن فایل‌های دانلود شده...")

# پیدا کردن همه فایل‌های .mat (دیتاست اصلی)
mat_files = glob.glob('/home/runner/mne_data/**/*.mat', recursive=True)

if not mat_files:
    print("❌ هیچ فایل .mat ای پیدا نشد!")
    sys.exit(1)

print(f"✅ {len(mat_files)} فایل .mat پیدا شد:")

# لیست فایل‌ها را نشان بده
for f in mat_files:
    print(f"  - {os.path.basename(f)}")

# ساخت فایل زیپ
zip_path = os.path.join(os.getcwd(), 'BNCI2014_001_dataset.zip')
print(f"\nدر حال زیپ کردن به: {zip_path}")

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for f in mat_files:
        # ذخیره با نام نسبی ساده
        arcname = os.path.basename(f)
        zipf.write(f, arcname)
        print(f"  ✓ افزوده شد: {arcname}")

zip_size = os.path.getsize(zip_path) / (1024 * 1024)
print(f"\n✅ موفقیت! فایل زیپ ساخته شد.")
print(f"   مسیر: {zip_path}")
print(f"   حجم: {zip_size:.2f} MB")
print(f"   تعداد فایل‌ها: {len(mat_files)}")
