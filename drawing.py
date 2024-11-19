import glm
from OpenGL.GL import *
from glfw.GLFW import *

def draw_object(cubeVAO, position, textures, vertexes, vet_idx, lightingShader):

    glBindVertexArray(cubeVAO)

    # calculate the model matrix for each object and pass it to shader before drawing
    model = glm.mat4(1.0)
    model = glm.translate(model, position)
    angle = 20.0
    model = glm.scale(model, glm.vec3(0.2))
    model = glm.rotate(model, glm.radians(angle), glm.vec3(1.0, 0.3, 0.5))
    lightingShader.setMat4("model", model)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[vet_idx])

    glDrawArrays(GL_TRIANGLES, vertexes[vet_idx]['inicio'], vertexes[vet_idx]['tam'])