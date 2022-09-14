import os
import sys
fpath = os.path.join(os.path.dirname(__file__), "..", "..", "synthetic-data")
fpath = os.path.abspath(fpath)
sys.path.append(fpath)

# We have 3 separate methods. Easier for testing and future decoupling
def main(n_days, dataset):
    from synthetic_data.evaluator.evaluator import SyntheticDataEvaluator
    import os   
    
    codings_dir = os.path.join('statics', '1', 'codings')
    evaluate_dir = os.path.join('statics', '1', 'confidential')
    
    # The generated data
    input_dir = os.path.join('out', 'generated', dataset)

    output_dir = os.path.join('out', 'evaluated_real', dataset)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # This is the directory that holds the processed files
    processed_dir = os.path.join('datasets', 'processed', dataset)
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # This is the directory that holds the files that are real
    real_dir = os.path.join('datasets', 'real', dataset)
    if not os.path.exists(real_dir):
        os.makedirs(real_dir)

    # This is the directory that holds the files that are fake
    fake_dir = os.path.join('datasets', 'fake', dataset)
    if not os.path.exists(fake_dir):
        os.makedirs(fake_dir)

    # This is the directory that holds reports. Should exist.
    report_file = os.path.join('datasets', 'report', dataset + ".csv")
   
    tool = SyntheticDataEvaluator(n_days)

    # Process the generated files
    tool.process_generated(codings_dir, input_dir, processed_dir)

    # Evaluate the processed files
    tool.evaluate_processed(evaluate_dir, processed_dir, real_dir, fake_dir, report_file)

    # Evaluate the processed files
    tool.postprocess_evaluated(real_dir, output_dir)

if __name__ == "__main__":
    # n_days, directory
    main(1, '20220914101527')