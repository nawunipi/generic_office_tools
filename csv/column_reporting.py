import csv

def order_columns(row):
    return (row['Column1'], row['Column2'], row ['Ownership'], '', '')

result = []

# Open the CSV file
with open('', 'r') as file:
    for row in csv.DictReader(file):
        if row['PrintRow'] == 'True':
            output_row = order_columns(row)
            result.append(output_row)
        else:
            pass
    
with open('', 'w', newline='') as file:
    writer = csv.writer(file)

    header = ('Column1','Column2','Ownership','Date Initiated','Status of Contract')
    writer.writerow(header)
    
    # Write each tuple as a row in the CSV file
    for item in result:
        writer.writerow(item)