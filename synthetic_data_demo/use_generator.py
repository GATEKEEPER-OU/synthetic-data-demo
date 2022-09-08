import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

from synthetic_data.generator.generator import SyntheticDataGenerator

from datetime import datetime

n_patients = 2 # TODO get from the stdin
n_days = 100 # TODO get from the stdin

codings_file = os.path.join('statics', 'codings.csv')

timestamp = datetime.now()

# This is the directory that holds the files that are to be evaluated
# Probably need another to hold the "real" files
output_dir = os.path.join('out', 'generated', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(output_dir)

tool = SyntheticDataGenerator(
  codings_file
)

print("Test one arg")
tool.generate(output_dir, n_patients)
print()


# Simulation of file transfer.
#
print('Transfering files to shared....')
# output_dir = "C:\\Users\\abe29\\SAM-GK-SYSTEM\\code2\\synthetic-data-demo\\out\\generated\\20220908164424"
transfer_dir = os.path.join('transfer', 'generated')
tool.transfer(output_dir, transfer_dir)
print('End of files transfer')

#print("Test two args")
#tool.generate(n_patients, n_days)
#print()
