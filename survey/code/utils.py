#!/usr/bin/env python

## How to use:
# utils -i <input-filename> -o <output-filename>
# Example: utils -i input.tsv -o output.csv

import  csv
import argparse

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'

GENDER_POSITION = 1
AGE_POSITION = 2

STATE_POSITION = 4


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


def load_file(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        table = list(spamreader)
    return table


def count_gender(filename):
    male = 0
    female = 0
    for row in load_file(filename):
        gender = row[GENDER_POSITION].strip()
        if gender.lower() == GENDER_MALE:
            male += 1
        elif gender.lower() == GENDER_FEMALE:
            female += 1
        else:
            print('Gender not supported: {}'.format(gender))
    return male, female


def average_age(filename):
    counter = 0
    sum_age = 0
    for row in load_file(filename):
        try:
            age = int(row[AGE_POSITION].strip())
            counter += 1
        except ValueError:
            print('Age not supported: {}'.format(row[AGE_POSITION].strip()))
            continue
        sum_age += age
    return sum_age/counter, counter
        

def count_country(filename):
    return 0


def count_state(filename):
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input filename')
    parser.add_argument('-o', '--output', help='Output filename')
    args = parser.parse_args()

    male, female = count_gender('outtest.tsv')
    print(male, female)
    average, counter = average_age('outtest.tsv')
    print(counter, average)

    #csv_to_lowercase(args.input, args.output)

