from room import Room
from guest import Guest
from reservation import Reservation

room1 = Room(1,"single",50,"available")
room2 = Room(2,"double",100,"available")
room3 = Room(3,"double",150,"available")
room4 = Room(4,"single",80,"booked")
room5 = Room(5,"single",30,"available")

all_rooms = [room1,room2,room3,room4,room5]

guest1 = Guest("Peter","example@examplemail.com")
new_reservation = Reservation(guest1,room1,"25.10.2024","29.10.2024")



print(room1)
print(guest1)
print(new_reservation)


print(Room.search_for_room(all_rooms,150,"single"))
new_reservation.create_reservation()