"""
    OPEN / CLOSE PRINCIPLE
        Definition:
            - Software components should be closed for modification, but open for extension
        
        Concept Learned:
        - just study

"""

# Problem situation: "Pass as parameter other kind of InsuranceCustomerProfile"
class HealthInsuranceCustomerProfile:
    def isLoyalCustomer(self):
        return True

class VehiculeInsuranceCustomerProfile:
    def isLoyalCustomer(self):
        return True

class InsurancePremiumDiscountCalculator:
    def calculatePremiumDiscountPercent(customer: HealthInsuranceCustomerProfile):  # need modification in here
        if customer.isLoyalCustomer():
            return 20
        return 0
    # NOT SOLID solution
    def calculatePremiumDiscountPercent(customer: VehiculeInsuranceCustomerProfile):
        if customer.isLoyalCustomer():
            return 20
        return 0


### SOLUTION USING SOLID Principle

import zope.interface
class CustomerProfile(zope.interface.Interface):
    def isLoyalCustomer(self) -> bool:
        pass

@zope.interface.implementer(CustomerProfile)
class HealthInsuranceCustomerProfile:
    def isLoyalCustomer(self):
        return True

@zope.interface.implementer(CustomerProfile)
class VehicleInsuranceCustomerProfile:
    def isLoyalCustomer(self):
        return True
    
class InsurancePremiumDiscountCalculator:
    def calculatePremiumDiscountPercent(customer: CustomerProfile):
        if customer.isLoyalCustomer():
            return 20
        return 0



        


