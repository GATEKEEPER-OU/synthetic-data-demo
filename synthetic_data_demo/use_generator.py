import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)


def main(n_patients, n_days):
    from synthetic_data.generator.generator import SyntheticDataGenerator
    from datetime import datetime
    import os
    
    model_dir =  os.path.join('models', '1')
    
    timestamp = datetime.now()

    # This is the directory that holds the files that are to be evaluated
    output_dir = os.path.join('out', 'generated', timestamp.strftime('%Y%m%d%H%M%S'))
    os.makedirs(output_dir)

    tool = SyntheticDataGenerator(n_patients, n_days)

    print("Generating Data")
    tool.generate(output_dir, model_dir)
    print()

if __name__ == "__main__":
    # n_patients, n_days
    # The UX is out of scope
    main(5, 5)
