import json 
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series"
# urllib.request.urlopen() returns a response object that behaves like a file object containing the data from the URL.
with urllib.request.urlopen(json_data_source) as json_stream:
  # The read() method returns the data as a bytes object.
   # The decode() method converts the bytes object to a string.
  data = json_stream.read().decode("utf-8")
   # The json.loads() function converts the string to a dictionary.
  anomalies = json.load(data)

  print(anomalies["description"])

  for year, value in anomalies["data"].items():
    year, value = int(year), float(value)
    print(f"{year} ... {value:6.2f}")

  print("*" * 80)
  print(anomalies["citation"])
