import glm

def load_obj_to_glm_array(filepath):
    vertices = []
    normals = []
    texcoords = []
    faces = []

    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue

            # Vértices
            if parts[0] == 'v':
                vertices.append([float(x) for x in parts[1:4]])
            
            # Normais
            elif parts[0] == 'vn':
                normals.append([float(x) for x in parts[1:4]])
            
            # Coordenadas de textura
            elif parts[0] == 'vt':
                texcoords.append([float(x) for x in parts[1:3]])

            # Faces
            elif parts[0] == 'f':
                face = []
                for vertex in parts[1:]:
                    v, vt, vn = (int(i) - 1 for i in vertex.split('/'))
                    face.append((v, vt, vn))
                faces.append(face)
        # Criando o array no formato glm.array(glm.float32)
    glm_vertices = []
    for face in faces:
        for v, vt, vn in face:
            glm_vertices.extend(vertices[v])
            glm_vertices.extend(normals[vn])
            glm_vertices.extend(texcoords[vt])
    # Convertendo para glm array
    return glm.array(glm.float32, *glm_vertices)

def get_cubes_positions():
    # positions all containers
    cubePositions = [
        glm.vec3(-2.8, -0.8, -6.8),
        glm.vec3( 2.7, -0.95, -7.8),
        glm.vec3( 0.0 , -1.0, 2.0),
        glm.vec3( 20.0, 2.2, -6.0),
        glm.vec3( 2.7, -1.0, -20.0),
        glm.vec3( 0.0, -1.0, 0.0),
        glm.vec3( 0.0, -1.0, -10.0),
        glm.vec3(-2.8, -0.8, -6.8),
        glm.vec3( 0.0, 50.0, 0.0),
        glm.vec3( 0.0, -45, 0.0)
    ]
    
    return cubePositions

def get_lights_positions():
    # positions of the point lights
    pointLightPositions = [
        glm.vec3( -2.8, -0.8, -6.8),
        glm.vec3( 2.3, -3.3, -4.0),
        glm.vec3(-4.0,  2.0, -12.0),
        glm.vec3( 0.0,  0.0, -3.0)
    ]

    return pointLightPositions