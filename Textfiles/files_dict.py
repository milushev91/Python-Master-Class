input_file = "country_info.txt"

with open(input_file) as country_file:
  # readline is iterator so we is completed the for loop will
  #begin from the second line
  country_file.readline()
  countries_dict = {}
  for row in country_file:
    data  = row.rstrip().split("|")
    country, capital, code, code3, dialing, timezone, currency = data
    country_dict = {
      "name": country,
      "capital": capital,
      "country_code": code,
      "cc3": code3,
      "dialing_code": dialing,
      "timezone": timezone,
      "currency": currency
    }
    countries_dict[country.casefold()] = country_dict

country_name = input("Chose country name: ").casefold()

print(countries_dict[country_name]["capital"])

    
