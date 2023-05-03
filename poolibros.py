class boock:
    def __init__(self,title,price,author):
        self._title
        self._price
        self._author
    def get_info(self):
        return f"""\n Tiulo: {self._title}\n Autor: {self._author}\nprecio: {self._price}"""

    def get_title(self):
        return self._title

    def get_price(self):
        return self._price
    
    def set_price(self,new_price):
        if new_price > 0:
           self._price = new_price
        else:
            print("el precio del libro no puede ser menor o igual a 0")
    
    def get_autor(self):
        return self._autor

book1 = book("viaje al centro de la tierra","julio berne","60.000" )




book1.set_price(0)


print(book1.get_info())