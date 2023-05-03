class animals:
    def __init__(self,kind,respiration,birth):
        self._kind
        self._respiration
        self._birth
    def get_info(self):
        return f"""\n Tipo: {self._kind}\n Respiracion: {self._respirations}\n Nacimiento: {self._birth}"""

    def get_kind(self):
        return self._kind

    def get_respration(self):
        return self._rspiration
    
    def get_birth(self):
        return self._birth
animals1 = animals ("leon","pulmonar","mamifero" )
animals2 = animals ("pez payaso","branquial","oviparo")
animals3 = animals ("gallina","pulmonar","oviparo")



print(animals1.get_info())
print(animals2.get_info())
print(animals3.get_info())