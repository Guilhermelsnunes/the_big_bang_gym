from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

bookings_blueprint = Blueprint("bookings", __name__)



@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

# NEW
# GET '/bookings/new'
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_task():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/new.html", members = members, gym_classes = gym_classes)

# CREATE
# POST '/bookings'
@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect('/bookings')


# DELETE - it worked!
@bookings_blueprint.route("/bookings/remove/<id>/")
def delete(id):
    booking_repository.delete(id)
    return redirect('/bookings')



#   ADD new and save/post - NOT SAVING!

@bookings_blueprint.route("/bookings/add")
def add():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/add.html", members=members, gym_classes=gym_classes)

@bookings_blueprint.route("/bookings/create", methods=['POST'])
def create():
    #member = member_repository.select(request.form['member_id'])
    #gym_class = gym_class_repository.select(request.form['gym_class_id'])
    #booking = Booking(member, gym_class)
    #booking_repository.save(booking)

    booking_repository.save(request.form['member_id'], request.form['gym_class_id'])
    return redirect('/bookings')



#  EDIT a booking and post  -  ver o select q ta branco!

@bookings_blueprint.route("/bookings/edit/<id>")
def edit(id):
    booking = booking_repository.select(id)
    return render_template("bookings/edit.html", booking=booking)


@bookings_blueprint.route("/bookings/save", methods=['POST'])
def save():
    booking = Booking(request.form['member_id'],request.form['gym_class_id'],)
    booking_repository.edit(booking)
    return redirect('/booking')