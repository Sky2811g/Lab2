def calculate_bmi(height, weight): 
 bmi=weight/(height*height)
 if bmi<18.5:
  WeightC = "Under Weight"
 elif 18.5<bmi<25.0:
  WeightC = "Normal Weight"
 else :
  WeightC = "Over Weight"
 
 print("BMI = " + WeightC) 
 
calculate_bmi(weight=57, height=1.73) 