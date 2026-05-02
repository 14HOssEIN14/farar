import os
import zipfile
import sys
from moabb.datasets import BNCI2014_001

print(f"Python version: {sys.version}")
print("در حال بارگذاری کتابخانه‌ها...")

def download_and_save():
    print("\nشروع دانلود دیتاست BNCI2014_001...")
    dataset = BNCI2014_001()
    
    # روش صحیح در نسخه جدید moabb
    # ابتدا همه سوژه‌ها را دانلود می‌کند (بدون آرگومان subject_ids)
    try:
        # دانلود همه سوژه‌ها
        dataset.download()
        print("✓ دانلود انجام شد (همه سوژه‌ها)")
    except Exception as e:
        print(f"خطا در دانلود: {e}")
        return None
    
    # پیدا کردن مسیر ذخیره شده
    try:
        # دریافت مسیر داده‌ها
        data_paths = dataset.data_path()
        if not data_paths:
            print("مسیر داده پیدا نشد!")
            return None
            
        # مسیر اصلی را پیدا می‌کنیم
        base_path = os.path.dirname(os.path.dirname(data_paths[0]))
        print(f"مسیر اصلی: {base_path}")
        
        # ساخت فایل زیپ
        zip_path = os.path.join(os.getcwd(), 'BNCI2014_001_dataset.zip')
        print(f"در حال زیپ کردن به: {zip_path}")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # نام نسبی برای داخل زیپ
                    arcname = os.path.relpath(file_path, os.path.dirname(base_path))
                    zipf.write(file_path, arcname)
                    print(f"  افزوده شد: {os.path.basename(file_path)}")
        
        print(f"✓ زیپ با موفقیت ساخته شد! حجم: {os.path.getsize(zip_path) / (1024*1024):.2f} MB")
        return zip_path
        
    except Exception as e:
        print(f"خطا در ساخت زیپ: {e}")
        return None

if __name__ == "__main__":
    result = download_and_save()
    if result:
        print(f"\n✅ موفقیت! دیتاست در {result} ذخیره شد")
    else:
        print("\n❌ شکست در دانلود دیتاست")
        sys.exit(1)
