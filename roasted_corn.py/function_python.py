#def string_characters(value):
#    output = " "
#    for item in (value):
#        if len(value) >= 2:
#            output = value[0] + value[1] + value[-2] + value[-1]
#            return output
#        else: 
#           return output      
#print(string_characters("s"))


      
#def adding_to_string(value):
#    
#    for items in range(len(value)):
#
#        if len(value) == 3 and len(value) <= 3:
#            value = (value + "ing")
#            
#        if len(value) > 3 and value[-3] == "i" and value[-2] == "n" and value [-1] == "g":
#            value = (value + "ly")
#
#        if len(value) < 3:
#            return value
#    return value
#print(adding_to_string("on"))
    

def longest_word(value):
    element = ""
    longest = ""
    for items in range(len(value)):
        length = len(value)
        longest = length
        if element > str(value):
           longest = value
        return value, element
print(longest_word(["welcome", "out", "weather", "ability", "one"]))
        


#def remove_function(value):
#    output =""
#    for item in range(len(value)):
#        if item % 2 != 0:
#            output += value[item]  
#    return output
#
#print(remove_function("Semicolon"))



#def minimum_number(value):
#    for count in value:
#        smallest = count
#        if count < smallest:
#            smallest = value
#        return smallest
#    
#print(minimum_number([2,4,9,3,5,7,8]))
#
#
#
#def maximum_number(value):
#    for count in value:
#        highest = count
#        if count > highest:
#            largest = value
#        return largest
#    
#print(minimum_number([8,4,9,3,5,7,2]))



#def repeated_string(input_one, input_two):
#    
#    if type(input_two) == float:
#        output = input_one
#    else:
#        output = input_one * input_two
#    return output
#print(repeated_string("hello", 4.5))




#def squared_list(value):
#    my_list = []
#    number_square = 1 
#    for count in range(0, len(value)):
#        number_square = value[count] * value[count]
#        my_list.append(number_square)
#    return my_list
#
#print(squared_list([2,3,4,5,7]))



#def sum_of_numbers(value):
#    my_list = []
#    sum_of_numbers = 0
#    for count in range(0, len(value)):
#        number_square = value[count] * value[count]
#        sum_of_numbers +=  number_square
#    return sum_of_numbers
#
#print(sum_of_numbers([2,3,4,5,7]))





    
