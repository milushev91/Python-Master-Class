from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

#pop() removes arbitrary item from a set and returns it
#arbitrary means random
#it used when we don't care which item will be removed

while trial_patients:
  patient = trial_patients.pop()
  print(patient, end= " : ")
  perscription = patients[patient]
  print(perscription)
