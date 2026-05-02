import os
import zipfile
import sys
import traceback

print(f"Python version: {sys.version}")
print("در حال导入 کتابخانه‌ها...")

try:
    from moabb.datasets import BNCI2014_001
    print("✓ moabb imported successfully")
except Exception as e:
    print(f"✗ Error importing moabb: {e}")
    traceback.print_exc()
    sys.exit(1)

def download_and_save():
    print("\nشروع دانلود دیتاست BNCI2014_001...")
    dataset = BNCI2014_001()
    
    try:
        # دانلود فقط ۲ سوژه اول برای تست سریع
        dataset.download(subject_ids=[1, 2])
        print("✓ Download completed successfully")
    except Exception as e:
        print(f"✗ Download failed: {e}")
        traceback.print_exc()
        return None
    
    # پیدا کردن مسیر ذخیره شده
    try:
        data_path = dataset.data_path(subject=1)
        print(f"Data path: {data_path}")
        
        # مسیر اصلی
        base_path = os.path.dirname(os.path.dirname(data_path))
        print(f"Base path: {base_path}")
        
        # ساخت زیپ ساده در مسیر فعلی
        zip_path = os.path.join(os.getcwd(), 'eeg-data.zip')
        print(f"Creating zip at: {zip_path}")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(base_path))
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        
        print(f"✓ Zip created successfully: {zip_path}")
        return zip_path
        
    except Exception as e:
        print(f"✗ Error during zip creation: {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = download_and_save()
    if result:
        print(f"\n✅ SUCCESS: Dataset saved to {result}")
    else:
        print("\n❌ FAILED: Could not download dataset")
        sys.exit(1)
