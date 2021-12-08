from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

members_blueprint = Blueprint("members", __name__)


# show all members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)


# show all id of memmbers
@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    gym_classes = []
    if member is not None:
        gym_classes = gym_class_repository.select_classes(member)
    return render_template("members/show.html", member=member, gym_classes=gym_classes)



#edit a member/id and post
@members_blueprint.route("/members/edit/<id>")
def edit(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member=member)

@members_blueprint.route("/members/create", methods=['POST'])
def create():
    member = Member(request.form['first_name'],request.form['last_name'],request.form['age'], 0)
    member_repository.save(member)
    return redirect('/members')




#delete a specific member based on id
@members_blueprint.route("/members/remove/<id>")
def delete(id):
    member_repository.delete(id)
    return redirect('/members')


#add a new member
@members_blueprint.route("/members/add")
def add():
    return render_template("members/add.html")
    


#post a saved member
@members_blueprint.route("/members/save", methods=['POST'])
def save():
    member = Member(request.form['first_name'],request.form['last_name'],request.form['age'],request.form['id'])
    member_repository.edit(member)
    return redirect('/members')

