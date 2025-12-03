def convert_time(minutes):
    hours = minutes/60
    seconds = minutes * 60
    print( hours,  seconds)
    return (hours, seconds)
convert_time(30)
