services = input("Enter 1 service that you provide:- ")

match services.lower():
    case "development":
        print(f"we are providing \"{services}\" services")
    case "qa":
        print(f"we are providing {services} services")
    case _:
        print("we are providing none as of now")

# _ default case

# combine values
weekend_or_weekday = input("Enter a day:- ")

match weekend_or_weekday.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("weekday or working day")
    case "sunday" | "saturday":
        print("weekend or holiday")


# if statement in match case
name = "vrk"
age = 150

name1 = "vrk"
match name1.lower():
    case "vrk" if age>170:
        print("match the requirements")
    case _:
        print("not matching")