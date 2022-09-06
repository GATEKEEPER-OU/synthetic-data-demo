from synthetic_data.generator.generator import SyntheticDataGenerator
import os
from datetime import datetime

n_patients = 10 # TODO get from the stdin
n_days = 100 # TODO get from the stdin

event_model = 'models/event_model.h5'
timing_model = 'models/timing_model.h5'

events_vocab = 'statics/events_vocab.json'
timings_vocab = 'statics/timings_vocab.json'

codings_file = 'statics/codings.csv'

timestamp = datetime.now()
output_dir = 'out/generated/%d' % timestamp
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
