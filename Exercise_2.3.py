#Create a class named Book with an __init__ method. Inside the __init__ method, create the instance variables isbn, title, author, publisher, pages, price, copies.

#Create these four instance objects from this class.

#book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
#book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
#book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
#book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
#Write a method display that prints the isbn, title, price and number of copies of the book.


# For the Book class that you have created, write a method named in_stock that returns True if number of copies is more than zero, otherwise it returns False.

#Create another method named sell that decreases the number of copies by 1 if the book is in stock, otherwise it prints the message that the book is out of stock.


class Book:
    def __init__(personal,isbn, title,author,publisher,pages,price,copies):
        personal.isbn = isbn
        personal.title = title
        personal.author = author
        personal.publisher = publisher
        personal.pages = pages
        personal.price = price
        personal.copies = copies
   
    def display(personal):
        print(personal.title)
        print(f'ISBN : {personal.isbn}')
        print(f'Price : {personal.price}')
        print(f'Number of copies : {personal.copies}')
        print('.' * 50)

    def in_stock(personal):
        return True if personal.copies > 0 else False
    
    def sell(personal):
        if personal.in_stock():
            personal.copies     -= 1
        else:
            print("The book is out of stock")

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
book2.display()
book3.display()
book4.display()

book3.sell()
book3.sell()
book3.sell()
book3.sell()
book3.sell()
book3.sell()