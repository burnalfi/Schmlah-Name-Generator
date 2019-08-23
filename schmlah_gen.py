VOCAL = "aiueoAIUEO"
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "Desember"
]

def name():
    name = input("Enter Your Name: ").lower()

    if name in VOCAL:
        name = name
    else:
        name = name[1:]

    return name

def month(name_input: str):
    month_input = int(input("Enter The Numeric of The Month: ")) - 1

    if month_input > 0 and month_input < 12:
        return "It's {} Schml{}".format(MONTHS[month_input], name_input)
    else:
        return "There is no month {} Schml{}!".format(month_input, name_input)
        

print(month(name()))
