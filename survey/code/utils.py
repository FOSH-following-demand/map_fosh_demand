#!/usr/bin/env python

## How to use:
# utils -i <input-filename> -o <output-filename>
# Example: utils -i input.tsv -o output.csv

import  csv
import argparse


def csv_to_lowercase(filename, output):
    """This function convert uppercase letters to lowercase."""
    
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        table = list(spamreader)
        for idx, row in enumerate(table):
            table[idx] = [item.lower() for item in row]

    output_file = '{}'.format(output)
    writer = csv.writer(open(output_file, 'w'), delimiter='\t') 
    writer.writerows(table)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input filename')
    parser.add_argument('-o', '--output', help='Output filename')
    args = parser.parse_args()

    csv_to_lowercase(args.input, args.output)

