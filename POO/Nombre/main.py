from controller import PatientController
from view import View


controller = PatientController()
view = View()

patients = controller.load_patients("patients.txt")

loop = True
while loop == True:

    view.menu()
    menu_choise = int(input())
    if menu_choise == 1:

        patients = controller.get_patients_over_18(patients)
        view.display_patients(patients)

    elif menu_choise == 2:
        
        view.choose_patient()
        selected_patient = input()
        view.new_weight()
        nWeight = float(input())
        controller.select_patient(nWeight, selected_patient, patients)
        bmi = controller.calculate_bmi(selected_patient, patients)
        view.display_bmi_result(bmi)
        difference = controller.calculate_difference(selected_patient, patients)
        view.display_weight_difference(difference)
        controller.save_new_data(patients, "patients.txt")
        
    elif menu_choise == 3:
        
        view.bye_bye()
        loop = False
    






'''
Juan;30;12345678;M;70;1.70
Maria;25;98765432;F;60;1.65
Carlos;45;24681357;M;80;1.80
Ana;35;13579246;F;55;1.60
Pedro;4;56789123;M;75;1.75
Laura;28;43219876;F;58;1.63
Luis;55;78912345;M;85;1.85
'''







