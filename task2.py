
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper()) 
    lower_count = sum(1 for char in string if char.islower()) 
    return upper_count, lower_count

input_string = "Hello World"
upper, lower = count_case_letters(input_string)
print(f"Uppercase: {upper}, Lowercase: {lower}")