from synthetic_data.generator.generator import SyntheticDataGenerator
import os
from datetime import datetime

n_patients = 10 # TODO get from the stdin
n_days = 100 # TODO get from the stdin

event_model = os.path.join('models', 'event_model.h5')
timing_model = os.path.join('models', 'timing_model.h5')

events_vocab = os.path.join('statics', 'events_vocab.json')
timings_vocab = os.path.join('statics', 'timings_vocab.json')

codings_file = os.path.join('statics', 'codings.csv')

timestamp = datetime.now()

# This is the directory that holds the files that are to be evaluated
# Probably need another to hold the "real" files
output_dir = os.path.join('out', 'generated', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(output_dir)

tool = SyntheticDataGenerator(
  event_model, timing_model, events_vocab, timings_vocab, codings_file
)

print("Test one arg")
tool.generate(output_dir, n_patients)
print()

#print("Test two args")
#tool.generate(n_patients, n_days)
#print()
