"""
download_and_push.py
Downloads Lee2019_MI dataset and saves it to the repository
"""

from moabb.datasets import Lee2019_MI
from moabb.paradigms import MotorImagery
import pickle
import os

# Create output directory
output_dir = "Lee2019_MI_data"
os.makedirs(output_dir, exist_ok=True)

# Initialize dataset and paradigm
dataset = Lee2019_MI()
paradigm = MotorImagery(
    fmin=8, fmax=30,
    tmin=1.0, tmax=3.5,
    n_classes=2
)

# Download and save data for all subjects
all_data = {}
for subject in range(1, 55):
    try:
        X, y, meta = paradigm.get_data(
            dataset,
            subjects=[subject]
        )
        all_data[subject] = {
            'X': X,
            'y': y,
            'meta': meta
        }
        print(f"Downloaded subject {subject}: {X.shape}")
    except Exception as e:
        print(f"Failed subject {subject}: {e}")

# Save to pickle file
output_file = os.path.join(output_dir, 'lee2019_mi.pkl')
with open(output_file, 'wb') as f:
    pickle.dump(all_data, f)

print(f"Dataset saved to {output_file}")
print(f"Total subjects downloaded: {len(all_data)}")
