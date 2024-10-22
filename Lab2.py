def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list=get_user_input()
 calc_average(num_list)
 find_min_max(num_list)
 sort_temperature(num_list)
 median = calc_median_temperature(num_list)
 print(f"Median = {median}")

def display_main_menu(): 
 print("Enter some numbers separated by commas (e.g. 5, 67,32)") 

def get_user_input():
  x = input()
  y= list(map(float,x.split(",")))
  print(f"Numbers = {y}")
  return y

def calc_average(num_list): 
 average = sum(num_list)/len(num_list)
 print(f"Average = {average}")

def find_min_max(num_list):
 x=min(num_list)
 y=max(num_list)
 print(f"Min = {x},Max = {y}")

def sort_temperature(num_list):
 x=sorted(num_list)
 print(f"Sorted Temperature = {x}")

def calc_median_temperature(num_list):
 sorted_list = sorted(num_list)
 n = len(sorted_list)
 mid = n // 2
    
    # If the length is odd, return the middle element
 if n % 2 != 0:
    return sorted_list[mid]
    # If the length is even, return the average of the two middle elements
 else:
    return (sorted_list[mid - 1] + sorted_list[mid]) / 2
 
 

 
if __name__ == "__main__": 
 main() 