import  csv

def csv_to_lowercase(filename):

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        table = list(spamreader)
        for idx, row in enumerate(table):
            table[idx] = [item.lower() for item in row]
    writer = csv.writer(open('output.csv', 'w'), delimiter='\t') 
    writer.writerows(table)


if __name__ == '__main__':
    csv_to_lowercase('RdP_FOSH_20180923_form_responses_1_english.tsv')

        