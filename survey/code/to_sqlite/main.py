#!/usr/bin/env python

import os
import csv
import argparse
import json
import sqlite3

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'

GENDER_POSITION = 1
AGE_POSITION = 2

STATE_POSITION = 4

header = [
    'response_id',
    'date_submitted',
    'last_page',
    'language',
    'gender',
    'city',
    'state',
    'country',
    'formation',
    'highest_degree',
    'affiliated_institutions',
    'institution',
    'academic_occupation',
    'main_work_area',
    'working_years',
    'equipment_situation',
    'explain_equipment',
    'situation',
    'the_biggest_difficulty_in_equipment_access',
    'tools_are_most_used_in_your_lab',
    'second_tools_are_most_used_in_your_lab',
    'third_tools_are_most_used_in_your_lab',
    'question_1',
    'question_2',
    'question_3',
    'question_4',
    'question_5',
    'question_6',
    'question_7',
    'question_8',
    'question_9',
    'question_10',
    'question_11',
    'question_12',
    'question_13',
    'question_14',
    'question_15',
    'question_16',
    'question_17',
    'question_18',
    'question_19',
    'question_20',
    'question_21',
    'question_22',
    'question_23',
    'question_24',
    'question_25',
    'question_26',
    'question_27',
    'question_28',
    'question_29',
    'question_30',
    'question_31',
    'question_32',
    'question_33',
    'question_34',
    'question_35',
    'question_36',
    'question_37',
    'question_38',	
    'question_39',
    'question_40',
    'question_41',
    'question_42',
    'question_43',
    'question_44',
    'question_45',
    'question_46',
    'question_47',
    'question_48',
    'question_49',
    'question_50',
    'question_51',
    'question_52',
    'question_53',
    'question_54',
    'question_55',
    'question_56',
    'question_57',
    'question_58',
    'question_59',
    'question_60',
    'question_61',
    'question_62',
    'question_63',
    'question_64',
    'question_65',
    'question_66',
    'question_67',
    'question_68',
    'question_69',
    'question_70',
    'question_71',
]


def grab_header(filename):
    with open(filename, newline='') as csvfile:
        #dialect = csv.Sniffer().sniff(csvfile.read(1024))
        #csvfile.seek(0)
        #spamreader = csv.reader(csvfile, dialect)
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for index,row in enumerate(spamreader):
            if index==0:
                header = row
        
        return header
        

def csv_to_lowercase(filename, output):
    """This function convert uppercase letters to lowercase."""
    
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        table = list(spamreader)
        for idx, row in enumerate(table):
            table[idx] = [item.lower() for item in row]

    output_file = '{}'.format(output)
    writer = csv.writer(open(output_file, 'w'), delimiter='\t', quotechar='"') 
    writer.writerows(table)


def populate(filename):
    """This function convert uppercase letters to lowercase."""

    l = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        table = list(spamreader)
        for idx, row in enumerate(table):
            print(
                f'Index: {idx} {json.dumps(dict(zip(header, row)), indent=4) }')
            print()
            print(len(row))
            l.append(tuple(row))
    return l
    
    

conn = sqlite3.connect('survey.db')
c = conn.cursor()

#c.execute('drop table survey')
#c.execute('''CREATE TABLE survey
#            (response_id text,date_submitted text,last_page text,language text,gender text,city text,state text,country text,formation text,highest_degree text,affiliated_institutions text,institution text,academic_occupation text,main_work_area text,working_years text,equipment_situation text,explain_equipment text,situation text,the_biggest_difficulty_in_equipment_access text,tools_are_most_used_in_your_lab text,second_tools_are_most_used_in_your_lab text,third_tools_are_most_used_in_your_lab text,question_1 text,question_2 text,question_3 text,question_4 text,question_5 text,question_6 text,question_7 text,question_8 text,question_9 text,question_10 text,question_11 text,question_12 text,question_13 text,question_14 text,question_15 text,question_16 text,question_17 text,question_18 text,question_19 text,question_20 text,question_21 text,question_22 text,question_23 text,question_24 text,question_25 text,question_26 text,question_27 text,question_28 text,question_29 text,question_30 text,question_31 text,question_32 text,question_33 text,question_34 text,question_35 text,question_36 text,question_37 text,question_38 text,question_39 text,question_40 text,question_41 text,question_42 text,question_43 text,question_44 text,question_45 text,question_46 text,question_47 text,question_48 text,question_49 text,question_50 text,question_51 text,question_52 text,question_53 text,question_54 text,question_55 text,question_56 text,question_57 text,question_58 text,question_59 text,question_60, question_61 text,question_62 text,question_63, question_64 text,question_65 text,question_66, question_67 text,question_68 text,question_69 text,question_70 text,question_71 text)''')

data = populate('output.tsv')
#c.executemany('INSERT INTO survey VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
#conn.commit()

for row in c.execute('SELECT * FROM survey WHERE country == "france" '):
    print(row)
    print('ROW --------------------------------------------------')
    
conn.close()



#if __name__ == '__main__':
#    csv_to_lowercase('results_september_march_without_identifiers.tsv', 'output.tsv')
