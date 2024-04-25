from pathlib import Path
import numpy as np

data_fp = Path(__file__).parent / "data/trial_zero.npy"
data = np.load(data_fp)
breakpoint()
