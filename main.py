#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = {"January": "01", "February": "02", "March": "03", "April": "04", 
              "May": "05", "June": "06", "July": "07", "August": "08", 
              "September": "09", "October": "10", "November": "11", 
              "December": "12" }
    month_num = months[month]
    return month_num
def parse_day(day):
    day = day.replace(",","")
    new= "0"
    day_num = int(day)

    if day_num < 10:
        new += day 
    else:
        new = day

    return new
#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    parsed_date = ""
    comps = user_string.split()
    month = comps[0]
    day = comps[1]
    year = comps[2]

    month_str = parse_month(month)
    day_str = parse_day(day)

    parsed_date = month_str + "/" + day_str + "/" + year

    return parsed_date

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_input = input("Enter a date: ")

    while user_input != "-1":
        parsed = parse_date(user_input)
        print(parsed)
        user_input = input("Enter a date: ")