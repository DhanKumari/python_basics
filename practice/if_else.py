person={'first': 'dhankumari',
 'last': 'kc',
 'age': 22,
 'gender': 'female'
}

#person={}
#if person:
#else:
 #   print("person doesn't exist")

#if elif else

#if person["age"]>25:
#   print("person is older than 25")
#elif person["age"]==25:
#    print("peerson is 25 years old")
#else:
#    print("person is younger than 25 ")

if "age" in person.keys() and "gender" in person.keys() :
    if person["age"]>18 and person["gender"]=="female":
        print("person is elgible for driving licence ")
    else:
        print("person is not eligiblle for licence ")
else:
    print("person is not eligible for licence ")
