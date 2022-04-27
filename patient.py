class Patient:
    

    def __init__(self,first_name,last_name,address,city,state,zip_code,phone,email,emergency_fname,emergency_lname,emergency_phone,emergency_email):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__address=address
        self.__city=city
        self.__state=state
        self.__zip_code=zip_code
        self.__phone=phone
        self.__email=email
        self.__emergency_fname=emergency_fname
        self.__emergency_lname=emergency_lname
        self.__emergency_phone=emergency_phone
        self.__emergency_email=emergency_email
        
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_emergency_fname(self):
        return self.__emergency_fname

    def get_emergency_lname(self):
        return self.__emergency_lname

    def get_emergency_phone(self):
        return self.__emergency_phone

    def get_emergency_email(self):
        return self.__emergency_email



