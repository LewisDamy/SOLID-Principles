"""
    INTERFACE SEGREGATION PRINCIPLE
        Definition:
            - SOLID Principles complentent each other, and work toghether in union, to achieve
            the common purpose of a well-design software
        
        Concept Learned:
        - just study

"""
import zope.interface


### INTERFACES
class IPrint(zope.interface.Interface):
    def print(self):
        pass
    
    def getPrintSpoolDetails(self):
        pass

class IScan(zope.interface.Interface):
    def scan(self):
        pass
    
    def scanPhoto(self):
        pass

class IFax(zope.interface.Interface):
    def fax(self):
        pass
    def internetFax(self):
        pass


### CLASSES THAT INHERIT THOSE INTERFACES
@zope.interface.implementer(IPrint, IScan, IFax)
class XeroxWorkCenter:
    def print(self):
        print("Printing... at Xerox Work Center")
    
    def getPrintSpoolDetails(self):
        print("Details of printer at Xerox Work Center")
    
    def scan(self):
        print("Scanning docum... at Xerox Work Center")
    
    def scanPhoto(self):
        print("Scanning photo... at Xerox Work Center")
    
    def fax(self):
        print("Faxing docum... at Xerox Work Center")


@zope.interface.implementer(IPrint, IScan)
class HPPrinterNScanner:
    def print(self):
        print("Printing... at HP Printer Scanner")

    def getPrintSpoolDetails(self):
        print("Details of HP Printer Scanner")

    def scan(self):
        print("Scanning document... at HP Printer Scanner")
    
    def scanPhoto(self):
        print("Scanning photo... at HP Printer Scanner")

@zope.interface.implementer(IPrint)
class CanonPrinter:
    def print(self):
        print("Printing... at Canon Printer")

    def getPrintSpoolDetails(self):
        print("Details of Canon Printer")



myPrinter = CanonPrinter()
myPrinter.print()
myPrinter2 = HPPrinterNScanner()
myPrinter2.scanPhoto()
