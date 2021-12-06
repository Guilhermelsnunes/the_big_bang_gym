from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, gym_class_id ) VALUES ( %s, %s ) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

# SELECT
#   b.id,
#   b.member_id,
#   b.gym_class_id,
#   m.first_name,
#   m.last_name,
#   m.age,
#   g.name,
#   g.date,
#   g.duration
# FROM bookings b
# JOIN members m ON m.id = b.member_id
# JOIN gym_classes g ON g.id = b.gym_class_id

#        member = Member(row['first_name'], row ['last_name'], row ['age'], row['member_id'])
#        gym_class = Gym_class(row['name'], row['date'], row['duration'], row['gym_class_id'] )
#        booking = Booking(member, gym_class, row['id'])
#
 

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings






#don't think we need a delete all...
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


#delete by id 
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
