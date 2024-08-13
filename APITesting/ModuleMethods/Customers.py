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
        return str(dbResponse[0]["username"]).__eq__(userName)