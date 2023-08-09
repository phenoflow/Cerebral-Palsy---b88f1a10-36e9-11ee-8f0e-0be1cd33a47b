# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"38Gw.00","system":"readv2"},{"code":"F23..14","system":"readv2"},{"code":"F23y300","system":"readv2"},{"code":"F2Bz.00","system":"readv2"},{"code":"100627.0","system":"med"},{"code":"104498.0","system":"med"},{"code":"104580.0","system":"med"},{"code":"104654.0","system":"med"},{"code":"104775.0","system":"med"},{"code":"104782.0","system":"med"},{"code":"104828.0","system":"med"},{"code":"105133.0","system":"med"},{"code":"107551.0","system":"med"},{"code":"107844.0","system":"med"},{"code":"12666.0","system":"med"},{"code":"15530.0","system":"med"},{"code":"16956.0","system":"med"},{"code":"16977.0","system":"med"},{"code":"2019.0","system":"med"},{"code":"2069.0","system":"med"},{"code":"21249.0","system":"med"},{"code":"21548.0","system":"med"},{"code":"25324.0","system":"med"},{"code":"25570.0","system":"med"},{"code":"27966.0","system":"med"},{"code":"28306.0","system":"med"},{"code":"33925.0","system":"med"},{"code":"37160.0","system":"med"},{"code":"39971.0","system":"med"},{"code":"42406.0","system":"med"},{"code":"45551.0","system":"med"},{"code":"48126.0","system":"med"},{"code":"49967.0","system":"med"},{"code":"52659.0","system":"med"},{"code":"53178.0","system":"med"},{"code":"53755.0","system":"med"},{"code":"5512.0","system":"med"},{"code":"55593.0","system":"med"},{"code":"5560.0","system":"med"},{"code":"61219.0","system":"med"},{"code":"64561.0","system":"med"},{"code":"66314.0","system":"med"},{"code":"73943.0","system":"med"},{"code":"90520.0","system":"med"},{"code":"92598.0","system":"med"},{"code":"95132.0","system":"med"},{"code":"99040.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cerebral-palsy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cerebral-palsy---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cerebral-palsy---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cerebral-palsy---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
