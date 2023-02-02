"""
    DEPENDENCY INVERSION PRINCIPLE
        Definition:
            - High-level modules should not depend on low-level modules. Both
            should depend on abstractions
            - Abstractions should not depend on details. Details should depend
            on abstractions
        
        Concept Learned:
        - just study

"""
import zope.interface

## INTERFACES
class ProductRespository(zope.interface.Interface):
    def getAllProductNames(self) -> list:
        pass


@zope.interface.implementer(ProductRespository)
class SQLProductRepository:
    def getAllProductNames(self) -> list:
        return ["soap", "toothpaste"]
    

class ProductFactory:
    def create(self) -> ProductRespository:
        return SQLProductRepository()


class ProductCatalog:
    def listAllProducts(self) -> None:
        # productRespository = ProductRespository()
        productRespository = ProductFactory().create()

        allProductNames = productRespository.getAllProductNames()
        print(allProductNames)
    

myProductCatalog = ProductCatalog()
myProductCatalog.listAllProducts()

