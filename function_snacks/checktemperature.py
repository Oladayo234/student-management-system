
def temperature_value (temperature, unit, threshold):

    if  unit.lower() == 'f':
        temperature = (temperature * 9/5) + 32
        print (temperature)
#        return temperature

    if unit.lower() == 'c':
        temperature = (temperature - 32) * 5/9
        print (temperature)
#        return temperature

    if temperature < threshold:
        print("cold advisory")
#        return "cold advisory"

    elif temperature > threshold:
        print("Heat alert")
        return "Heat alert"        

   


temperature_value(80, "c", 80)








#elif temperature_value in fahrenheit:
#    temperature_value == celcius_to_fahrenheit 
#fahrenheit_to_celcius = (fahrenheit - 32) * 5/9
 
