from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import gym_class
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes = gym_classes)


@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    gym_class = gym_class_repository.select(id)
    members = []
    if gym_class is not None:    
        members = member_repository.select_members(gym_class)
    return render_template("gym_classes/show.html", gym_class=gym_class, members=members)




@gym_classes_blueprint.route("/gym_classes/add")
def add():
    return render_template("gym_classes/add.html")

@gym_classes_blueprint.route("/gym_classes/create", methods=['POST'])
def create():
    gym_class = Gym_class(request.form['name'],request.form['date'],request.form['duration'])
    gym_class_repository.save(gym_class)
    return redirect('/gym_classes')



#    dont forget delete - below!
@gym_classes_blueprint.route("/gym_classes/remove/<id>")
def delete(id):
    gym_class_repository.delete(id)
    return redirect('/gym_classes')


#edit a gym class

@gym_classes_blueprint.route("/gym_classes/edit/<id>")
def edit(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/edit.html", gym_class=gym_class)

@gym_classes_blueprint.route("/gym_classes/save", methods=['POST'])
def save():
    gym_class = Gym_class(request.form['name'],request.form['date'],request.form['duration'],request.form['id'])
    gym_class_repository.edit(gym_class)
    return redirect('/gym_classes')




