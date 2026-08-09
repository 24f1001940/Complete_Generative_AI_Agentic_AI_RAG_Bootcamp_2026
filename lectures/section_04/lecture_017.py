"""
Lecture 17: Importing Modules and Packages
Author: MOHD SAQIB
"""

import math
import sys
from datetime import datetime
from pathlib import Path

def inspect_environment():
    return {
        "current_time": datetime.now().isoformat(),
        "script_dir": str(Path(__file__).resolve().parent),
        "python_path_entries": len(sys.path),
        "pi_val": math.pi
    }

if __name__ == "__main__":
    print("Module Inspection:", inspect_environment())