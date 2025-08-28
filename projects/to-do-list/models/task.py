
class Task:
    def __init__(self, name, description, status, id_to_do_list):
        self.name = name
        self.description = description
        self.status = status
        self.id_to_do_list = id_to_do_list
    
    #Get
    @property
    def name(self):
        return self._name
    
    #Set
    @name.setter
    def name(self, value):
        self._name = value

    #Get
    @property
    def description(self):
        return self._description
    
    #Set
    @name.setter
    def description(self, value):
        self._description = value

    #Get
    @property
    def completed(self):
        return self._completed
    
    #Set
    @name.setter
    def completed(self, value):
        self._description = value