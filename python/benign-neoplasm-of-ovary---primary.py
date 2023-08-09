# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"B7A2.00","system":"readv2"},{"code":"105462.0","system":"med"},{"code":"11728.0","system":"med"},{"code":"11747.0","system":"med"},{"code":"11937.0","system":"med"},{"code":"15786.0","system":"med"},{"code":"17505.0","system":"med"},{"code":"18639.0","system":"med"},{"code":"20030.0","system":"med"},{"code":"25689.0","system":"med"},{"code":"2979.0","system":"med"},{"code":"33932.0","system":"med"},{"code":"35115.0","system":"med"},{"code":"40033.0","system":"med"},{"code":"40974.0","system":"med"},{"code":"41667.0","system":"med"},{"code":"49824.0","system":"med"},{"code":"49911.0","system":"med"},{"code":"51846.0","system":"med"},{"code":"52995.0","system":"med"},{"code":"53674.0","system":"med"},{"code":"5588.0","system":"med"},{"code":"6251.0","system":"med"},{"code":"6521.0","system":"med"},{"code":"85236.0","system":"med"},{"code":"9380.0","system":"med"},{"code":"957.0","system":"med"},{"code":"958.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benign-neoplasm-of-ovary-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benign-neoplasm-of-ovary---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benign-neoplasm-of-ovary---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benign-neoplasm-of-ovary---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
