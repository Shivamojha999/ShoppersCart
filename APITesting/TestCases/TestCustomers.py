import pytest
from APITesting.ModuleMethods.CommonMethods import CommonMethods
from APITesting.ModuleMethods.Customers import Customers


@pytest.mark.TestClass
class TestCustomers(CommonMethods):

    commonUrl = "/wp-json/wc/v3/customers"

    @pytest.mark.parametrize("firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone", [
        (CommonMethods.alphaStringGenerator(6),CommonMethods.alphaStringGenerator(5),CommonMethods.alphaStringGenerator(10),
         CommonMethods.alphaNumericStringGenerator(8),CommonMethods.alphaNumericStringGenerator(5),CommonMethods.alphaStringGenerator(7),
         CommonMethods.alphaStringGenerator(5),CommonMethods.randomNumberGenerator(2000, 5000),
         CommonMethods.alphaStringGenerator(10),CommonMethods.randomNumberGenerator(2000000000, 5000000000)) ])
    def test_VerifyUserCanCreateCustomer(self,firstName,lastName,company,address_1,address_2,city,state,postcode,country,phone):
        customers = Customers()
        firstName = firstName
        lastName = lastName
        userName = firstName+"."+lastName
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=company,address_1=address_1,address_2=address_2,
                city=city,state=state,postcode=postcode,country=country,email=firstName+lastName+"@gmail.com",phone=phone)
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],address_1=billingData["address_1"],
                address_2=billingData["address_2"],city=billingData["city"],state=billingData["state"],postcode=billingData["postcode"],
                country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,billing=billingData,shipping=shippingData)
        userId = customers.createCustomerAndGetId(self.commonUrl,data,201)
        assert customers.verifySpecificCustomerCreated(self.commonUrl+f"/{userId}",userName,200) is True,\
        f"Failed: verifySpecificCustomerCreated returns False for Name:-{userName} and User Id:-{userId}"

    @pytest.mark.parametrize("firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone", [
        (CommonMethods.alphaStringGenerator(6),CommonMethods.alphaStringGenerator(5),CommonMethods.alphaStringGenerator(10),
         CommonMethods.alphaNumericStringGenerator(8),CommonMethods.alphaNumericStringGenerator(5),CommonMethods.alphaStringGenerator(7),
         CommonMethods.alphaStringGenerator(5),CommonMethods.randomNumberGenerator(2000, 5000),
         CommonMethods.alphaStringGenerator(10),CommonMethods.randomNumberGenerator(2000000000, 5000000000)) ])
    def test_VerifyCreatedCustomerInDataBase(self, firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone):
        customers = Customers()
        userName = f"{firstName}.{lastName}"
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=company,address_1=address_1,address_2=address_2,
            city=city,state=state,postcode=postcode,country=country,email=f"{firstName}{lastName}@gmail.com",phone=phone)
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],address_1=billingData["address_1"],
            address_2=billingData["address_2"],city=billingData["city"],state=billingData["state"],postcode=billingData["postcode"],
            country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,billing=billingData,
            shipping=shippingData)
        userId = customers.createCustomerAndGetId(self.commonUrl, data, 201)
        query = f"select * from wp_wc_customer_lookup where user_id = {userId}"
        customerCreatedInDB = customers.verifySpecificCustomerCreatedInDB(query, userName)
        assert customerCreatedInDB is True, f"Fail: verifySpecificCustomerCreatedInDB returned False for Customer: {userName}"


    def test_VerifyListOfCreatedCustomersInDBAndUsingUrl(self):
        customers = Customers()
        customerList = customers.verifyListOfCustomerDisplayed(self.commonUrl,200)
        assert  customerList is True,f"Failed: verifyListOfCustomerDisplayed returns False as no Customers were present"
        customerListInDB = customers.verifyListOfCustomerPresentInDB("select * from wp_wc_customer_lookup")
        assert  customerListInDB is True,f"Failed: verifyListOfCustomerPresentInDB returns False as no Customers were present in data base"

    @pytest.mark.parametrize("firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone", [
        (CommonMethods.alphaStringGenerator(6),CommonMethods.alphaStringGenerator(5),CommonMethods.alphaStringGenerator(10),
         CommonMethods.alphaNumericStringGenerator(8),CommonMethods.alphaNumericStringGenerator(5),CommonMethods.alphaStringGenerator(7),
         CommonMethods.alphaStringGenerator(5),CommonMethods.randomNumberGenerator(2000, 5000),
         CommonMethods.alphaStringGenerator(10),CommonMethods.randomNumberGenerator(2000000000, 5000000000)) ])
    def test_CustomersCanBeDeletedFromDataBase(self, firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone):
        customers = Customers()
        userName = f"{firstName}.{lastName}"
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=company,address_1=address_1,address_2=address_2,
            city=city,state=state,postcode=postcode,country=country,email=f"{firstName}{lastName}@gmail.com",phone=phone)
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],address_1=billingData["address_1"],
            address_2=billingData["address_2"],city=billingData["city"],state=billingData["state"],postcode=billingData["postcode"],
            country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,billing=billingData,
            shipping=shippingData)
        userId = customers.createCustomerAndGetId(self.commonUrl, data, 201)
        customerCreatedInDB = customers.verifySpecificCustomerCreatedInDB(f"select * from wp_wc_customer_lookup where user_id = {userId}",userName)
        assert customerCreatedInDB is True, f"Fail: verifySpecificCustomerCreatedInDB return False for Customer: {userName}"
        oneRowsAffected = customers.deleteSpecificCustomerFromDB(f"delete from wp_wc_customer_lookup where user_id = {userId}")
        assert oneRowsAffected is True, f"Fail: deleteSpecificCustomerFromDB did not delete customer: {userName}"
        customerNotDeleted = customers.verifySpecificCustomerCreatedInDB(f"select * from wp_wc_customer_lookup where user_id = {userId}",userName)
        assert customerNotDeleted is False, f"Fail: Customer still exists in the database after deletion: {userName}"

    @pytest.mark.parametrize("firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone", [
        (CommonMethods.alphaStringGenerator(6),CommonMethods.alphaStringGenerator(5),CommonMethods.alphaStringGenerator(10),
         CommonMethods.alphaNumericStringGenerator(8),CommonMethods.alphaNumericStringGenerator(5),CommonMethods.alphaStringGenerator(7),
         CommonMethods.alphaStringGenerator(5),CommonMethods.randomNumberGenerator(2000, 5000),
         CommonMethods.alphaStringGenerator(10),CommonMethods.randomNumberGenerator(2000000000, 5000000000)) ])
    def test_VerifyEmailAccountAlreadyExist(self, firstName, lastName, company, address_1, address_2, city, state, postcode, country, phone):
        customers = Customers()
        userName = f"{firstName}.{lastName}"
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=company,address_1=address_1,address_2=address_2,
            city=city,state=state,postcode=postcode,country=country,email=f"{firstName}{lastName}@gmail.com",phone=phone)
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],
            address_1=billingData["address_1"],address_2=billingData["address_2"],city=billingData["city"],
            state=billingData["state"],postcode=billingData["postcode"],country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,
            billing=billingData,shipping=shippingData)
        _ = customers.createCustomerAndGetId(self.commonUrl, data, 201)
        alreadyExistEmail = billingData["email"]
        billingDataNew = self.createDictionary(first_name=firstName,last_name=lastName,company=company,
            address_1=address_1,address_2=address_2,city=city,state=state,postcode=postcode,country=country,email=alreadyExistEmail,phone=phone)
        shippingDataNew = self.createDictionary(first_name=firstName,last_name=lastName,company=billingDataNew["company"],address_1=billingDataNew["address_1"],
            address_2=billingDataNew["address_2"],city=billingDataNew["city"],state=billingDataNew["state"],
            postcode=billingDataNew["postcode"],country=billingDataNew["country"])
        dataNew = self.createDictionary(email=alreadyExistEmail,first_name=firstName,last_name=lastName,username=userName,
            billing=billingDataNew,shipping=shippingDataNew)
        errorMessage = customers.createCustomerAndGetErrorMessage(self.commonUrl, dataNew, 400)
        expectedErrorMessage = "An account is already registered with your email address."
        assert expectedErrorMessage in errorMessage, f"Failed: Expected error message '{expectedErrorMessage}', but got '{errorMessage}'"
