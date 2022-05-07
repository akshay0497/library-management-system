# Student Library 
''' by the help of OOPs function'''
from datetime import datetime
now = datetime.now()
# print(now)
class Classes:
    
    def __init__(self, list_of_classes):
        self.classes = list_of_classes

    def displayAvailableclasses(self):
        print("\n Books are available for these class as mentioned below: ")
        for classes in self.classes:
            print(' \t\t\t\t --> ' + classes)

class Library:
    dr_sting1 = now.strftime('%d-%b-%y') 
    dr_sting2 = now.strftime('%H:%M:%S')
    # print(dr_sting1)
    # print(dr_sting2)

    def __init__(self, list_of_books):
        self.books = list_of_books

    def displayAvailablebooks(self):
        print('\n Books present in this library are:- ')
        for book in self.books:
            print(" \t\t\t\t -- " + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'''You have been issued {bookName}. Please keep it safe and return it within 30 days.
Issued from Central Library on {self.dr_sting1} and time is {now.strftime('%H:%M:%S')}''')
            self.books.remove(bookName)
            return True
        else:
            print('Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available')
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f'''Thanks you returning the books..... Have a nice day.......... 
Issued book return to Central Library on {self.dr_sting1} and time is {now.strftime('%H:%M:%S')}''')
    
    def addBook(self, bookName):
        self.books.append(bookName)
        print('Thanks you for this books..... Have a nice day..')
    
class Student:
    def requestBook(self):
        reqBook = input('Enter the name of the book you want to borrow: ')
        self.book = reqBook
        return self.book
    
    def returnBook(self):
        self.book = input('Enter the name of the book you want to borrow: ')
        return self.book
    
    def addBook(self):
        self.book = input('Enter the name of the book you want to add: ')
        return self.book        
    
if __name__ == "__main__":
    central = Classes(["Class - 6", "Class - 7", "Class - 8", "Class - 9", "Class - 10", "Class - 11", "Class - 12"])
    centralLibrary = Library(['Science - Class- 6', 'Social Science - Class - 6', 'Maths - Class - 6', 'Our Pasts-I - Class - 6', 'The Earth our Habitat - Class - 6', 'Social and Political Life-I - Class -6',
'Science - Class- 7', 'Social Science - Class - 7', 'Maths - Class - 7', 'Our Pasts-II - Class - 7', 'Our Environment - Class - 7', 'Social and Political Life-II - Class -7', 'Science - Class- 8', 
'Social Science - Class - 8', 'Maths - Class - 8', 'Our Pasts-III (part 1 & 2) - Class - 8', 'Resource and Development(Geography) - Class - 8', 'Social and Political Life - Class -8', 'Science - Class- 9', 
'Social Science - Class - 9', 'Maths - Class - 9', 'Contemporary India - Class - 9', 'India and the Contemporary World-I - Class - 9', 'Economics - Class -9', 'Democratic Politics - Class - 9',
'Science - Class- 10', 'Social Science - Class - 10', 'Maths - Class - 10', 'Contemporary India - Class - 10', 'India and the Contemporary World-II - Class - 10', 'Understanding Economic Development - Class -10',
'Democratic Politics-II - Class - 10', 'Physics(Part 1 & 2) - Class - 11', 'Chemistry (Part 1 & 2) - Class - 11', 'Maths - Class - 11', 'Biology - Class - 11', 'Accountancy(Part 1 & 2) - Class -11', 
'Business Studies - Class -11', 'Indian Economic Development - Class -11', 'Geography - Class - 11', 'History - Class -11','Political Science Books - Class -11', 'Pschology - Class -11', 'Sociology - Class -11', 
'Economics - Class -11', 'Hindi - Class -11', 'English - Class -11', 'Physics(Part 1 & 2) - Class - 12', 'Chemistry(Part1 &2) - Class -12', 'Maths(Part1 & 2) - Class - 12',  'Biology - CLass - 12', 
'Accountancy(Part 1& 2) - Class - 12', 'Business Studies(Part 1 & 2) - Class - 12', 'Economics(Micro & Macro) - Class -12','Geography - Class - 12', 'History(Part 1, 2 & 3) - Class - 12', 'Political Science - Class -12',
'Psychology - Class - 12', 'Sociology - Class - 12', 'Hindi - Class - 12', 'English - Class - 12']) 
    student = Student()
    while(True):
        welcomeMsg = ''' 
        
                                    ~~~~~~~~~~~~~   Welcome to central Library   ~~~~~~~~~~~~~

                                        Please choose an option:
                                            0. Check availablility classes for book issue
                                            1. Listing all the books
                                            2. Request a book
                                            3. Return a book
                                            4. Add a book
                                            5. Exit the Library
'''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        if a == 0:
            central.displayAvailableclasses()                
        elif a == 1:
            centralLibrary.displayAvailablebooks()    
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 5:
            print("Thanks for choosing Central Library! Have a great day ahead")
            break
        elif a == 4:
            centralLibrary.addBook(student.addBook())
            print("The book has successfully added in the library. Thank you for your help!!!!")
        else:
            print('''Invalid Choice!!!! 
            Please try again''')
        