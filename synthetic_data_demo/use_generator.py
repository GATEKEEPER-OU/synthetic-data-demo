import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

from datetime import datetime
from synthetic_data.generator.generator import SyntheticDataGenerator

def main():
  models_dir =  os.path.join('models', '1')

  timestamp = datetime.now()

  # For this demo, this is the directory that holds the files that are to be evaluated
  output_dir = os.path.join('out', 'generator', timestamp.strftime('%Y%m%d%H%M%S'))
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  syntdatag = SyntheticDataGenerator(models_dir)

  print("Generating Data")
  syntdatag.generate(output_dir, 1, 1)
  print()

if __name__ == "__main__":
    main()
