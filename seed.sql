-- from the terminal run:
-- psql < seed.sql

DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INTEGER,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets (name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'Dog', 'https://images.unsplash.com/photo-1628563694622-5a76957fd09c?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 23, 'Best dog ever', TRUE),
  ('Porchetta', 'Mouse', 'https://lh3.googleusercontent.com/a/ACg8ocKCaB0i3DZctm3GL57I9ywQnnNe4nL_ix9mM8WBdubKIvE=s324-c-no', 12, 'Best mouse ever', FALSE),
  ('Snargle', 'Cat', 'https://cdn.vectorstock.com/i/1000x1000/15/40/blank-profile-picture-image-holder-with-a-crown-vector-42411540.webp', 1, 'Best cat ever', TRUE);
