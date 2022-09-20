"""------------ list

 is mutable built-in datatupe that can hold different values with
 different data structures

"""
"1- to define a list "
l = []
myl = list([])

"2- list can hold different values from different types "
myl = ["iti", 'september', 'autumn', 2022, True, ['postgres', 'python'], "apis", "apis"]

"3- can access the elements using index"
print(myl[3])

"4- mutable datatype"
print(myl)
myl[4]= "Very Happpy"
print(myl)

"5- append element to the list"
myl.append("Django")

"6- insert element at certain index"
myl.insert(3, "apis")

"7- pop the element"
poppeditem = myl.pop()  # return with the last element in the list

"8- pop item at certain index"
newpopped = myl.pop(5)

"9- remove element  ---> remove the first occurance of the element "
myl.remove("apis")

"10- get len of the list "
print(len(myl))

"11- get count of element occurence in the list"
print(myl.count("apis"))

"12- list concatenation"
courses = ["pyhton", "djnago"]
courses2 = ["flask", "odoo"]
allcourses = courses  + courses2
# print(allcourses)

"13- extend a list"
courses.extend(courses2)
print(courses)
print(courses2)

"14- sort list ---> ((___you must make sure the items in the list are from the same type___))"
# courses.sort()
# print(courses)
courses.sort(reverse=True)
print(courses)

"15- reverse a list "
myl.reverse()
print(myl)

"16- loop over the list "
for item in myl:
    print(f"item -= {item}")

"17- in operator "
if "apis" in myl:
    print("-=--- Found----")
else:
    print("----- not found Bye ----- ")


"18- min and max ----> the list items must be from the same type "
print(max([4,5,6,666,9]))

print(min([4,5,6,666,9]))

print(sum([4,5,6,666,9]))