persons =[
{
    'first': 'dhankumari',
    'last': 'kc',
    'age': 22,
    'gender': 'female',
    'friends':['mevita','candace','neetal','nishika']

},
{
    'first': 'kannu',
    'last': 'chettri',
    'age': 23,
    'gender': 'female',
    'friends': ['hrutwa','mustaf','javed','keegan']
}
]
"""
for  person in persons:
    for key,value in person.items():
        if key == "friends":
            for friend in value:
                if friend == "mustaf":
                    continue
                print(friend)
"""


i=1
while(i<=10):
    j=1
    while(j<=10):
        print(i,"*",j,"=", i*j)
        j+=1
    i+=1


       












