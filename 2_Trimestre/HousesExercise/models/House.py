from typing import Dict, Any

class House():
    def __init__(self, price, area, bedrooms, bathrooms, parking, basement):
        self.__price = price
        self.__area = area
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__parking = parking
        self.__basement = basement

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self.__price = new_price
        else:
            raise ValueError('Error al introducir el nuevo precio')
        
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, new_area):
        if isinstance(new_area, float) and new_area > 0:
            self.__area = new_area
        else:
            raise ValueError('Error al introducir el nuevo area.')
        
    @property
    def bedrooms(self):
        return self.__bedrooms
    
    @bedrooms.setter
    def bedrooms (self, new_bedrooms):
        if isinstance(new_bedrooms, float) and new_bedrooms > 0:
            self.__bedrooms = new_bedrooms
        else:
            raise ValueError('Error al introducir el número de habitaciones.')
        
    @property
    def bathrooms(self):
        return self.__bathrooms
    
    @bathrooms.setter
    def bathrooms (self, new_bathrooms):
        if isinstance(new_bathrooms, float) and new_bathrooms > 0:
            self.__bathrooms = new_bathrooms
        else:
            raise ValueError('Error al introducir el número de baños.')
        
    @property
    def parking(self):
        return self.__parking
    
    @parking.setter
    def parking(self, new_parking):
        if isinstance(new_parking, int) and  new_parking >= 0:
            self.__parking = new_parking
        else:
            raise ValueError('Error al introducir el número de parking.')
        
    @property
    def basement(self):
        return self.__basement
    
    @basement.setter
    def basement(self, new_basement):
        if isinstance(new_basement, str) and new_basement != '':
            self.__basement = new_basement
        else:
            raise ValueError('Error al introducir si tiene sótano la vivienda.')
        

    def to_dict(self) -> Dict[str, Any]:
        return {
            "price": self.__price,
            "area": self.__area,
            "bedrooms": self.__bedrooms,
            "bathrooms": self.bathrooms,
            "parking": self.__parking,
            "basement": self.__basement
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "House":
        return House(
            price = data["price"],
            area = data["area"],
            bedrooms = data["bedrooms"],
            bathrooms = data["bathrooms"],
            parking = data["parking"],
            basement = data["basement"]
        )


