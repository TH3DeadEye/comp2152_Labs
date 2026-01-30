#Q1
def studentgrade():
    grades = [85, 92, 78, 95, 88]
    grades.append(90)
    grades.sort()
    print("Sorted Grades",grades)
    print("Highest Grade", grades[-1])
    print("Lowest Grade", grades[0])
    print("Number of grades", len(grades))

#Q2
def shoppingCart(tofind,toCount, itemRemove):
    items = ["apple", "banana", "milk", "bread", "apple", "eggs"]
    print(f"Number of {toCount}  is: {items.count(toCount)}")
    print(f"Position of {tofind}  is: {items.index(tofind)}")
    items.remove(itemRemove)
    print(f"Removed item using pop: {items[-1]}")
    items.pop()
    print(f"Is banana in Cart: {'yes' if 'banana' in items else 'No'}")
    print(f"Final Items {items}")

#Q3
def CordinateSystem(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    tupleString = tuple("PYTHON")
    print(f"Point 1: x={x1}, y={y1}")
    print(f"Point 2: x={x2}, y={y2}")
    print(f"Distance between two points {((x2-x1)**2 + (y2-y1)**2)**0.5}")

    for i in tupleString:
        print(f"Characters tuple: {i}")


#Q4
def ClassAttendence(c1, c2):
    monday_class = c1
    wednesday_class = c2
    monday_class.add("Grace")
    print(monday_class, "\n", wednesday_class)
    print(f"Attended both classes: {monday_class.intersection(wednesday_class)}")   
    print(f"Attended Either class: {monday_class.union(wednesday_class)}")
    print(f"Only on Monday: {monday_class.difference(wednesday_class)}")
    print(f"Attended only one class: {monday_class ^ wednesday_class}")
    print(f"Is monday_class a subset of union: {monday_class <= monday_class.union(wednesday_class)}")



#Q5
def ContactBook(contact):
    print(f"Alices Phone number {contact['Alice']}")

    contact['Diana'] = "555-4321"
    print(f"Contacts after adding Diana: {contact}")

    contact['Bob'] = '555-0000'
    print(f"Contacts after updating Bob: {contact}")

    del contact['Charlie']
    print(f"Contacts after deleting Charlie: {contact}")

    print(f"All names: {contact.keys()}")
    print(f"All numbers: {contact.values()}")
    print(f"Total contacts: {len(contact.keys())}")


#calling the functions
studentgrade()
shoppingCart("milk", "apple", "apple")
CordinateSystem((3,7), (7,2))
ClassAttendence({"Alice", "Bob", "Charlie", "Diana"}, {"Bob", "Diana", "Eve", "Frank"})
ContactBook({'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-9999'})