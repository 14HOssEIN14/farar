import os
import urllib.request

url = "http://www.bbci.de/competition/iv/download/IV_2a_gdf.zip"
zip_name = "IV_2a_gdf.zip"

# 1. دانلود
print("📥 در حال دانلود...")
urllib.request.urlretrieve(url, zip_name)
print(f"✅ دانلود شد: {zip_name}")

# 2. اسپلیت به قطعات 90 مگ
print("✂️ در حال اسپلیت...")
os.system(f'split -b 90m "{zip_name}" "IV_2a_gdf.zip.part_"')
print("✅ اسپلیت تمام شد")

# 3. لیست قطعات
print("\n📁 قطعات ایجاد شده:")
os.system('ls -lh IV_2a_gdf.zip.part_*')
