from synthetic_data.evaluator.evaluator import SyntheticDataEvaluator

import os

dataset = "/a/dataset/path" # TODO get from the stdin
codings_file = os.path.join('statics', 'codings.csv')

timestamp = datetime.now()

# This is the directory that holds the files that are real
real_dir = os.path.join('datasets', 'real', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(real_dir)

# This is the directory that holds the files that are fake
fake_dir = os.path.join('datasets', 'real', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(fake_dir)

# This is the directory that holds reports
report_dir = os.path.join('datasets', 'report', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(report_dir)

tool = SyntheticDataEvaluator(
  codings_file
)

print("Test one arg")
tool.evaluate_processed(dataset, real_dir, fake_dir, report_dir)
print()