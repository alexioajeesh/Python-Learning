import csv

with open('names.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    with open('new_names.csv', 'w', newline='') as new_file:
        fieldnames = ["first_name", "last_name"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t', extrasaction='ignore')
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow(row)
