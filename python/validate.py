class validateMinimum:
  
  income = 0
  name ="farida atei"
  def __init__(self,name,income):
    self.income = income
    self.name =name
    self.validateMinimum()
    
  def validatelncome(self):
    if self.income<10,001 == False:
     raise ValueError("The income {} is not numeric".format(self.income))
     
  def validateName(self):
    if self.income.isnumeric() == False:
      raise ValueError("The name {} is not a string".format(self.name))
  def calculate_tax(self):
    return float(self.income) *0.3
       
income=input("what is your income")
name =input("what is your name")
employee = TaxPayer(name,income)
print(employee.calculate_tax())