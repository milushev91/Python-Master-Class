import csv

csv_filename = "OlympicMedals2020.csv"
# newline="" prevents blank lines between rows when using Windows
# newline defaults to None on non-Windows platforms
# so you adivisable to use to make your code cross-platform
with open(csv_filename, 'r', encoding="utf-8", newline="") as csv_file:

  headers = csv_file.readline().rstrip().split(",")
  print(f"Column headers: {headers}")
  # reader() returns an iterator that yields one row at a time from the CSV file
  # each row is a list of strings, one for each field in the row
  reader =  csv.reader(csv_file)

  for row in reader:
     print(row)
  
