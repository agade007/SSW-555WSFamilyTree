import sys
from gedcomFileParser import GEDCOMFileParser
from userStory import checkUserStory , display
from prettytable import PrettyTable
fileName = 'falsetree.ged'

x = PrettyTable()
y = PrettyTable()

def main():
    individual, families = GEDCOMFileParser(fileName)
    checkUserStory(individual, families)
    displayData(individual, families)
    print()
    display()


def displayData(individual, families):

    # displaying data for individuals
    x.field_names = ["id","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        x.add_row(attrs.values())
    print("Individuals: ")
    print(x)

    # displaying data for families
    y.field_names = ["id","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]
    for line in families:
        attrs = vars(line)
        y.add_row(attrs.values())
    print("Families: ")
    print(y)

if __name__ == '__main__':
    sys.stdout = open("output.txt","w")
    main()
    sys.__stdout__.close()
