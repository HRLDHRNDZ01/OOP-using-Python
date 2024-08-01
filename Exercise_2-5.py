class Book:
    
    def __init__(personal, isbn, title, author, publisher, pages, price, copies):
        personal.isbn = isbn
        personal.title = title
        personal.author = author
        personal.publisher = publisher
        personal.pages = pages
        personal._price = price  # Store the price in a private variable
        personal.copies = copies
   
    def display(personal):
        print(personal.title)
        print(f'ISBN : {personal.isbn}')
        print(f'Price : {personal.price}')
        print(f'Number of copies : {personal.copies}')
        print('.' * 50)

    @property
    def price(personal):
        return personal._price
    
    @price.setter
    def price(personal, new_price):
        if 50 <= new_price <= 1000:
            personal._price = new_price
        else:
            raise ValueError("Price must be between 50 and 1000")

book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

book1.display()
book2.display()
book3.display()
book4.display()
