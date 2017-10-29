class Doctor(object):
    def __init__(self, name, department, shift_assigned):
        self.name = name
        self.department = department
        self.shift_assigned = shift_assigned
        self.patients_assigned = 0
        self.per_patient = 2000
    def shift(self, shift_assigned):
        if shift_assigned =='7 a.m to 4 p.m':
            return 'Day-shift'
        elif shift_assigned == '4 p.m to 11 p.m':
            return 'Evening-shift'
        elif shift_assigned == '11 p.m to 7 a.m':
            return 'Graveyard'
        return 'Not assigned'

    def information(self):
        return (self.name, self.department, self.shift_assigned, self.patients_assigned)

    def doc_daily_pay(self):
        consultation_pay = (self.per_patient * self.patients_assigned)
        return consultation_pay

    doc_1 = ("John Doe", "Oncology", "11 p.m to 7 a.m", 21)
    print information(doc_1)
