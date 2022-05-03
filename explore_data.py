import csv
from itertools import islice

with open('data.tsv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')

	headers = next(csv_reader)
	#get indexes and names of column headers
	for index, header in enumerate(headers):
		print(index, header)

	#inspect first 10 rows of data 
	for row in islice(csv_reader, 10):
		print(row)

	#Get all data dimensions from the file
	data_dimensions = []
	for row in csv_reader:
		dimension = (row[0])
		data_dimensions.append(dimension)

	print(data_dimensions)

	
#Now we have better understanding of the data file
#and we can clean and visualize data.