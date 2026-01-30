#This function converts seconds since midnight into time format
def convertTime(seconds):
    # Validate input
    if not isinstance(seconds, int) or seconds < 0 or seconds >= 86400:
        return "Invalid input."

    #Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    #Determine AM or PM
    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    #Convert to 12-hour format
    hours = hours % 12
    if hours == 0:
        hours = 12

    return f"{hours} {minutes} {secs} {period}"


#Example usage
print(convertTime(19067))