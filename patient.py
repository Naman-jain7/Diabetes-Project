class Patient:
    def __init__(self, name, age, pregnancies, glucose, bp, skinThickness, insulin, bmi, dpf):
        self.name = name
        self.age = age
        self.pregnancies = pregnancies
        self.glucose = glucose
        self.bp = bp
        self.skinThickness = skinThickness
        self.insulin = insulin
        self.bmi = bmi
        self.dpf = dpf
    
    def show(self, *args, **kwargs):
        for attr in args:
            if hasattr(self, attr):
                print(f"{attr}: {getattr(self, attr)}")
            else:
                print(f'{attr}: Not Found!')
    
    def to_tuple(self):
        return (self.name, self.age, self.pregnancies, self.glucose, self.bp, self.skinThickness, self.insulin, self.bmi, self.dpf)