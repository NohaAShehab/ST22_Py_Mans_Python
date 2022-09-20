"""


    tuple is immutable datatype
"""
"1- to define a tuple "
t = ()
myt = tuple([])

"2- tuple can hold different values from different types "
myt = ("iti", 'september', 'autumn', 2022, True, ['postgres', 'python'], "apis", "apis")

"3- can access the elements using index"
print(myt[3])

"4- get len of the tuple "
print(len(myt))

"5- get count of element occurence in the tuple"
print(myt.count("apis"))

"6- list concatenation"
courses = ("pyhton", "djnago")
courses2 = ("flask", "odoo")
allcourses = courses + courses2

"7- loop over the list "
for item in myt:
    print(f"item -= {item}")

"8- in operator "
if "apis" in myt:
    print("-=--- Found----")
else:
    print("----- not found Bye ----- ")

"9- min and max ----> the list items must be from the same type "
print(max((4, 5, 6, 666, 9)))

print(sum((4, 5, 6, 666, 9)))

"10- tuple of one item "

t = ("python",)

"11- cast the tuple to a list "

t = ("python",'django')

t = list(t)

l= [4,55,6,5]
l  = tuple(l)