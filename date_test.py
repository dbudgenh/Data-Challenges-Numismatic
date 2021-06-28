import datefinder
string_with_dates = """
This coin is from 500 BC.
"""

matches = datefinder.find_dates(string_with_dates)


for match in matches:
    print(match)