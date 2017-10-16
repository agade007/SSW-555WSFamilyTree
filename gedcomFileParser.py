from datetime import date
from datetime import datetime
from classModels import gedcomLineClass, individualsClass, familiesClass
import math

# Function to Parse the GEDCOM file
def GEDCOMFileParser(filename):
    listOfIndividuals = []
    listOfFamilies = []
    gedlist = []
    f = open(filename)
    lines = [line.rstrip('\n\r') for line in f]

    for line in lines:
        current_gedcom = gedcomLineClass(line)
        gedlist.append(current_gedcom)

    for index, gedcomline in enumerate(gedlist):
        #for storing individual person details
        if gedcomline.tag == 'INDI':
            date_type = None
            individualsClassObject = individualsClass(gedcomline.ref)
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    individualsClassObject.name = gedline.arg
                if gedline.tag == "SEX":
                    individualsClassObject.gender = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    individualsClassObject.child.append(gedline.arg[0])
                if gedline.tag == "FAMS":
                    individualsClassObject.spouse.append(gedline.arg[0])
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        individualsClassObject.birthday = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        birthDate = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        age = (datetime.today().date() - birthDate).days / 365
                        individualsClassObject.age = math.floor(age)
                        date_type = None
                    elif date_type == 'DEAT':
                        individualsClassObject.death = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        individualsClassObject.alive = False
                        date_type = None
            listOfIndividuals.append(individualsClassObject)

        # For storing family details
        if gedcomline.tag == 'FAM':

            date_type = None
            familyObject = familiesClass(gedcomline.ref)
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husbandId = gedline.arg[0]
                    for persons in listOfIndividuals:
                        if persons.id == gedline.arg[0]:
                            familyObject.husbandName = persons.name
                if gedline.tag == "WIFE":
                    familyObject.wifeId = gedline.arg[0]
                    for persons in listOfIndividuals:
                        if persons.id == gedline.arg[0]:
                            familyObject.wifeName = persons.name
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])
                if gedline.tag == "DATE":
                    if date_type == "MARR":
                        familyObject.married = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
                    elif date_type == "DIV":
                        familyObject.divorced = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
            listOfFamilies.append(familyObject)

    f.close()
    return listOfIndividuals, listOfFamilies
