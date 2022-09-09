import os
import sys
fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

from synthetic_data.shared.shared import SyntheticDataShared

from datetime import datetime

timestamp = datetime.now()

# This is the directory that holds the transferred files that are to be evaluated
input_dir = os.path.join('transfer', 'generated')

# This is the directory that holds the processed files that are to be evaluated
output_dir = os.path.join('transfer', 'processed', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(output_dir)

tool = SyntheticDataShared()

# Process the generated files for evaluation
tool.process_generated(input_dir, output_dir)

# Simulation of file transfer.
#
print('Transfering files to evaluator....')
transfer_dir = os.path.join('datasets', 'processed')
tool.transfer(output_dir, transfer_dir)
print('End of files transfer')