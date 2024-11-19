import glm
from OpenGL.GL import *
from PIL import Image

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
                    print(str (v) + " " + str(vn))
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

# function that loads and automatically flips an image vertically
LOAD_IMAGE = lambda name: Image.open(name).transpose(Image.FLIP_TOP_BOTTOM)

def loadTexture(path: str) -> int:

    textureID = glGenTextures(1)
    
    try:
        img = LOAD_IMAGE(path)

        nrComponents = len(img.getbands())

        format = GL_RED if nrComponents == 1 else \
                 GL_RGB if nrComponents == 3 else \
                 GL_RGBA 

        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexImage2D(GL_TEXTURE_2D, 0, format, img.width, img.height, 0, format, GL_UNSIGNED_BYTE, img.tobytes())
        glGenerateMipmap(GL_TEXTURE_2D)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        img.close()

    except:

        print("Texture failed to load at path: " + path)

    return textureID