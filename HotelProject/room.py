class Room:
    """
    Represents a hotel room

    Attributes: 
        |room_number (int) -> Identifier for the room
        |room_type (str) -> Type of room (single, double)
        |price (float) -> Price of the room per night
        |booking_status (str) -> Current status of the room (available, booked)
        |guest_info (list) -> Information about guest that booked this room
        |dates (list -> List of check-in and check-out dates
        
    Methods:
        |check_availability() -> Checks if the room is available for booking
        |book_room(guest, check_in_date, check_out_date) -> Books the room for a guest
        |cancel_booking() -> Cancels the booking for the room
        |search_for_room(rooms, price, room_type) -> Searches for available rooms based on price and type

    """
    def __init__(self,room_number,room_type,price,booking_status):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.booking_status = booking_status
        self.guest_info = []
        self.dates = []

    def __str__(self):
        return f"{self.room_type} room {self.room_number} costs {self.price} is {self.booking_status} "

    def check_availability(self):
        """
        returns (bool) depending on availability    
        """
        if self.booking_status == "available":
            return True
        else:
            return False

    def book_room(self,guest,check_in_date,check_out_date):
        """
        Args:
            guest (Guest) -> The guest who is booking the room
            check_in_date (str) -> The check-in date for the booking
            check_out_date (str) -> The check-out date for the booking
        """
        if self.booking_status == "available":
            self.booking_status = "booked"
            self.guest_info.append(guest)
            self.dates.append((check_in_date,check_out_date))
        else:
            print(f"You cant book room {self.room_number} because it already booked")

    def cancel_booking(self):
        if self.booking_status == "booked":
            self.booking_status == "available"
            self.guest_info = []
        else:
            print(f"Room {self.room_number} is not booked")

    def search_for_room(rooms,price,type):
        """
        Args:
            rooms (list) -> A list of Room objects to search through
            price (float) -> The maximum price for the room
            room_type (str) -> The type of room to search for

        """
        found_rooms = []
        for room in rooms:
            if room.price <= price and room.room_type == type and Room.check_availability(room):
                found_rooms.append(room.room_number)
        return found_rooms
    



