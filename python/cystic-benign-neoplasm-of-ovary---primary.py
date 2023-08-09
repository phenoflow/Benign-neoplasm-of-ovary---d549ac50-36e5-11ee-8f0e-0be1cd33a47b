# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7E23300","system":"readv2"},{"code":"7E25200","system":"readv2"},{"code":"7E25211","system":"readv2"},{"code":"7E29100","system":"readv2"},{"code":"7E2B000","system":"readv2"},{"code":"B7A..11","system":"readv2"},{"code":"K53..11","system":"readv2"},{"code":"K530.00","system":"readv2"},{"code":"K530.11","system":"readv2"},{"code":"K531.00","system":"readv2"},{"code":"K531100","system":"readv2"},{"code":"K531200","system":"readv2"},{"code":"K531z00","system":"readv2"},{"code":"K532z00","system":"readv2"},{"code":"PC04.00","system":"readv2"},{"code":"ZV13G00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benign-neoplasm-of-ovary-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cystic-benign-neoplasm-of-ovary---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cystic-benign-neoplasm-of-ovary---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cystic-benign-neoplasm-of-ovary---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
