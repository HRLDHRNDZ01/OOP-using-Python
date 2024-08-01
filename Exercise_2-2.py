class Book:
    def __init__(personal,  isbn, title, author, publisher, pages, price, copies):
        personal.isbn = isbn       
        personal.title = title
        personal.author = author
        personal.publisher = publisher
        personal.pages = pages
        personal.price = price
        personal.copies = copies

    def display(personal):
        details = (
            f"ISBN: {personal.isbn}\n"
            f"Title: {personal.title}\n"
            f"Author: {personal.author}\n"
            f"Publisher: {personal.publisher}\n"
            f"Pages: {personal.pages}\n"
            f"Price: {personal.price}\n"
            f"Copies: {personal.copies}\n"
            )
        return details
    
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200, 6)

book1_details = book1.display()
book2_details = book2.display()
book3_details = book3.display()
book4_details = book4.display()

print(book1_details)
print(book2_details)
print(book3_details)
print(book4_details)

