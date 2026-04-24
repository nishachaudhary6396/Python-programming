from abc import ABC, abstractmethod 
class hospital(ABC):      #abstraction
    @abstractmethod        
    def get_role(self):
        pass
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        print(self.name,self.age)
class doctor(person,hospital):        #inheritance
    def __init__(self,name,age,attributes):
        super().__init__(name,age)
        self.attributes = attributes
    def display_details(self):
        print(f"Name: {self.name},Age: {self.age},Specialization: {self.attributes}")

    def get_role(self):
        print("I am doctor")
class patient(person,hospital):
    def __init__(self,name,age,disease):
        super().__init__(name,age)
        self.__disease = disease    
    def display_details(self):
        print(f"name :{self.name},Age :{self.age}, Disease :{self.__disease}")

    def get_role(self):
        print("I m pateint")
    @property
    def get_disease(self):   #getter       
        return self.__disease
    
    @get_disease.setter
    def set_disease(self,new_disease):    #setter
        self._disease = new_disease
        

dc = doctor("Nisha","22","Cardiologist")
p = patient("Riya","21","Fever")
dc.display_details()
p.display_details()
dc.get_role()
p.get_role()





