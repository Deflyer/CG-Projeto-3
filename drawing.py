# Effectively draws our objects on the screen.

import glm
import keyboard as kb
from OpenGL.GL import *
from lights import *
from transformations_info import *

def draw_object(cubeVAO, textures, vertexes, idx, lightingShader, pointLightPositions):
    '''
    Draws all the one-textured objects.
    '''

    glBindVertexArray(cubeVAO)

    # Applying light parameters.
    apply_light_param(lightingShader, pointLightPositions, idx)

    # Getting transformations parameters.
    pos = get_position(idx)
    scale = get_scale(idx)
    rot_angle = get_rotation(idx)

    # Calculates the model matrix for each object and pass it to shader before drawing.
    model = glm.mat4(1.0)
    model = glm.translate(model, pos)
    model = glm.scale(model, glm.vec3(scale))
    model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
    lightingShader.setMat4("model", model)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx])
    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], vertexes[idx]['tam'])

def draw_shrek(cubeVAO, textures, vertexes, idx, lightingShader, pointLightPositions):
    '''
    Draws Shrek. There is a single function for it because it has 2 texture and is placed once in the world.
    '''

    glBindVertexArray(cubeVAO)

    # Applying light parameters.
    apply_light_param(lightingShader, pointLightPositions, idx)

    # Getting transformations parameters.
    pos = get_position(idx)
    scale = get_scale(idx)
    rot_angle = get_rotation(idx)

    # Calculates the model matrix for each object and pass it to shader before drawing.
    model = glm.mat4(1.0)
    model = glm.translate(model, pos)
    model = glm.scale(model, glm.vec3(scale))
    model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
    lightingShader.setMat4("model", model)

    # Drawing first texture.
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx])
    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], 5112)

    # Drawing second texture.
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textures[idx+1])
    glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'] + 5112, 1086)

def draw_plants(cubeVAO, textures, vertexes, idx, lightingShader, plants_positions, pointLightPositions):
    '''
    Draws both types of plants. There is a single function for it because it has 2 texture and is placed more than once in the world.
    '''
    
    # Applying light parameters.
    apply_light_param(lightingShader, pointLightPositions, idx)

    # Draw each type of plant separately.
    for plant in plants_positions:

        glBindVertexArray(cubeVAO)

        for (t_x, t_y, t_z, angle, s_x, s_y, s_z) in plant:

            # Getting transformations parameters.
            pos = glm.vec3(t_x, t_y, t_z)
            scale = glm.vec3(s_x, s_y, s_z)
            rot_angle = angle

            # Calculates the model matrix for each object and pass it to shader before drawing.
            model = glm.mat4(1.0)
            model = glm.translate(model, pos)
            model = glm.scale(model, scale)
            model = glm.rotate(model, glm.radians(rot_angle), glm.vec3(0, 1, 0))
            lightingShader.setMat4("model", model)

            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, textures[idx])
            glDrawArrays(GL_TRIANGLES, vertexes[idx]['inicio'], vertexes[idx]['tam'])

        # Preparing to draw the other type of plant.
        idx += 1