import patient
import procedure

def main():
    #patient one
    patient1= patient.Patient('James','Jones','123 Fourth Street','Charleston','Illinois',61920,'217-555-1212','jjones@eiu.edu','Ellie','Jones','217-555-1213','ejones@gmail.com')
    patients1_procedure= procedure.Procedure('Physical Exam','12/01/2022','Dr. Nathatan Alcox','SBL Clinic', 'Mattoon', 250.00)
    #patient two
    patient2= patient.Patient('Carmen','Brown','456 Ninth Street','Charleston','Illinois',61920,'217-666-1314','cbrown@eiu.edu','Jennifer','Brown','217-555-1213','jbrown@gmail.com')
    patients2_procedure= procedure.Procedure('X-ray','12/05/2022','Dr. Leslie Fernandez','Carle Foundation', 'Mattoon', 150.00)

    #Display for patient 1
    print('First Name: '+patient1.get_first_name())
    print('Last Name: '+patient1.get_last_name())
    print('Address: '+patient1.get_address())
    print('City: '+patient1.get_city())
    print('State: '+patient1.get_state())
    print('ZIP: '+str(patient1.get_zip_code()))
    print('Phone: '+patient1.get_phone())
    print('Email: '+patient1.get_email())
    print('Emergency Contact-First Name: '+patient1.get_emergency_fname())
    print('Emergency Contact-Last Name: '+patient1.get_emergency_lname())
    print('Emergency Contact Phone: '+patient1.get_emergency_phone())
    print('Emergency Contact Email: '+patient1.get_emergency_email(),sep='\n')
    print('\n')
    #Display for patient 2
    print('First Name: '+patient2.get_first_name())
    print('Last Name: '+patient2.get_last_name())
    print('Address: '+patient2.get_address())
    print('City: '+patient2.get_city())
    print('State: '+patient2.get_state())
    print('ZIP: '+str(patient2.get_zip_code()))
    print('Phone: '+patient2.get_phone())
    print('Email: '+patient2.get_email())
    print('Emergency Contact-First Name: '+patient2.get_emergency_fname())
    print('Emergency Contact-Last Name: '+patient2.get_emergency_lname())
    print('Emergency Contact Phone: '+patient2.get_emergency_phone())
    print('Emergency Contact Email: '+patient2.get_emergency_email())
    print('\n')
    #Display for Patients 1 procedures
    print('Procedure: '+patients1_procedure.get_procedure())
    print('Date: '+patients1_procedure.get_date())
    print('Practicioner: '+patients1_procedure.get_practitioner_name())
    print('Hospital Name: '+patients1_procedure.get_hospital())
    print('Hospital City: '+patients1_procedure.get_city())
    print('Charge: '+str(patients1_procedure.get_procedure_charge()))
    print('\n')
    #Display for patients 2 procedures
    print('Procedure: '+patients2_procedure.get_procedure())
    print('Date: '+patients2_procedure.get_date())
    print('Practicioner: '+patients2_procedure.get_practitioner_name())
    print('Hospital Name: '+patients2_procedure.get_hospital())
    print('Hospital City: '+patients2_procedure.get_city())
    print('Charge: '+str(patients2_procedure.get_procedure_charge()))
    
    
    
main()
