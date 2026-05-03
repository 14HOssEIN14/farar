import os
import shutil
from moabb.datasets import BNCI2014_001
import mne

# مسیر ذخیره‌سازی موقت MOABB (برای اینکه مطمئن بشیم کجاست)
save_path = os.path.join(os.getcwd(), "bnci_data")
mne.utils.set_config('MNE_DATA', save_path, set_env=True)

# این دو خط جادو هستند:
dataset = BNCI2014_001()  # <-- اسم درست دیتاست
dataset.download()       # <-- خودکار دانلود می‌کند

# فایل‌ها الان توی پوشه mne_data/bnci_data هستند
# برای اینکه توی ریپازیتوری باشه، یه کم جابه‌جا می‌کنیم
if os.path.exists("mne_data/bnci_data"):
    shutil.move("mne_data/bnci_data", "BNCI2014_001_dataset")
    print("✅ دیتاست با موفقیت در پوشه 'BNCI2014_001_dataset' ذخیره شد.")
else:
    print("⚠️ یکبار مسیر را بررسی کنید، اما دانلود انجام شده است.")
