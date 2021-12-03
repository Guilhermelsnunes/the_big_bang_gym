from db.run_sql import run_sql
from models import gym_class
from models.gym_class import Gym_class
from models.member import Member

def save(member):
    sql = "INSERT INTO member( first_name, last_name, age ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [member.first_name]
    values = [member.last_name]
    values = [member.age]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row ['last_name'], row ['age'], row['id'])
        members.append(member)
    return members


def select(id):
    user = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['age'], result['id'])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def members(location):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN gym_glasses ON gym_classes.member_id = members.id WHERE gym_class_id = %s"
    values = [gym_class.id]
    
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row ['last_name'], row ['age'], row ['id'])
        members.append(member)

    return members