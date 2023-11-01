class Borrower:
    def __init__(self,username,password,confirm_password,email,location):
        self.username=username
        self.password=password
        self.confirm_password=confirm_password
        self.email=email
        self.location=location
    
    borrower_details=[]   

    def save_details(self):
        Borrower.borrower_details.append(self)
    
    def delete_details(self):
        Borrower.borrower_details.remove(self)
        