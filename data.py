# data.py

PLACEHOLDER_IMAGE = "Images/_placeholder.jpg"

SPECIES_DATA = {
    "Neocaridina shrimp": {
        "Category": "Shrimp",
        "Image": "Images/neocaridina_davidi_yellow_neon.jpg",
        "Temperature (°C)": (16, 26),
        "pH": (6.5, 8.0),
        "Hardness (dGH)": (4, 12),
        "Min Tank Size (L)": 20,
    },
    "Amano shrimp": {
        "Category": "Shrimp",
        "Temperature (°C)": (20, 25),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (1, 12),
        "Min Tank Size (L)": 40,
    },
    "Honey Gourami": {
        "Category": "Fish",
        "Image": "Images/honey_gourami.jpg",
        "Temperature (°C)": (20, 30),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (5, 15),
        "Min Tank Size (L)": 40,
        "Min groupsize": 2,
    },
    "Trichogaster leeri": {
        "Category": "Fish",
        "Other names": "Mosaikfadenfisch",
        "Temperature (°C)": (24, 28),
        "pH": (5.5, 7.5),
        "Hardness (dGH)": (0, 12),
        "Min Tank Size (L)": 250,
        "Min groupsize": 2
    },
    "Palacsinta algázó": {
        "Category": "Fish",
        "Temperature (°C)": (18, 24),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (4, 25),
        "Min Tank Size (L)": 80,
    },
    "Otocinclus": {
        "Image": "Images/otocinclus_sp.jpg",
        "Category": "Fish",
        "Temperature (°C)": (20, 28),
        "pH": (5.5, 7.5),
        "Hardness (dGH)": (3, 15),
        "Min Tank Size (L)": 80,
    },
    "Pfeffersalmler": {
        "Category": "Fish",
        "Temperature (°C)": (20, 28),
        "pH": (5.0, 7.0),
        "Hardness (dGH)": (2, 10),
        "Min Tank Size (L)": 40,
        "Min Tank Size (L)": 80,
    },
    "Rotkopfsalmler": {
        "Category": "Fish",
        "Temperature (°C)": (23, 30),
        "pH": (5.5, 7.5),
        "Hardness (dGH)": (2, 15),
        "Min Tank Size (L)": 160,
        "Min Tank lenght (cm)": 100,
        "Min groupsize": 10
    },
    "Phenacogrammus interruptus": {
        "Category": "Fish",
        "Other names": "Blauer kongosalmler",
        "Temperature (°C)": (23, 27),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (2, 12),
        "Carbon hardness (dKH)": (3, 8),
        "Min Tank Size (L)": 300,
        "Min Tank lenght (cm)": 120,
        "Min groupsize": 10
    },
    "Blue Neon Tetra": {
        "Category": "Fish",
        "Image": "Images/blue_neon_tetra.jpg",
        "Temperature (°C)": (21, 28),
        "pH": (5.0, 7.5),
        "Hardness (dGH)": (2, 12),
        "Min Tank Size (L)": 60,
        "Min groupsize": 15,
    },
    "Pencil tetra": {
        "Category": "Fish",
        "Temperature (°C)": (22, 27),
        "pH": (6.0, 7.0),
        "Hardness (dGH)": (2, 12),
        "Min Tank Size (L)": 60,
        "Min Tank lenght (cm)": 60,
    },
    "Schwarzer neon": {
        "Category": "Fish",
        "Temperature (°C)": (21, 28),
        "pH": (6.0, 7.0),
        "Hardness (dGH)": (1, 10),
        "Min Tank Size (L)": 80,
        "Min Tank lenght (cm)": 80,
        "Min groupsize": 10,
    },
    "Boraras utoptalmodes": {
        "Category": "Fish",
        "Temperature (°C)": (22, 26),
        "pH": (5.0, 7.0),
        "Hardness (dGH)": (3, 10),
        "Min Tank Size (L)": 60,
    },
    "Posthornschnecke": {
        "Category": "Other",
        "Temperature (°C)": (18, 28),
        "pH": (6.5, 8.0),
        "Hardness (dGH)": (5, 20),
        "Min Tank Size (L)": 10,
    },
     "Apistogramma Tefe": {
         "Category": "Fish",
        "Temperature (°C)": (22, 28),
        "pH": (5.5, 7.0),
        "Hardness (dGH)": (2, 12),
        "Min Tank Size (L)": 100,
        "Min Tank lenght (cm)": 75,
    },
    "Danio margaritatus (Microrasboras galaxy)": {
        "Category": "Fish",
        "Other names": "Perlhuhnbärbling",
        "Temperature (°C)": (18, 25),
        "pH": (6.5, 7.5),
        "Hardness (dGH)": (5, 20),
        "Min Tank Size (L)": 60,
        "Min Tank lenght (cm)": 75,
        "Min groupsize": 12
    },
    "Apistogramma cacatuoides": {
        "Category": "Fish",
        "Other names": "Kakadu-Zwergbuntbarsch",
        "Temperature (°C)": (23, 29),
        "pH": (5.5, 7.5),
        "Hardness (dGH)": (8, 12),
        "Carbon hardness (dKH)": (3, 8),
        "Min Tank Size (L)": 150,
        "Min groupsize": 2
    },
     "Scalar Pterophyllum scalare Santa Isabel": {
         "Category": "Fish",
        "Temperature (°C)": (24, 30),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (2, 10),
        "Min Tank Size (L)": 200,
        "Min Tank lenght (cm)": 120,
        "Min Tank height (cm)": 55
    },
    "Puntius pentazona": {
        "Category": "Fish",
        "Other names": "Fünfgürtelbarbe",
        "Temperature (°C)": (24, 27),
        "pH": (5.5, 6.8),
        "Hardness (dGH)": (5, 12),
        "Carbon hardness (dKH)": (0, 4),
        "Min Tank Size (L)": 150,
        "Min groupsize": 10
    },
    "Mikrogeophagus ramirezi": {
        "Category": "Fish",
        "Other names": "Schmetterlingsbunbarsch",
        "Temperature (°C)": (25, 30),
        "pH": (6.0, 7.0),
        "Hardness (dGH)": (2, 20),
        "Carbon hardness (dKH)": (0, 12),
        "Min Tank Size (L)": 60,
        "Min groupsize": 2
    },

    
    



}