class Patient:
    def __init__(self, namn, symtom):
        self.namn = namn
        self.symtom = symtom
        self.behandlad = False

    def undersök(self):
        print(f"{self.namn} undersöks för {self.symtom}.")

    def behandla(self):
        print(f"{self.namn} behandlas för {self.symtom}.")
        self.behandlad = True

# Testkod för att köra sjukhussimulationen
if __name__ == "__main__":
    patient1 = Patient("Anna", "feber")
    patient2 = Patient("Bengt", "hosta")
    patient3 = Patient("Caroline", "magsmärta")

    patienter = [patient1, patient2, patient3]

    for patient in patienter:
        patient.undersök()
        patient.behandla()
        if patient.behandlad:
            print(f"{patient.namn} är färdigbehandlad.")