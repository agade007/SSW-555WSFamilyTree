from datetime import datetime
from dateutil.relativedelta import relativedelta
errorList = []

def checkUserStory(individuals, families):

    us_01_dates_before_current(individuals, families)
    us_02_birth_before_marriage(individuals, families)
    us03_birth_before_death(individuals)
    us04_marriage_before_divorce(families)
    us07_less_than_150year_old(individuals)
    us_08_birthbefore_marriage_after9monthsdivorce(individuals,families)
    US05_marriage_before_death(individuals,families)
    US06_divorce_before_death(individuals,families)
    
#User story 1 dates are before current date
def us_01_dates_before_current(individuals, families):

    return_flag = True
    for individual in individuals:
        if individual.birthday and individual.birthday > datetime.now().date():
            error_description = "Birth of "+ individual.id+ " occurs after current date"
            report_error('ERROR: INDIVIDUAL: US01: ', error_description)
            return_flag = False

        if individual.death and individual.death > datetime.now().date():
            error_description = "Death of "+individual.id+" occurs after current date"
            report_error('ERROR: INDIVIDUAL: US01: ', error_description)
            return_flag = False

    for family in families:
        if family.married and family.married > datetime.now().date():
            error_description = "In family "+family.id+" marriage of "+family.husbandId+" and "+family.wifeId+" occurs after current date"
            report_error('ERROR: FAMILY: US01: ', error_description)
            return_flag = False

        if family.divorced and family.divorced > datetime.now().date():
            error_description = "In family " +family.id+" divorce of "+ family.husbandId+" and "+family.wifeId+" occurs after current date"
            report_error('ERROR: FAMILY: US01: ', error_description)
            return_flag = False

    return return_flag

#User story 2 birth should be before marriage
def us_02_birth_before_marriage(individuals, families):
    
    return_flag = True
    for family in families:
        if family.married:
            for individual in individuals:
                if individual.id == family.husbandId:
                    husband = individual
                if individual.id == family.wifeId:
                    wife = individual

            if wife.birthday and wife.birthday > family.married:
                error_description = "Birth of wife "+wife.id+" occurs after marriage"
                report_error('ERROR: FAMILY: US02:', error_description)
                return_flag = False

            if husband.birthday and husband.birthday > family.married:
                error_description = "Birth of husband "+husband.id+" occurs after marraige"
                report_error('ERROR: FAMILY: US02: ',error_description)
                return_flag = False

    return return_flag


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
#user story 5:marriage occuring before the death of either spouse
def US05_marriage_before_death(individuals,families):
    return_flag=True
    for family in families:
        if family.married:
            for individual in individuals:
                if family.married and individual.death:
                    if family.married >individual.death:
                        error_description = family.id+" "+" Marriage "+str(family.married)+" occurs before death of either spouse. "+str(individual.death)
                        report_error('ERROR: FAMILY: US05: ', error_description)
                        return_flag = False
    return return_flag
def US06_divorce_before_death(individuals,families):
    return_flag=True
    for family in families:
        if family.married:
            for individual in individuals:
                if family.divorced and individual.death:
                    if family.divorced>individual.death:
                        error_description = family.id+" "+family.husbandId+""+family.wifeId+" Divorced "+str(family.divorced)+" before death of either spouse. "+str(individual.death)
                        report_error('ERROR: FAMILY: US06:', error_description)
                        return_flag = False
    return return_flag                        
                


def report_error(errortype, description):

    err = errortype  + description
    errorList.append(err)

def display_error():

    for err in errorList:
        print(err)
