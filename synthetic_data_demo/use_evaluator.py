import os
import sys
fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

from synthetic_data.evaluator.evaluator import SyntheticDataEvaluator

from datetime import datetime

n_days = 1 # TODO get from the stdin
# dataset = '' N # TODO get from the stdin. Not sure about this

dataset_dir = os.path.join('datasets', 'processed')

timestamp = datetime.now()

# This is the directory that holds the files that are real
real_dir = os.path.join('datasets', 'real', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(real_dir)

# This is the directory that holds the files that are fake
fake_dir = os.path.join('datasets', 'fake', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(fake_dir)

# This is the directory that holds reports
report_file = os.path.join('datasets', 'report',timestamp.strftime('%Y%m%d%H%M%S') + ".csv")

tool = SyntheticDataEvaluator(n_days = n_days)

tool.evaluate_processed(dataset_dir, real_dir, fake_dir, report_file)

# Simulation of file transfer.
#
#real_dir = os.path.join('C:\\Users\\abe29\\SAM-GK-SYSTEM\\code2\\synthetic-data-demo\\datasets\\real\\20220909100943')
print('Transfering files to shared....')
transfer_dir = os.path.join('transfer', 'evaluated')
tool.transfer(real_dir, transfer_dir)
print('End of files transfer')