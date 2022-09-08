from synthetic_data.share.share import SyntheticDataShare
import os
from datetime import datetime

codings_file = os.path.join('statics', 'codings.csv')

timestamp = datetime.now()

# This is the directory that holds the transferred files that are to be evaluated
input_dir = os.path.join('transfer', 'generated')

# This is the directory that holds the processed files that are to be evaluated
output_dir = os.path.join('transfer', 'processeed', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(output_dir)

tool = SyntheticDataShare(
  codings_file
)

# Process the generated files for evaluation
tool.process_generated(input_dir, output_dir)

# Simulation of file transfer.
#
transfer_dir = os.path.join('datasets', 'processed')
tool.transfer(output_dir, transfer_dir)