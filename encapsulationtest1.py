class Patient: #Creates a patient class and assigns all created instances to have protected and private values for fullname, age, procedure, and symptoms
    def __init__(self, fullname, age, procedure, symptoms):
        self._fullname = fullname #Protected attribute for fullname
        self._age = age #Protected attribute for age
        self.__procedure = procedure #Private attribute for procedure
        self.__symptoms = None #Private attribute for symptoms, conditionally set later

    def get_patient(self): #Returns the values of of all patient data 
        return self._fullname, self._age, self.__procedure, self.__symptoms

    def set_symptoms(self, symptoms): 
        if self.__procedure: #Checks if the procedure attribute has value and if so,
            self.__symptoms = symptoms #Sets the private symptom attribute to its value
        else: #If no Procedure is given, this text message should show
            print("Symptoms will be a side-effect of the procedure.")
        

p1 = Patient("Yoona Velen", 34, "Carotid Endarterectomy" , "") #Creates an object instance that gives values to the protected and private attributes
print(p1.get_patient()) #Prints the values
    
p1.set_symptoms("Symptoms: Loss of Breath, Dizziness, Limited Mobility") #Conditionally adds the symptoms attribute if procedure has value
print(p1.get_patient()) #Print the object once more with updated symptoms attributes
