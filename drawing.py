import glm
from OpenGL.GL import *

from transformations_info import *

def draw_object(cubeVAO, textures, vertexes, idx, lightingShader):

    glBindVertexArray(cubeVAO)

    pos = get_position(idx)
    scale = get_scale(idx)
    rot_angle = get_rotation(idx)

    # calculate the model matrix for each object and pass it to shader before drawing
    model = glm.mat4(1.0)
    model = glm.translate(model, pos)
    model = glm.scale(model, glm.vec3(scale))
    model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
    lightingShader.setMat4("model", model)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx])

    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], vertexes[idx]['tam'])

def draw_shrek(cubeVAO, textures, vertexes, idx, lightingShader):

    glBindVertexArray(cubeVAO)

    pos = get_position(idx)
    scale = get_scale(idx)
    rot_angle = get_rotation(idx)
    #print(idx, scale)

    # calculate the model matrix for each object and pass it to shader before drawing
    model = glm.mat4(1.0)
    model = glm.translate(model, pos)
    model = glm.scale(model, glm.vec3(scale))
    model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
    lightingShader.setMat4("model", model)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx])

    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], 5112)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx+1])

    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'] + 5112, 1086)