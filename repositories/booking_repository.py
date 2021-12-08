from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(booking):
    check_sql = "SELECT * FROM bookings WHERE member_id = %s AND gym_class_id = %s"
    values = [booking.member.id, booking.gym_class.id]
    check_result = run_sql( check_sql, values )
    if len(check_result) ==  0:   
        sql = "INSERT INTO bookings ( member_id, gym_class_id ) VALUES ( %s, %s ) RETURNING id"
        results = run_sql( sql, values )
        booking.id = results[0]['id']
        return booking

def save(member_id, gym_class_id):
    check_sql = "SELECT * FROM bookings WHERE member_id = %s AND gym_class_id = %s"
    values = [member_id, gym_class_id]
    check_result = run_sql( check_sql, values )
    if len(check_result) ==  0:  
        sql = "INSERT INTO bookings ( member_id, gym_class_id ) VALUES ( %s, %s ) RETURNING id"
        results = run_sql( sql, values )
        return results[0]['id']


def select_all():
    bookings = []


 

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
