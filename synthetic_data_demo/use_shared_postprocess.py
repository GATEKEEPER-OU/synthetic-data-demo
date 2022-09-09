import os
import sys
fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

from synthetic_data.shared.shared import SyntheticDataShared

from datetime import datetime

timestamp = datetime.now()

# This is the directory that holds the evaluated files
input_dir = os.path.join('transfer', 'evaluated')

# This is the directory that holds the processed files that are to be evaluated
output_dir = os.path.join('transfer', 'real', timestamp.strftime('%Y%m%d%H%M%S'))
os.makedirs(output_dir)

tool = SyntheticDataShared()

# Process the evaluation files
tool.postprocess_evaluated(input_dir, output_dir)

# These are the files that go to B-B for conversion to FHIR. If there are any issues
# with the contents of the files B-B should contact the Data Scientist for support.
#
# As we have used various temperatures there could be more than 1 file per "user"
# Either select the file with the largest number of obsevations per user,
# Or, each file could be allocated a different user reference. This could be done in a separate method,
# or, in the postprocess_evaluated method.