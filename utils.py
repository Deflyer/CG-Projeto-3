# Useful functions that dont have enough semantic to be in another module.

import glm
from OpenGL.GL import *
from PIL import Image

def load_obj_to_glm_array(filepath):
    '''
    Returns the vertexes of a given OBJ file.
    '''

    vertices = []
    normals = []
    texcoords = []
    faces = []

    with open(filepath, 'r') as file:

        for line in file:
            parts = line.strip().split()
            if not parts:
                continue

            # Vertexes.
            if parts[0] == 'v':
                vertices.append([float(x) for x in parts[1:4]])
            
            # Normals.
            elif parts[0] == 'vn':
                normals.append([float(x) for x in parts[1:4]])
            
            # Texture coordinates.
            elif parts[0] == 'vt':
                texcoords.append([float(x) for x in parts[1:3]])

            # Faces.
            elif parts[0] == 'f':
                face = []
                for vertex in parts[1:]:
                    v, vt, vn = (int(i) - 1 for i in vertex.split('/'))
                    face.append((v, vt, vn))
                faces.append(face)

    # Creating the array in glm.array(glm.float32) format.
    glm_vertices = []
    for face in faces:
        for v, vt, vn in face:
            glm_vertices.extend(vertices[v])
            glm_vertices.extend(normals[vn])
            glm_vertices.extend(texcoords[vt])

    # Coverting to glm array and returning.
    return glm.array(glm.float32, *glm_vertices)

def loadTexture(path: str) -> int:
    '''
    Loads a texture of a given file (PNG, JPG).
    '''

    textureID = glGenTextures(1)
    
    try:
        
        img = Image.open(path)

        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        img_width = img.size[0]
        img_height = img.size[1]
        image_data = img.convert("RGBA").tobytes("raw", "RGBA",0,-1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        img.close()

    except:

        print("Texture failed to load at path: " + path)

    return textureID