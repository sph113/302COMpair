import pytest
from tax_cal import cal
import csv

file = open('testdata_all.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
singlerows = []
jointrows = []
for row in csvreader:
    if row[1] == "":
        singlerows.append(row)
    elif not row[1] == "":
        jointrows.append(row)
print(singlerows)
print(jointrows)

@pytest.mark.parametrize("row", singlerows)
def test_single_input(row):
    cals=cal()
    assert cals.single(int(row[0]))[0] == int(row[0])

@pytest.mark.parametrize("row", singlerows)
def test_single_mpf(row):
    cals=cal()
    assert cals.single(int(row[0]))[1] == int(row[2])


@pytest.mark.parametrize("row", singlerows)
def test_single_basic(row):
    cals=cal()
    assert cals.single(int(row[0]))[2] == int(row[5])


@pytest.mark.parametrize("row", singlerows)
def test_single_net(row):
    cals=cal()
    assert cals.single(int(row[0]))[3] == int(row[8])

@pytest.mark.parametrize("row", singlerows)
def test_single_tax(row):
    cals=cal()
    assert cals.single(int(row[0]))[4] == int(row[11])

#-------------------------------Joint-------------------------------------------

@pytest.mark.parametrize("row", jointrows)
def test_joint_self_input(row):
    cals=cal()
    assert cals.single(int(row[0]))[0] == int(row[0])

@pytest.mark.parametrize("row", jointrows)
def test_joint_spouse_input(row):
    cals=cal()
    assert cals.single(int(row[1]))[0] == int(row[1])

@pytest.mark.parametrize("row", jointrows)
def test_joint_self_mpf(row):
    cals=cal()
    assert cals.single(int(row[0]))[1] == int(row[2])

@pytest.mark.parametrize("row", jointrows)
def test_joint_spouse_mpf(row):
    cals=cal()
    assert cals.single(int(row[1]))[1] == int(row[3])

@pytest.mark.parametrize("row", jointrows)
def test_joint_mpf(row):
    cals=cal()
    assert cals.joint(int(row[0]),int(row[1]))[1] == int(row[4])

@pytest.mark.parametrize("row", jointrows)
def test_joint_self_basic(row):
    cals=cal()
    assert cals.single(int(row[0]))[2] == int(row[5])

@pytest.mark.parametrize("row", jointrows)
def test_joint_spouse_basic(row):
    cals=cal()
    assert cals.single(int(row[1]))[2] == int(row[6])

@pytest.mark.parametrize("row", jointrows)
def test_joint_basic(row):
    cals=cal()
    assert cals.joint(int(row[0]),int(row[1]))[2] == int(row[7])

@pytest.mark.parametrize("row", jointrows)
def test_joint_self_net(row):
    cals=cal()
    assert cals.single(int(row[0]))[3] == int(row[8])

@pytest.mark.parametrize("row", jointrows)
def test_joint_spouse_net(row):
    cals=cal()
    assert cals.single(int(row[1]))[3] == int(row[9])

@pytest.mark.parametrize("row", jointrows)
def test_joint_net(row):
    cals=cal()
    assert cals.joint(int(row[0]),int(row[1]))[3] == int(row[10])


@pytest.mark.parametrize("row", jointrows)
def test_joint_self_tax(row):
    cals=cal()
    assert cals.single(int(row[0]))[4] == int(row[11])

@pytest.mark.parametrize("row", jointrows)
def test_joint_spouse_tax(row):
    cals=cal()
    assert cals.single(int(row[1]))[4] == int(row[12])

@pytest.mark.parametrize("row", jointrows)
def test_joint_tax(row):
    cals=cal()
    assert cals.joint(int(row[0]),int(row[1]))[4] == int(row[13])