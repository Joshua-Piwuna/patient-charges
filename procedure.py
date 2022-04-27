class Procedure:

    def __init__(self,pro_name,pro_date,prac_name,hospital,city,pro_charge):
        self.__pro_name=pro_name
        self.__pro_date=pro_date
        self.__prac_name=prac_name
        self.__hospital=hospital
        self.__hospital_city=city
        self.__pro_charge=pro_charge

    def get_procedure(self):
        return self.__pro_name

    def get_date(self):
        return self.__pro_date

    def get_practitioner_name(self):
        return self.__prac_name

    def get_hospital(self):
        return self.__hospital

    def get_city(self):
        return self.__hospital_city

    def get_procedure_charge(self):
        return self.__pro_charge
        
