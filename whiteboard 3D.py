# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 45},
            {"day": "Sábado", "temp": 58},
            {"day": "Domingo", "temp": 72}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 46},
            {"day": "Martes", "temp": 59},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 49},
            {"day": "Domingo", "temp": 63}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 57},
            {"day": "Martes", "temp": 51},
            {"day": "Miércoles", "temp": 55},
            {"day": "Jueves", "temp": 52},
            {"day": "Viernes", "temp": 58},
            {"day": "Sábado", "temp": 51},
            {"day": "Domingo", "temp": 55}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 45},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 49},
            {"day": "Viernes", "temp": 54},
            {"day": "Sábado", "temp": 67},
            {"day": "Domingo", "temp": 41}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 65},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 48},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 52},
            {"day": "Sábado", "temp": 56},
            {"day": "Domingo", "temp": 54}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 84},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 70}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)