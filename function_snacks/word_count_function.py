
def vowel_count(letters):
    total_count = 0
    vowels = "aeiouAEIOU"
    for char in letters:  
        if char in vowels:
            total_count += 1  
#            if char not in vowels:
#                total_count -= 1
    print(total_count)          
    return total_count

vowel_count("elephant")

