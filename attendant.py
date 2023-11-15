class Attendant:
    def __init__(self, username,confirm_username,email,store_location): 
        self.username=username
        self.confirm_username=confirm_username
        self.email=email
        self.store_location=store_location

    attendant_details=[]

    def save_details (self):
        Attendant.attendant_details.append(self)

    def delete_details (self):
        Attendant.attendant_details.remove(self)
        
        
