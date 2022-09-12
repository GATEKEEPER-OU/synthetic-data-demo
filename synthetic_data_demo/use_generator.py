import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s <n_patients> <n_days>",
        description="Generate data for <n_days> for <n_patients> and send to be evaluated"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 2.0-beta.1"
    )
    parser.add_argument('n_patients', nargs='?', type=int)
    parser.add_argument('n_days', nargs='?', type=int)
    return parser

def run(n_patients, n_days):
    from synthetic_data.generator.generator import SyntheticDataGenerator
    from datetime import datetime

    timestamp = datetime.now()

    # This is the directory that holds the files that are to be evaluated
    output_dir = os.path.join('out', 'generated', timestamp.strftime('%Y%m%d%H%M%S'))
    os.makedirs(output_dir)

    tool = SyntheticDataGenerator(n_patients, n_days)

    print("Generating Data")
    tool.generate(output_dir)
    print()

    # Simulation of file transfer.
    #
    print('Transfering files to shared....')
    transfer_dir = os.path.join('transfer', 'generated')
    tool.transfer(output_dir, transfer_dir)
    print('End of files transfer')

def main():
    parser = init_argparse()
    args = parser.parse_args()
    run(args.n_patients, args.n_days)

if __name__ == "__main__":
    main()