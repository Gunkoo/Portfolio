class Guest:
    """
    Represents a hotel guest

    Attributes:
        name (str) -> The name of the guest
        contact_info (str) -> The contact information for the guest
        
    """
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"{self.name} {self.contact_info}"
