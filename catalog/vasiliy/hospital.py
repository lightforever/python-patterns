class PersonalNurse:
    def __init__(self, patient_type):
        self.__available_treatments = {
            'slightly ill': self.__apply_treatment_1,
            'ill': self.__apply_treatment_2,
            'seriously ill': self.__apply_treatment_3,
            'almost dead': self.__call_doctor,
        }

        if patient_type not in self.__available_treatments:
            raise ValueError()

        self.patient_type = patient_type

    def __apply_treatment_1(self):
        print('rest')

    def __apply_treatment_2(self):
        print('pills')

    def __apply_treatment_3(self):
        print('many pills')

    def __call_doctor(self):
        print('aaaa he is almost dead!')

    def treat(self):
        return self.__available_treatments[self.patient_type]()


if __name__ == '__main__':
    PersonalNurse('ill').treat()
    PersonalNurse('almost dead').treat()
    PersonalNurse('seriously ill').treat()

    PersonalNurse('pretending').treat()
