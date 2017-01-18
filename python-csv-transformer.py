import csv

def CSVTransformer(inputCSV, outputCSV, filterLine, traransformLine, reportingStep=1000):
	with open(inputCSV, newline='', encoding='utf-8') as i, open(outputCSV, 'w', newline='', encoding='utf-8') as o:
		reader = csv.reader(i)
		writer = csv.writer(o, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		count = 0
		for row in reader:
			if filterLine(row):
				newRow = traransformLine(row)
				writer.writerow(newRow)
			count += 1
			if count % reportingStep == 0:
				print(count)

if __name__ == '__main__':
	def traransformLine(row):
		return row

	def filterLine(row):
		return True

	CSVTransformer('original.csv', 'transformed.csv', filterLine, traransformLine)
