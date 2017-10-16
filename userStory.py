from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter
errorList = []

def checkUserStory(individuals, families):

    #Sprint 1
    us_01_dates_before_current(individuals, families)
    us_02_birth_before_marriage(individuals, families)
    us03_birth_before_death(individuals)
    us04_marriage_before_divorce(families)
    us07_less_than_150year_old(individuals)
    us_08_birthbefore_marriage_after9monthsdivorce(individuals,families)
    
    #Sprint2
    US05_marriage_before_death(individuals,families)
    US06_divorce_before_death(individuals,families)
    US14_mutiple_birth_5(individuals, families)
    US16_males_same_lastname(individuals, families)
    us10_marriage_after_14yrs(individuals, families)
    us21_correct_gender(individuals, families)

    
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
        ##searching through individuals to get husband and wife
        if family.married:
            for individual in individuals:
                if individual.id==family.husbandId:
                    husband=individual
                if individual.id==family.wifeId:
                    wife=individual
            if wife.alive==False:
                if family.married<wife.death:
                    error_description="Death of Wife"+str(wife.id)+"occurs before marriage."+str(family.married)
                    report_error('ERROR:FAMILY:US05:',error_description)
                    return_flag=False
            if husband.alive==False:
                if family.married>husband.death:
                    error_description="Death of Husband"+str(husband.id)+"occurs before marriage."+str(family.married)
                    report_error('ERROR:FAMILY:US05:',error_description)
                    return_flag=False
    return return_flag

 # User story 6: divorce before death                   
def US06_divorce_before_death(individuals,families):
    return_flag=True
    for family in families:
        if family.divorced :
            for individual in individuals:
                if individual.id==family.husbandId:
                    husband=individual
                if individual.id==family.wifeId:
                    wife=individual
            if wife.alive==False:
                if family.divorced<wife.death:
                    error_description="Death of Wife"+str(wife.id)+"occurs before divorce."+str(family.divorced)
                    report_error('ERROR:FAMILY:US06:',error_description)
                    return_flag=False
                
            if husband.alive==False:
                if family.divorced>husband.death:
                    print(husband)
                    error_description="Death of Husband"+str(husband.id)+"occurs before divorce."+str(family.divorced)
                    report_error('ERROR:FAMILY:US06:',error_description)
                    return_flag=False
    return return_flag

#US14: No more than five siblings should be born at the same time
def US14_mutiple_birth_5(individuals,families):
    return_flag=True
    for family in families:
        siblings_id=family.children
        siblings=list(x for x in individuals if x.id in siblings_id)
        sib_birthday=[]
        for sibling in siblings:
            sib_birthday.append(sibling.birthday)
        result = Counter(sib_birthday).most_common(1)
        for(a,b) in result:
            if b>5:
                error_description = family.id+"More than 5 siblings born at once"
                report_error('ERROR: FAMILY: US14: ' ,error_description)
                return_flag = False
    return return_flag

#US16: All male members of a family should have the same last name
def US16_males_same_lastname(individuals,families):
    return_flag=True
    for family in families:
        if family.married:
            # Search through individuals to get husband and wife
            lastname=family.husbandName[1]
            for individual in individuals:
                id=individual.id
                name=individual.name
                gender=individual.gender
                if id in family.children:
                    if gender == "M":
                        if lastname not in name:
                            error_description = individual.id+" Lastname not the same as father "
                            report_error('ERROR:INDIVIDUAL: US16: ',error_description)
                            return_flag = False

    return return_flag

#US10 - Marriage should be atleast 14 years after the birth of both spouses
def us10_marriage_after_14yrs(individuals, families):

    return_flag = True

    for family in families:
        for individual in individuals:
            if individual.id == family.husbandId:
                husband = individual
            if individual.id == family.wifeId:
                wife = individual

        if husband.age < 14:
            error_description = family.id+" "+husband.id+" Husband is married before age of 14"
            report_error('ANOMALY: FAMILY: US10:',error_description)
            return_flag = False

        if wife.age < 14:
            error_description = family.id + " " + wife.id + " Wife is married before age of 14"
            report_error('ANOMALY: FAMILY: US10:', error_description)
            return_flag = False
    return return_flag

#US21 - Correct Gender for Role; husband should be male, wife should be female
def us21_correct_gender(individuals, families):

    return_flag = True

    for family in families:
        for individual in individuals:
            if individual.id == family.husbandId:
                husband = individual
            if individual.id == family.wifeId:
                wife = individual

        if husband.gender is not "M":
            error_description = family.id+" "+husband.id+" Husband is not a male"
            report_error('ANOMALY: FAMILY: US21: ',error_description)
            return_flag = False

        if wife.gender is not "F":
            error_description = family.id + " " + wife.id + " Wife is not a female"
            report_error('ANOMALY: FAMILY: US21: ', error_description)
            return_flag = False
    return return_flag


                  


def report_error(errortype, description):

    err = errortype  + description
    errorList.append(err)

def display_error():

    for err in errorList:
        print(err)
