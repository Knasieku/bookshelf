class Books:
    def __init__(self,title,year_published,author,publishing_house):
        self.title=title
        self.year_published=year_published
        self.author=author
        self.publishing_house=publishing_house
    
    book_details=[]

    def save_books (self):
        Books.book_details.append(self)

    def delete_books (self):
        Books.book_details.remove(self)
    
    
        
    