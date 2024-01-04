from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPet(FlaskForm):
    """ Form for adding pets. """

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField(
        "Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ("porcupine", "Porcupine")])
    
    photo_url = StringField("Photo URL", validators=[URL(require_tld=False, message="The URL is not valid."),
                            Optional(strip_whitespace=True)])
    
    age = IntegerField("Age",
                       validators=[NumberRange(min=0, max=30, message="Age should be between 0 - 30"),
                       Optional(strip_whitespace=True)])
    
    notes = StringField("Notes", validators=[Optional(strip_whitespace=True)])

class EditPet(FlaskForm):
    """ Form for editing pets. """

    photo_url = StringField("Photo URL", validators=[URL(require_tld=False, message="The URL is not valid."),
                            Optional(strip_whitespace=True)])
    
    notes = StringField("Notes", validators=[Optional(strip_whitespace=True)])

    available = BooleanField("Availability", default=True)
