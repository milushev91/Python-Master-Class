from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

for patient in trial_patients:
  #getting patient prescription from patient dictionary in prescription_data modlue
  #we use patient name from trial pantients as key
  prescription = patients[patient]
  #try - more optimised approach with try except
  if warfarin in prescription:
    prescription.remove(warfarin)
    prescription.add(edoxaban)
# except KeyError:
  else:
    print(f"Patient {patient} isn't taking warfarin"
         f"Please remove {patient} from trial patients")
