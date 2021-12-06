from db.run_sql import run_sql
from models import gym_class
from models.gym_class import Gym_class
from models.member import Member

def save(member):
    sql = "INSERT INTO members( first_name, last_name, age ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [member.first_name,member.last_name,member.age]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def edit(member):
    sql = "UPDATE members SET first_name=%s, last_name=%s, age=%s WHERE id=%s"
    values = [member.first_name    ,member.last_name    ,member.age    ,member.id]
    results = run_sql (sql, values)
    return results



def select_all():
    members = []

    sql = "SELECT * FROM members ORDER BY last_name, first_name"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row ['last_name'], row ['age'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['age'], result['id'])
    return member


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def select_members(gym_class):
    members = []

    sql = "SELECT m.* FROM bookings b JOIN members m ON m.id = b.member_id WHERE gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row ['last_name'], row ['age'], row['id'])
        members.append(member)
    return members

