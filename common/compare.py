from csv_diff import load_csv, compare
import os

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def compare_csvs(input_file, output_file):



    input_data = []
    try:
        f = open(input_file)
        for line in f:
            data_line = line.rstrip().split('\t')
            input_data.append(data_line)
        f.close()
        print(input_data)
    except Exception as e:
        print("Input file not found : " + str(e))


    try:
        f1 = open(output_file)

        output_data = []
        for line in f1:
            data_line = line.rstrip().split('\t')
            output_data.append(data_line)
        f1.close()
        print(output_data)
    except Exception as e:
        print("Output file not found : " + str(e))

    print("Input file path: " +input_file + " Output file path " + output_file)
    print("Total rows from input file: " + str(len(input_data)))
    print("Total rows from output file: " + str(len(output_data)))

    if len(input_data)== len(output_data):
        print("No. of records in both the files are same")
    else:
        if len(input_data)> len(output_data):
            print("No of records in input file is more than the output file")
        else:
            print("No of records in output file is more than the input file")

    row_success_count = 0
    for i in range(0, len(input_data)):
        try:
            a= str(input_data[i]).replace('[','').replace(']','').replace("'",'').split(',')
            b= str(output_data[i]).replace('[','').replace(']','').replace("'",'').split(',')

            if a ==b :
                row_success_count +=1
            else:
                for j in range(0, len(a)):
                    if a[j] != b[j]:
                        print("Failed - Row No. "+ str(i) + " Column No. " + str(j))
                        print("Expected value: " + a[j] + " | Actual value: " + b[j])
        except Exception as e:
            print("Something went wrong: "+ str(e))

    print("Count of success rows: " + str(row_success_count))
    failed_rows_count = len(input_data)-row_success_count
    print("Count of failed rows: " + str(failed_rows_count))
    assert int(failed_rows_count) == 0, "Output file data doesn't match with inuput file data"





















    # Comparing input\data1.csv with output\data1.csv
    # Total rows from input\data1.csv = 100
    # Total rows from out\data1.csv = 100
    # count of success = 70
    # count of failed = 30
    # details of failed
    # row no :
    # cell no :
    # actual :
    # expected :

