from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_class(name, date, duration) VALUES ( %s, %s, %s ) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.duration]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class


def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['date'], row['duration'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes 


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['date'], result['duration'], result['id'] )
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def gym_classes(member):
    gym_classes = []

    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN booking ON bookings.gym_class_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Gym_class(row['name'], row['date'], row['duration'], row ['id'])
        gym_classes.append(gym_class)

    return gym_classes
