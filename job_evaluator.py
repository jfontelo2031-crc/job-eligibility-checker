def display_error_message():
  print(""Error: Invalid input. Please try again.")
  
def is_number(value):
    valid = True
    for character in value:
        if character < "0" or character > "9":
            valid = False
    return valid        
