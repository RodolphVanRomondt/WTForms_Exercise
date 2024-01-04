"""Adopt application."""

from flask import Flask, render_template,  redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "springboard"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_route():
    """ Show homepage / List of pets. """

    pets = Pet.query.all()

    return render_template("pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def pet_add():
    """ Show edit page. """

    pet = AddPet()

    if pet.validate_on_submit():
        name = pet.name.data
        species = pet.species.data
        photo_url = pet.photo_url.data
        age = pet.age.data
        notes = pet.notes.data

        pet_save = Pet(name=name, species=species, photo_url=photo_url,
                       age=age, notes=notes)
        
        db.session.add(pet_save)
        db.session.commit()

        return redirect("/")

    return render_template("pet_form.html", pet=pet)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_display_edit(pet_id):
    """ Show details info about a pet, or edit it. """

    pet_form = EditPet()
    pet = Pet.query.get(pet_id)

    if pet_form.validate_on_submit():
        
        pet.photo_url = pet_form.photo_url.data
        pet.notes = pet_form.notes.data
        pet.available = pet_form.available.data

        db.session.commit()

        return redirect(f"/{ pet_id}")

    return render_template("pet_details.html", pet=pet, form=pet_form)