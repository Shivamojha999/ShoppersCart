from APITesting.Utils.DBUtils import DBUtils
from APITesting.Utils.RequestUtils import RequestUtil
import random
import string


class CommonMethods(RequestUtil,DBUtils):

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to create Dictionary
    param: dictParameters (Keys=Value)
    return: dict
    '''
    def createDictionary(self,**kwargs):
        return kwargs

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to generate alpha Numeric String
    param: length
    return: string
    '''
    @classmethod
    def alphaNumericStringGenerator(self,length):
        char = string.ascii_letters+string.digits
        randomString = "".join(random.choices(char,k=length))
        return randomString

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to generate alphabetical String
    param: length
    return: string
    '''
    @classmethod
    def alphaStringGenerator(self,length):
        char = string.ascii_uppercase + string.ascii_lowercase
        randomString = "".join(random.choices(char,k=length))
        return randomString

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to generate Numeric String
    param: lowerLimit, upperLimit
    return: string
    '''
    @classmethod
    def randomNumberGenerator(self,lowerLimit,upperLimit):
        number = round(random.uniform(lowerLimit,upperLimit),2)
        return str(number)

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to generate boolean String
    param: none
    return: string
    '''
    def randomBooleanGenerator(self):
        randomValue = random.random()
        return str(randomValue < 0.5).lower()

    '''
    created By: Shivam Ojha
    since: 11 August 2024
    desc: This method is used to execute Select Query
    param: selectQuery
    return: list of dict
    '''
    def executeSelectQuery(self,selectQuery):
        dbResponse = self.executeSelectSqlQuery(selectQuery)
        return dbResponse

    '''
    created By: Shivam Ojha
    since: 14 August 2024
    desc: This method is used to execute Non Select Query
    param: nonSelectQuery
    return: int
    '''
    def executeNonSelectQuery(self,nonSelectQuery):
        return self.executeNonSelectSqlQuery(nonSelectQuery)