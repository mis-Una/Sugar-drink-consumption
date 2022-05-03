import csv
from itertools import islice

#Opens the data file
with open('data.tsv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')

	#gets indexes and names of column headers
	headers = next(csv_reader)
	for index, header in enumerate(headers):
		print(index, header)

	#prints first 10 rows of data 
	for row in islice(csv_reader, 10):
		print(row)

	#prints all data dimensions(data by age group, education etc.) from the file
	data_dimensions = []
	for row in csv_reader:
		dimension = (row[0])
		data_dimensions.append(dimension)

	print(data_dimensions)

	
#Now we have better understanding of the data file
#and we can clean, group and visualize data.