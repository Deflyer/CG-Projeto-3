import glm
from OpenGL.GL import *
import keyboard as kb
from lights import *

from transformations_info import *

def draw_object(cubeVAO, textures, vertexes, idx, lightingShader, pointLightPositions):

    glBindVertexArray(cubeVAO)

    aplicar_luz_param(lightingShader, pointLightPositions, idx)

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

def draw_shrek(cubeVAO, textures, vertexes, idx, lightingShader, pointLightPositions):

    glBindVertexArray(cubeVAO)

    aplicar_luz_param(lightingShader, pointLightPositions, idx)

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

    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], 5112)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx+1])

    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'] + 5112, 1086)

def draw_plants(cubeVAO, textures, vertexes, lightingShader, plants_positions, pointLightPositions):

    idx = 9
    
    aplicar_luz_param(lightingShader, pointLightPositions, idx)

    for plant in plants_positions:
        glBindVertexArray(cubeVAO)
        for (t_x, t_y, t_z, angle, s_x, s_y, s_z) in plant:
            pos = glm.vec3(t_x, t_y, t_z)
            scale = glm.vec3(s_x, s_y, s_z)
            rot_angle = angle

            model = glm.mat4(1.0)
            model = glm.translate(model, pos)
            model = glm.scale(model, scale)
            model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
            lightingShader.setMat4("model", model)

            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, textures[idx])

            glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], vertexes[idx]['tam'])
        idx += 1