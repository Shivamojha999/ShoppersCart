import pytest
from APITesting.ModuleMethods.CommonMethods import CommonMethods
from APITesting.ModuleMethods.Customers import Customers


@pytest.mark.TestClass
class TestCustomers(CommonMethods):

    commonUrl = "/wp-json/wc/v3/customers"

    def test_VerifyUserCanCreateCustomer(self):
        customers = Customers()
        firstName = self.alphaStringGenerator(6)
        lastName = self.alphaStringGenerator(5)
        userName = firstName+"."+lastName
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=self.alphaStringGenerator(10),address_1=self.alphaNumericStringGenerator(8),address_2=self.alphaNumericStringGenerator(5),city=self.alphaStringGenerator(7),state=self.alphaStringGenerator(5),postcode=self.randomNumberGenerator(2000,5000),country=self.alphaStringGenerator(10),email=firstName+lastName+"@gmail.com",phone=self.randomNumberGenerator(2000000000,5000000000))
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],address_1=billingData["address_1"],address_2=billingData["address_2"],city=billingData["city"],state=billingData["state"],postcode=billingData["postcode"],country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,billing=billingData,shipping=shippingData)
        userId = customers.createCustomerAndGetId(self.commonUrl,data,201)
        assert customers.verifySpecificCustomerCreated(self.commonUrl+f"/{userId}",userName,200) is True,\
        f"Failed: verifySpecificCustomerCreated returns False for Name:-{userName} and User Id:-{userId}"

    def test_VerifyCreatedCustomerInDataBase(self):
        customers = Customers()
        firstName = self.alphaStringGenerator(6)
        lastName = self.alphaStringGenerator(5)
        userName = firstName+"."+lastName
        billingData = self.createDictionary(first_name=firstName,last_name=lastName,company=self.alphaStringGenerator(10),address_1=self.alphaNumericStringGenerator(8),address_2=self.alphaNumericStringGenerator(5),city=self.alphaStringGenerator(7),state=self.alphaStringGenerator(5),postcode=self.randomNumberGenerator(2000,5000),country=self.alphaStringGenerator(10),email=firstName+lastName+"@gmail.com",phone=self.randomNumberGenerator(2000000000,5000000000))
        shippingData = self.createDictionary(first_name=firstName,last_name=lastName,company=billingData["company"],address_1=billingData["address_1"],address_2=billingData["address_2"],city=billingData["city"],state=billingData["state"],postcode=billingData["postcode"],country=billingData["country"])
        data = self.createDictionary(email=billingData["email"],first_name=firstName,last_name=lastName,username=userName,billing=billingData,shipping=shippingData)
        userId = customers.createCustomerAndGetId(self.commonUrl,data,201)
        customerCreatedInDB = customers.verifySpecificCustomerCreatedInDB(f"select * from wp_wc_customer_lookup where user_id = {userId}",userName)
        assert customerCreatedInDB is True,f"Fail: verifySpecificCustomerCreatedInDB return False for Customer: {userName}"