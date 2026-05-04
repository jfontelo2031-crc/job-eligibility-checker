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

while True:
        highest_education = input("Enter highest education (college/seniorhigh/vocational/below): ")
        if (highest_education == "college"    or highest_education == "College"    or
            highest_education == "seniorhigh" or highest_education == "Seniorhigh" or
            highest_education == "vocational" or highest_education == "Vocational" or
            highest_education == "below"      or highest_education == "Below"):
            break
        display_error_message()

    return age, years_of_experience, highest_education

def evaluate_applicant(age, years_of_experience, highest_education):
    if (18 <= age <= 35 and 3 <= years_of_experience <= 10 and
       (highest_education == "college" or highest_education == "College")):
        return "Ideal Range", "Strong Candidate", "Highly Qualified"

elif (36 <= age <= 45 and 1 <= years_of_experience <= 2 and
         (highest_education == "seniorhigh" or highest_education == "Seniorhigh" or
          highest_education == "vocational" or highest_education == "Vocational")):
        return "Acceptable", "Entry Level", "Qualified"

elif ((age < 18 or age > 45) and years_of_experience == 0 and
          (highest_education == "below" or highest_education == "Below")):
        return "Not Eligible", "No Experience", "Not Eligible"

else:
        return "Invalid", "Invalid", "Invalid"

def display_result(age_result, experience_result, education_result):
    print("----CHECKING----")
    if age_result == "Invalid":
        print("Result: No matching qualification category found.")
    else:
        print("Age:       ", age_result)
        print("Experience:", experience_result)
        print("Education: ", education_result)

def ask_to_continue():
    while True:
        choice = input("Check another applicant? (yes/no): ")
        if choice == "yes" or choice == "Yes":
            return True
        elif choice == "no" or choice == "No":
            return False
        display_error_message()











