validTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for tag line in gedcom file
class gedcomLineClass(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        gedLineList = line.split(' ',)
        self.level = int(gedLineList[0])
        if self.level > 0:
            self.tag = gedLineList[1]
            self.arg = gedLineList[2:]
        if self.level == 0:
            if gedLineList[1] in validTags:
                self.tag = gedLineList[1]
                self.arg = None
            else:
                self.tag = gedLineList[2]
                self.ref = gedLineList[1]


# class for individuals
class individualsClass(object):

    def __init__(self, id):
        self.id = id
        self.name = None
        self.gender = None
        self.birthday = None
        self.age = None
        self.alive = True
        self.death = None
        self.child = []
        self.spouse = []

# class for families
class familiesClass(object):

    def __init__(self, id):
        self.id = id
        self.married = None
        self.divorced = None
        self.husbandId = None
        self.husbandName = None
        self.wifeId = None
        self.wifeName = None
        self.children = []
