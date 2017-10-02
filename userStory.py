from datetime import datetime
from dateutil.relativedelta import relativedelta
errorList = []

def checkUserStory(individuals, families):

    us03_birth_before_death(individuals)
    us04_marriage_before_divorce(families)
    us07_less_than_150year_old(individuals)
    us_08_birthbefore_marriage_after9monthsdivorce(individuals,families)


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

#user story 7 check if individual lived more than 150 years
def us07_less_than_150year_old(individuals):
    return_flag = True
    today = datetime.now()
    for individual in individuals:

        if individual.alive == False and relativedelta(individual.death, individual.birthday).years > 150:
            error_description = individual.id+" lived longer than 150 years"
            report_error('ANOMALY: INDIVIDUAL: US07: ', error_description)
            return_flag= False
        if individual.alive == True and relativedelta(today,individual.birthday).years > 150:
            error_description = individual.id+" is living longer than 150 years"
            report_error('ANOMALY: INDIVIDUAL: US07:', error_description)
            return_flag = False
    return return_flag

#user story 8 birth before marriage and not after 9 months of divorce
def us_08_birthbefore_marriage_after9monthsdivorce(individuals, families):
    return_flag = True
    for family in families:
        if family.married:
            for individual in individuals:
                id = individual.id
                bday = individual.birthday
                if id in family.children and family.divorced is not None:
                    if bday < family.married:
                        error_description = "Child "+individual.id+" born "+str(individual.birthday)+" before marriage"+str(family.married)
                        report_error('ANOMALY: FAMILY: US08:',error_description)
                        return_flag = False
                    if relativedelta(bday,family.divorced).months+9:
                        error_description="Child "+individual.id+" born "+str(individual.birthday)+" after 9 months of divorce on "+str(family.divorced)
                        report_error('ANOMALY: FAMILY: US08:', error_description)
                        return_flag=False
    return return_flag



def report_error(errortype, description):

    err = errortype  + description
    errorList.append(err)

def display_error():

    for err in errorList:
        print(err)