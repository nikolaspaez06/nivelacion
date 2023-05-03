class celetial:
    def __init__(self,tipe):
        self._tipe
    def get_info(self):
       return f"""\n Tipo: {self._tipe}"""
    def get_tipe(self):
        return self._tipe
celetial1 = celestial("luna")
celetial2 = celestial("sol")
celetial3 = celestial("estrellas")
print(celestial1.get_info())
print(celestial2.get_info())
print(celestial3.get_info())