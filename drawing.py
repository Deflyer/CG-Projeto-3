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

def draw_internal_objects(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions):
    '''
    Draws only the objects inside the house. Also forces outside lights to not influence.
    '''

    # Deactivating effects from outside lights in inside objects.
    lightingShader.setFloat("pointLights[0].space", 1)
    lightingShader.setFloat("pointLights[1].space", 1)
    lightingShader.setFloat("pointLights[2].space", 0)
    lightingShader.setFloat("dirLight.space", 0)
    
    draw_object(cubeVAO, textures, vet, vet_idx['rose'], lightingShader, pointLightPositions)    
    draw_object(cubeVAO, textures, vet, vet_idx['drawer'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['bed'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['vase'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['magic_ball'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['magic_ball_stand'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['lamp'], lightingShader, pointLightPositions)

def draw_external_objects(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions, plant_positions):
    '''
    Draws only the objects outside the house. Also forces inside lights to not influence.
    '''

    # Deactivating effects from inside lights in outside objects.
    lightingShader.setFloat("pointLights[0].space", 0)
    lightingShader.setFloat("pointLights[1].space", 0)
    lightingShader.setFloat("pointLights[2].space", 1)
    lightingShader.setFloat("dirLight.space", 1)
    
    # drawing  external objects
    draw_object(cubeVAO, textures, vet, vet_idx['bird'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['bathroom'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['ground'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['sky'], lightingShader, pointLightPositions)
    draw_plants(cubeVAO, textures, vet, vet_idx['plant1'], lightingShader, plant_positions, pointLightPositions)
    draw_shrek(cubeVAO, textures, vet, vet_idx['shrek'], lightingShader, pointLightPositions)
    draw_object(cubeVAO, textures, vet, vet_idx['lantern'], lightingShader, pointLightPositions)

def draw_house(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions, x_min, x_max, z_min, z_max, y_max, position):
    '''
    Draws house handling lights depending on the camera position.
    '''

    # If the camera is inside house, inverts normals.
    if(x_min <= position[0] <= x_max) and (z_min <= position[2] <= z_max) and (position[1] <= y_max):
        lightingShader.setFloat("pointLights[0].space", 1)
        lightingShader.setFloat("pointLights[1].space", 1)
        lightingShader.setFloat("pointLights[2].space", 0)
        lightingShader.setFloat("dirLight.space", 0)
        lightingShader.setFloat("pointLights[0].normal_correction", -1)
        lightingShader.setFloat("pointLights[1].normal_correction", -1)
    else:        
        lightingShader.setFloat("pointLights[2].normal_correction", -1)
    draw_object(cubeVAO, textures, vet, vet_idx['house'], lightingShader, pointLightPositions)