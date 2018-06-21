_author_ = 'jslvtr'


def ask_age():

    user_age = input("Enter your age: ")
    return int(user_age)

def calculate_seconds_from_years(age_years):
    return age_years * 365 * 24 * 3600

def prompt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calculate_seconds_from_years(age)
    print("You have lived for {} seconds".format(seconds_lived))


prompt_user_and_calculate_age()

