def calculate_bmi(height, weight): 
 bmi=weight/(height*height)
 if bmi<18.5:
  WeightC = "-1"
 elif 18.5<bmi<25.0:
  WeightC = "0"
 else :
  WeightC = "1"
 
 print("BMI = " + WeightC) 
 
calculate_bmi(weight=57, height=1.73) 