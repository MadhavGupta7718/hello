print("The Love Calculator is calculating your score...")
def my_function(name1, name2):
 lower_case = combine_name.lower()
 t = lower_case.count("t")
 r = lower_case.count("r")
 u = lower_case.count("u")
 e = lower_case.count("e")
 true_total = t+r+u+e
 l = lower_case.count("l")
 o = lower_case.count("o")
 v = lower_case.count("v")
 e = lower_case.count("e")
 love_total = l+o+v+e
 love_score = int(str(true_total)+str(love_total))
 if love_score <10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
 elif love_score >40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
 else:
print(f"Your score is {love_score}")
  





  