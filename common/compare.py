from csv_diff import load_csv, compare
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def compare_csvs(input_file, output_file):
    diff = compare(
        load_csv(open(input_file)),
        load_csv(open(output_file))
    )
    print(diff)
