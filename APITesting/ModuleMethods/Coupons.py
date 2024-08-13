from APITesting.ModuleMethods.CommonMethods import CommonMethods


class Coupons(CommonMethods):

    def __init__(self):
        pass

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to get list of coupons which are created
    param: url,statusCode
    return: list
    '''
    def getListOfCoupons(self,url,statusCode):
        response = self.get(url,statusCode)
        listOfCoupons = response.json()
        return listOfCoupons

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to create New Coupon And Get Id
    param: url,data,statusCode
    return: string
    '''
    def createNewCouponAndGetId(self,url,data,statusCode):
        response = self.post(url,data,statusCode).json()
        return str(response["id"])

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to verify Specific Coupon Created
    param: url,couponCode,statusCode
    return: bool
    '''
    def verifySpecificCouponCreated(self,url,couponCode,statusCode):
       # actualUrl = str(url).replace("<id>",str(couponId))
        response = self.get(url,statusCode).json()
        return response["code"] == str(couponCode).lower()

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to delete Specific Coupon
    param: url,statusCode
    return: none
    '''
    def deleteSpecificCoupon(self,url,statusCode):
        self.delete(url,statusCode).json()

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to verify Specific Coupon Deleted
    param: url,statusCode
    return: bool
    '''
    def verifySpecificCouponDeleted(self,url,statusCode):
        response = self.get(url,statusCode).json()
        return response["status"] == "trash"

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to get Id Of Specific Coupon Code
    param: couponList,couponCode
    return: string
    '''
    def getIdOfSpecificCouponCode(self,couponList,couponCode):
        for i in range(len(couponList)):
            if couponList[i]["code"] == str(couponCode).lower() :
                return str(couponList[i]["id"])

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used to update Specific Coupon And Get New Response
    param: url,data,statusCode
    return: dict
    '''
    def updateSpecificCouponAndGetNewResponse(self,url,data,statusCode):
        response = self.put(url,data,statusCode).json()
        return response

    '''
    created By: Shivam Ojha
    since: 30 July 2024
    desc: This method is used to delete List Of Coupons Present
    param: couponList,url,statusCode
    return: none
    '''
    def deleteListOfCouponsPresent(self,couponList,url,statusCode):
        for i in range(len(couponList)):
            couponId = couponList[i]["id"]
            self.deleteSpecificCoupon(url+f"/{couponId}",statusCode)