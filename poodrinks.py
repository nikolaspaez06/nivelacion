class drinks:
    def __init__(self,type,color,price):
        self._color
        self._type
    def get_info(self):
        return f"""\n Tipo: {self._type}\n Color: {self._color}\n Precio: {self._price}"""

    def get_type(self):
        return self._title

    def get_price(self):
        return self._price
    
    def set_price(self,new_price):
        if new_price > 0:
           self._price = new_price
        else:
            print("el precio de la bebida no puede ser menor o igual a 0")
    
    def get_color(self):
        return self._color


drinks1 = drinks("cafe","negro","3,000")
drinks2 = drinks("jugo de naranja","naranja","4,000")


drinks.set_price(0)


print(drinks1.get_info())
print(drinks2.get_info())
print(drinks3.get_info())