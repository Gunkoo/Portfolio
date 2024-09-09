from room import Room
class Reservation:
    """
    Represents a reservation for a guest

    Attributes:
        guest (Guest) -> The guest making the reservation
        room (Room) -> The room being reserved
        check_in_date (str) -> The check-in date for the reservation
        check_out_date (str) ->  The check-out date for the reservation

    Methods:
        create_reservation() -> Creates a reservation for the guest and room
        update_reservation(new_check_in_date, new_check_out_date) -> Updates the reservation dates
        cancel_reservation() -> Cancels the reservation for the room
    """
    def __init__(self,guest,room,check_in_date,check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def __str__(self):
        return f"{self.guest} has reservation for {self.room}. {self.check_in_date} - {self.check_out_date}"    
    
    def create_reservation(self):
        if Room.check_availability(self.room):   
            Room.book_room(self.room,self.guest,self.check_in_date,self.check_out_date)
        else:
            print(f"{Room} is not available")
    
    def update_reservation(self,new_check_in_date,new_check_out_date):
        """
        Args:
            new_check_in_date (str) -> The new check-in date
            new_check_out_date (str) -> The new check-out date
        """
        Room.cancel_booking(self.room)
        Room.book_room(self.room,self.guest,new_check_in_date,new_check_out_date)

    def cancel_reservation(self):
        Room.cancel_booking(self.room)