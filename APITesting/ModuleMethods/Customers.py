from APITesting.ModuleMethods.CommonMethods import CommonMethods


class Customers(CommonMethods):

    '''
    created By: Shivam Ojha
    since: 30 July 2024
    desc: This method is used to create Customer And Get Id
    param: url,data,statusCode
    return: String
    '''
    def createCustomerAndGetId(self,url,data,statusCode):
        response = self.post(url,data,statusCode).json()
        return str(response["id"])

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to verify Specific customer Created
    param: url,userName,statusCode
    return: bool
    '''
    def verifySpecificCustomerCreated(self,url,userName,statusCode):
        response = self.get(url,statusCode).json()
        return response["username"] == str(userName)

    '''
    created By: Shivam Ojha
    since: 11 August 2024
    desc: This method is used to verify Specific customer Created in DB
    param: query,userName
    return: bool
    '''
    def verifySpecificCustomerCreatedInDB(self,query,userName):
        dbResponse = self.executeSelectQuery(query)
        if len(dbResponse)>0:
            return str(dbResponse[0]["username"]).__eq__(userName)
        return False

    '''
    created By: Shivam Ojha
    since: 13 August 2024
    desc: This method is used to verify List of customer present
    param: url,statusCode
    return: bool
    '''
    def verifyListOfCustomerDisplayed(self,url,statusCode):
        response = self.get(url,statusCode).json()
        return len(response) > 0

    '''
    created By: Shivam Ojha
    since: 14 August 2024
    desc: This method is used to verify List of customer present in DB
    param: query,userName
    return: bool
    '''
    def verifyListOfCustomerPresentInDB(self,query):
        dbResponse = self.executeSelectQuery(query)
        return len(dbResponse) > 0

    '''
    created By: Shivam Ojha
    since: 14 August 2024
    desc: This method is used to delete Specific Customer From DB
    param: query,rowsAffected
    return: bool
    '''
    def deleteSpecificCustomerFromDB(self,query,rowsAffected=1):
        dbresponse = self.executeNonSelectQuery(query)
        return dbresponse == rowsAffected

    '''
    created By: Shivam Ojha
    since: 21 August 2024
    desc: This method is used to create Customer get error message
    param: url,data,statusCode
    return: String
    '''
    def createCustomerAndGetErrorMessage(self,url,data,statusCode):
        response = self.post(url,data,statusCode).json()
        return str(response["message"])