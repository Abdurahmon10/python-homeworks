class BookNotFound(BaseException):
    def __init__(self, message : str, *args, **kwargs):
        self.message = message
        super().__init__(message, args, kwargs)
    

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return f"{self.message}"
    
class BookAlreadyBorrowedException(BaseException):
    def __init__(self,message:str,*args,**kwargs):
        self.message=message
        super().__init__(message, args, kwargs)
    def __str__(self):
        return f"{self.message}"
    def __repr__(self):
        return f"{self.message}"

class MemberLimitExceededException(BaseException):

    def __init__(self,message:str,*args,**kwargs):
        self.message=message
        super().__init__(message,args,kwargs)
    def __str__(self):
        return f"{self.message}"
    def __repr__(self):
        return f"{self.message}"

class MemberNotFoundException(BaseException):

    def __init__(self,message:str,*args,**kwargs):
        self.message=message
        super().__init__(message,args,kwargs)
    def __str__(self):
        return f"{self.message}"
    def __repr__(self):
        return f"{self.message}"









class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.__title=title
        self.__author=author
        self.__is_borrowed=is_borrowed


    
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,title):
        self.__title=title


    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self,author):
        self.__author=author
    

    @property
    def is_borrowed(self):
        return self.__is_borrowed
    @is_borrowed.setter
    def is_borrowed(self,is_borrowed):
        self.__is_borrowed=is_borrowed
    


class Member:
    def __init__(self,name):
        self.__name=name
        self.__borrowed_books=[]
        self.__num_borrowed_books=0
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    @borrowed_books.setter
    def borrowed_books(self,borrowed_books):
        self.__borrowed_books=borrowed_books
    
    @property
    def num_borrowed_books(self):
        return self.__num_borrowed_books
    @num_borrowed_books.setter
    def num_borrowed_books(self,num_borrowed_books):
        self.__num_borrowed_books=num_borrowed_books

    def add_book(self,title):
        self.__borrowed_books.append(title)
        self.__num_borrowed_books+=1
    
    def return_book(self,title):
        if title in self.__borrowed_books:
            self.__borrowed_books.remove(title)
            self.__num_borrowed_books-=1



class Library:
    def __init__(self):
        self.__members=dict()
        self.__books=dict()
        self.maxbb=4
    

    def addMember(self):
        name=input("Enter the name of the new member:\n")
        member=Member(name)
        self.__members[name]=member
        
    
    def addBook(self):
        title=input("Enter the title of the new book:\n")
        author=input("Enter the name of the author:\n")

        book=Book(title,author)
        self.__books[title]=book
    def display(self):
        print("members")
        for k in self.__members.keys():
            print(k)
        print("books")
        for k in self.__books.keys():
            print(k)

    def find_member(self,name):
        if(not(name in self.__members.keys())):
            raise MemberNotFoundException("Member was not found")

    def find_book(self,title):
        if(not(title in self.__books.keys())):
            raise BookNotFound("The book with this title was not found")
    def check(self,title):
        if(self.__books[title].is_borrowed):
            raise BookAlreadyBorrowedException("The book is already borrowed")
    def maxb(self,name):
        if(self.__members[name].num_borrowed_books>=self.maxbb):
            raise MemberLimitExceededException("You have reached your limit")


    def borrowing(self):
        name=input("Enter the name of the member who is borrowing:\n")
        try:
            self.find_member(name)
        except MemberNotFoundException as m:
            print(m)
        else:
            title=input("Enter the title of the book being borrowed:\n")
            try:
                self.find_book(title)
            except BookNotFound as m:
                print(m)
                return False
            else:
                try:
                    self.check(title)
                except BookAlreadyBorrowedException as m:
                    print(m)
                    return False
                else:
                    try:
                        self.maxb(name)
                    except MemberLimitExceededException as m:
                        print(m)
                        return False
                    else:
                        self.__members[name].add_book(title)
                        #self.__members[name].num_borrowed_books=(self.__members[name].num_borrowed_books+1)
                        return True
    def return_book (self):
        name=input("Enter the name of the member who is returning the books:\n")
        title=input("Enter the title of the book being returned:\n")
        if(not(name in self.__members.keys())or not(title in self.__books.keys())):
            return False
        self.__members[name].return_book(title)
        return True



            
                

my_lib=Library()

#menu

while True:
    choice=int(input("Choose an option:\n1. adding a member\n2. adding a book\n3. displaying a everything\n4. borrow\n5. return\n6. exit\n"))
    if(choice==1):
        my_lib.addMember()
    elif(choice==2):
        my_lib.addBook()
    elif(choice==3):
        my_lib.display()
    elif(choice==4):
        succes=my_lib.borrowing()
        if(succes):
            print("process completed successfully.")
    elif(choice==5):
        succes=my_lib.return_book()
        if(succes):
            print("process completed successfully.")
    else:
        break


print("Bye")









    
        







            

