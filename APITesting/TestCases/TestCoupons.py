import pytest
from APITesting.ModuleMethods.CommonMethods import CommonMethods
from APITesting.ModuleMethods.Coupons import Coupons

@pytest.mark.TestClass
class TestCoupons(CommonMethods):

    commonUrl = "/wp-json/wc/v3/coupons"

    def test_verifyCouponCreated(self):
        coupons = Coupons()
        data = self.createDictionary(code=self.alphaNumericStringGenerator(5),discount_type="percent",amount=self.randomNumberGenerator(1,50),undividual_use=self.randomBooleanGenerator(),exclude_sale_items=self.randomBooleanGenerator(),minimum_amount=self.randomNumberGenerator(100,200))
        couponId = coupons.createNewCouponAndGetId(self.commonUrl,data,201)
        result = coupons.verifySpecificCouponCreated(self.commonUrl+f"/{couponId}",data["code"],200)
        assert result is True, f"Failed: verifySpecificCouponCreated returned False for coupon code {data['code']}"

    def test_VerifyCouponDeleted(self):
        coupons = Coupons()
        data = self.createDictionary(code=self.alphaNumericStringGenerator(5),discount_type="percent",amount=self.randomNumberGenerator(1,50),undividual_use=self.randomBooleanGenerator(),exclude_sale_items=self.randomBooleanGenerator(),minimum_amount=self.randomNumberGenerator(100,200))
        couponId = coupons.createNewCouponAndGetId(self.commonUrl,data,201)
        assert coupons.verifySpecificCouponCreated(self.commonUrl+f"/{couponId}",data["code"],200) is True, \
            f"Failed: verifySpecificCouponCreated returned False for coupon code {data['code']}"
        coupons.deleteSpecificCoupon(self.commonUrl+f"/{couponId}",200)
        assert  coupons.verifySpecificCouponDeleted(self.commonUrl+f"/{couponId}",200) is True, \
            f"Failed: verifySpecificCouponDeleted returned False for coupon code {data['code']}"

    def test_VerifySpecificCouponDeletedFromList(self,coupon=None):
        coupons = Coupons()
        couponList = coupons.getListOfCoupons(self.commonUrl,200)
        if len(couponList) == 0:
            pytest.skip("Skipping test as couponList is empty")
        elif coupon != None:
            couponCode = coupon
        else:
            couponCode = couponList[0]["code"]
        couponId = coupons.getIdOfSpecificCouponCode(couponList,couponCode)
        coupons.deleteSpecificCoupon(self.commonUrl+f"/{couponId}",200)
        assert  coupons.verifySpecificCouponDeleted(self.commonUrl+f"/{couponId}",200) is True, \
            f"Failed: verifySpecificCouponDeleted returned False for coupon code {couponCode}"

    def test_VerifyUserCanUpdateCreatedCoupon(self):
        coupons = Coupons()
        data = self.createDictionary(code=self.alphaNumericStringGenerator(5),discount_type="percent",amount=self.randomNumberGenerator(1,50),undividual_use=self.randomBooleanGenerator(),exclude_sale_items=self.randomBooleanGenerator(),minimum_amount=self.randomNumberGenerator(100,200))
        couponId = coupons.createNewCouponAndGetId(self.commonUrl,data,201)
        assert coupons.verifySpecificCouponCreated(self.commonUrl+f"/{couponId}",data["code"],200) is True, \
            f"Failed: verifySpecificCouponCreated returned False for coupon code {data['code']}"
        dataToUpdate = self.createDictionary(amount=self.randomNumberGenerator(50.00,60.00))
        updatedResponse = coupons.updateSpecificCouponAndGetNewResponse(self.commonUrl+f"/{couponId}",dataToUpdate,200)
        assert updatedResponse["amount"] == dataToUpdate["amount"], \
            f"Failed: Update Response from updateSpecificCouponAndGetNewResponse not equal to {dataToUpdate['amount']}"

    def test_VerifyUserCanDeleteMultipleCouponns(self):
        coupons = Coupons()
        couponList = coupons.getListOfCoupons(self.commonUrl,200)
        if len(couponList) == 0:
            pytest.skip("Skipping test as couponList is empty")
        coupons.deleteListOfCouponsPresent(couponList,self.commonUrl,200)
        assert len(coupons.getListOfCoupons(self.commonUrl,200)) == 0,\
            f"Failed: All coupons are not deleted"
