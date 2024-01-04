"""Seed file to make sample data for pets db."""

from models import Pet, db

# Drop all tables
db.drop_all()

# Create all tables
db.create_all()

# clean reset the database
# db.engine.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
woofly = Pet(name='Woofly', species="Dog", photo_url="https://lh3.googleusercontent.com/a/ACg8ocKCaB0i3DZctm3GL57I9ywQnnNe4nL_ix9mM8WBdubKIvE=s324-c-no", age=23, notes="Best dog ever", available=True)
porchetta = Pet(name='Porchetta', species="Porcupine", image_url="https://cdn.vectorstock.com/i/1000x1000/15/40/blank-profile-picture-image-holder-with-a-crown-vector-42411540.webp", age=12, notes="Best porcupine ever", available=False)
snargle = Pet(name='Snargle', species="Cat", image_url="https://images.unsplash.com/photo-1628563694622-5a76957fd09c?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", age=1, notes="Best cat ever", available=False)

# Add new objects to session
db.session.add_all([woofly, porchetta, snargle])

# Commit
db.session.commit()