import os
from moabb.datasets import Lee2019_MI
import mne

# Set path for MNE data
os.environ['MNE_DATA'] = os.path.join(os.getcwd(), 'mne_data')

print("=" * 60)
print("Downloading Lee2019_MI Dataset")
print("=" * 60)

# Create dataset instance
dataset = Lee2019_MI()

# Download all subjects (54 subjects)
print("\n1. Downloading dataset (54 subjects, 2 sessions each)...")
print("   This may take a while due to large file sizes.")
dataset.download()

print("\n2. Verifying download...")
# Check data for first subject
raw = dataset._get_single_subject_data(1)['session_0']['run_0']
print(f"   Sample data shape: {raw.get_data().shape}")
print(f"   Sampling frequency: {raw.info['sfreq']} Hz")
print(f"   Number of channels: {len(raw.ch_names)}")

print("\n✅ Download complete!")
print(f"   Data saved to: {os.environ['MNE_DATA']}")
