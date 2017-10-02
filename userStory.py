from datetime import datetime
from dateutil.relativedelta import relativedelta
errorList = []

def checkUserStory(individuals, families):

    us03_birth_before_death(individuals)
    us04_marriage_before_divorce(families)

#User story 3 birth should occur before death
def us03_birth_before_death(individuals):

    return_flag = True
    for individual in individuals:
        if individual.death and individual.birthday:
            if individual.death < individual.birthday:
                error_description = individual.id+": Birthday "+str(individual.birthday)+" occurs after death. "+str(individual.death)
                report_error('ERROR: INDIVIDUAL: US03: ', error_description)
                return_flag = False
    return return_flag

#user story 4 marriage should occur before divorce
def us04_marriage_before_divorce(families):
    return_flag = True
    for family in families:
        if family.married and family.divorced:
            if family.married > family.divorced:
                error_description = family.id+" "+family.husbandId+" "+family.wifeId+" Marriage "+str(family.married)+" occurs after divorce "+str(family.divorced)
                report_error('ERROR: FAMILY: US04: ', error_description)
                return_flag = False
    return return_flag


def report_error(errortype, description):

    err = errortype  + description
    errorList.append(err)

def display_error():

    for err in errorList:
        print(err)
