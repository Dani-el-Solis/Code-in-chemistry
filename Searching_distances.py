####This code works for any type of file in which you have columns of coordinates separate by blankspaces, the principal difference is that for this case###
####the identifier (in this case C and Cx) must be upon the line that you want to analize (LINE OF COORDINATES)####
###Made By Luis Daniel Solis, TCCM student. 2023

import numpy as np

# First, open the file in the lecture mode, in this code for the file .txt type
with open('REVCON2.txt', 'r') as file:
    # Leer el contenido del archivo
    lines = file.readlines()

    # Made lists to keep in them the coordinates of each type of atom
    coordinates_c = []
    coordinates_cx = []

    # Processing the information
    for line in lines:
        # Deleting the blankspaces at the beggining and end of each line
        line = line.strip()

        if line.startswith('C'):
            # Split the lines in parts and getting the coordinates
            parts = line.split()
            type = parts[0]  # Tipo de átomo ('C' o 'Cx')
            coordinates = list(map(float, parts[1:4]))  # Coordenadas x, y, z

            # Store the coordinates in the corresponding list
            if type == 'C':
                coordinates_c.append(coordinates)
            elif type == 'Cx':
                coordinates_cx.append(coordinates)

    # Calculating the distance between C and Cx
    for coord_c in coordinates_c:
        for coord_cx in coordinates_cx:
            distance = np.linalg.norm(np.array(coord_c) - np.array(coord_cx))
            
            # Print the distances minors or equal to 7
            if distance <= 7:
                print(f'Distancia entre C y Cx: {distance}')
