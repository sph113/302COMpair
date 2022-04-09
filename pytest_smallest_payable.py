import pytest
from tax_cal import cal
import csv

file = open('testdata_smallest_tax.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)

@pytest.mark.parametrize("row", rows)
def test_mpf_output(row):
    cals=cal()
    assert cals.smallest_payable(int(row[0]),int(row[0]))[0] == int(row[2])

