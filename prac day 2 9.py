def get_season(month, day):
    seasons = {
        'Winter': (12, 21),
        'Spring': (3, 21),
        'Summer': (6, 21),
        'Fall': (9, 22)
    }
    month = month.lower().capitalize()

    for season, (start_month, start_day) in seasons.items():
        if (month == 'December' and day >= 21) or (month == 'March' and day < 20):
            return 'Winter'
        elif (month == 'March' and day >= 20) or (month == 'June' and day < 21):
            return 'Spring'
        elif (month == 'June' and day >= 21) or (month == 'September' and day < 22):
            return 'Summer'
        elif (month == 'September' and day >= 22) or (month == 'December' and day < 21):
            return 'Fall'
    
    return 'Invalid input'

month = input("Enter the month: ")
day = int(input("Enter the date: "))

season = get_season(month, day)
print(f"The season associated with the date {month} {day} is {season}.")
