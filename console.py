import pdb
from models.gym_class import Gym_class
from models.member import Member
from models.booking import Booking

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()



member1 = Member('Sheldon', 'Cooper', 31)
member_repository.save(member1)

member2 = Member('Leonard', 'Hofstadter', 34)
member_repository.save(member2)

member3 = Member('Howard', 'Wolowitz', 28)
member_repository.save(member3)

member4 = Member('Rajesh', 'Koothrappali', 30)
member_repository.save(member4)



gym_class1 = Gym_class('Brazilian Jiu_Jitsu', '21/11/2021', 60)
gym_class_repository.save(gym_class1)

gym_class2 = Gym_class('Muay-Thai', '25/11/2021', 60)
gym_class_repository.save(gym_class2)

gym_class3 = Gym_class('Bando', '30/11/2021', 60)
gym_class_repository.save(gym_class3)

gym_class4 = Gym_class('Capoeira', '27/11/2021', 60)
gym_class_repository.save(gym_class4)



booking1 = Booking(member1, gym_class1)
booking_repository.save(booking1)

booking2 = Booking(member2, gym_class2)
booking_repository.save(booking2)

booking3 = Booking(member3, gym_class3)
booking_repository.save(booking3)

booking4 = Booking(member4, gym_class4)
booking_repository.save(booking4)



print(gym_class_repository.gym_classes(member1))

pdb.set_trace()



