def display_error_message():
  print("Error: Invalid input. Please try again.")
  
def is_number(value):
    valid = True
    for character in value:
        if character < "0" or character > "9":
            valid = False
    return valid  

def get_applicant_info():
    while True:
        age_input = input("Enter your age: ")
        if age_input != "" and is_number(age_input):
            age = int(age_input)
            break
        display_error_message()

while True:
        experience_input = input("Enter years of work experience: ")
        if experience_input != "" and is_number(experience_input):
            years_of_experience = int(experience_input)
            break
        display_error_message()
