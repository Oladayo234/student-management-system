user_input = input("enter an alphabet ")

vowel = "A a E e I i O o U u"
consonant = "B b C c D d F f G g H h J j K k L l M m N n P p Q q R r S s T t V v W w X x Y y Z z"

if user_input in vowel:
    print("It is a vowel ")

elif user_input in consonant:
    print("It is a consonant ")

else:  
    print ("it is invalid")
