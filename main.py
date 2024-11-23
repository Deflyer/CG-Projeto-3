from OpenGL.GL import *
from glfw.GLFW import *

from glfw import _GLFWwindow as GLFWwindow

from shader import Shader
from keyboard import *
from config_screen import *
from utils import *
from transformations_info import *
from drawing import *

import platform, ctypes, os

# settings
SCR_WIDTH = 1920
SCR_HEIGHT = 1080

# lighting
lightPos = glm.vec3(1.2, 1.0, 2.0)

if __name__ == '__main__':
    
    global deltaTime, lastFrame

    window = init_window()

    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback)
    glfwSetCursorPosCallback(window, mouse_callback)
    glfwSetScrollCallback(window, scroll_callback)

    # tell GLFW to capture our mouse
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED)

    # configure global opengl state
    # -----------------------------
    glEnable(GL_DEPTH_TEST)

    # build and compile our shader zprogram
    # ------------------------------------
    lightingShader = Shader("./shaders/6.multiple_lights.vs", "./shaders/6.multiple_lights.fs")
    lightCubeShader = Shader("./shaders/6.light_cube.vs", "./shaders/6.light_cube.fs")
    # set up vertex data (and buffer(s)) and configure vertex attributes
    # ------------------------------------------------------------------

    vet = []
    textures = []
    vet_idx = {}
    
    vertexes_aux_1 = load_obj_to_glm_array('./objects/rose/rose.obj')
    vet.append({'inicio': 0, 'tam': int(len(vertexes_aux_1)/8)})
    texture_aux = loadTexture("./objects/rose/rose_texture.jpg")
    textures.append(texture_aux)
    vet_idx['rose'] = 0
    
    vertexes_aux_2 = load_obj_to_glm_array('./objects/bird/bird.obj')
    ini = vet[0]['inicio'] + vet[0]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_2)/8)})
    texture_aux = loadTexture("./objects/bird/bird_texture.jpg")
    textures.append(texture_aux)
    vet_idx['bird'] = 1

    vertexes_aux_3 = load_obj_to_glm_array('./objects/drawer/drawer.obj')
    ini = vet[1]['inicio'] + vet[1]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_3)/8)})
    texture_aux = loadTexture("./objects/drawer/drawer_texture.png")
    textures.append(texture_aux)
    vet_idx['drawer'] = 2

    vertexes_aux_4 = load_obj_to_glm_array('./objects/bed/bed.obj')
    ini = vet[2]['inicio'] + vet[2]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_4)/8)})
    texture_aux = loadTexture("./objects/bed/bed_texture.png")
    textures.append(texture_aux)
    vet_idx['bed'] = 3

    vertexes_aux_5 = load_obj_to_glm_array('./objects/bathroom/bathroom.obj')
    ini = vet[3]['inicio'] + vet[3]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_5)/8)})
    texture_aux = loadTexture("./objects/bathroom/bathroom_texture.png")
    textures.append(texture_aux)
    vet_idx['bathroom'] = 4

    vertexes_aux_6 = load_obj_to_glm_array('./objects/ground/ground.obj')
    ini = vet[4]['inicio'] + vet[4]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_6)/8)})
    texture_aux = loadTexture("./objects/ground/ground_texture.jpg")
    textures.append(texture_aux)
    vet_idx['ground'] = 5

    vertexes_aux_7 = load_obj_to_glm_array('./objects/house/house.obj')
    ini = vet[5]['inicio'] + vet[5]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_7)/8)})
    texture_aux = loadTexture("./objects/house/house_texture.jpg")
    textures.append(texture_aux)
    vet_idx['house'] = 6

    vertexes_aux_8 = load_obj_to_glm_array('./objects/sky/sky.obj')
    ini = vet[6]['inicio'] + vet[6]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_8)/8)})
    texture_aux = loadTexture("./objects/sky/sky_texture.jpg")
    textures.append(texture_aux)
    vet_idx['sky'] = 7

    vertexes_aux_9 = load_obj_to_glm_array('./objects/vase/vase.obj')
    ini = vet[7]['inicio'] + vet[7]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_9)/8)})
    texture_aux = loadTexture("./objects/vase/vase_texture.png")
    textures.append(texture_aux)
    vet_idx['vase'] = 8

    vertexes_aux_10 = load_obj_to_glm_array('./objects/plant/plant1.obj')
    ini = vet[8]['inicio'] + vet[8]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_10)/8)})
    texture_aux = loadTexture("./objects/plant/plant1_texture.png")
    textures.append(texture_aux)
    vet_idx['plant1'] = 9

    vertexes_aux_11 = load_obj_to_glm_array('./objects/plant/plant2.obj')
    ini = vet[9]['inicio'] + vet[9]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_11)/8)})
    texture_aux = loadTexture("./objects/plant/plant2_texture.png")
    textures.append(texture_aux)
    vet_idx['plant2'] = 10

    vertexes_aux_12 = load_obj_to_glm_array('./objects/lamp/lamp.obj')
    ini = vet[10]['inicio'] + vet[10]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_12)/8)})
    texture_aux = loadTexture("./objects/lamp/lamp_texture.png")
    textures.append(texture_aux)
    vet_idx['lamp'] = 11

    vertexes_aux_13 = load_obj_to_glm_array('./objects/lantern/lantern.obj')
    ini = vet[11]['inicio'] + vet[11]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_13)/8)})
    texture_aux = loadTexture("./objects/lantern/lantern_texture.jpg")
    textures.append(texture_aux)
    vet_idx['lantern'] = 12

    vertexes_aux_14 = load_obj_to_glm_array('./objects/magic_ball/magic_ball.obj')
    ini = vet[12]['inicio'] + vet[12]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_14)/8)})
    texture_aux = loadTexture("./objects/magic_ball/magic_ball.jpg")
    textures.append(texture_aux)
    vet_idx['magic_ball'] = 13

    vertexes_aux_15 = load_obj_to_glm_array('./objects/magic_ball/magic_ball_stand.obj')
    ini = vet[13]['inicio'] + vet[13]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_15)/8)})
    texture_aux = loadTexture("./objects/magic_ball/stand.jpg")
    textures.append(texture_aux)
    vet_idx['magic_ball_stand'] = 14

    vertexes_aux_16 = load_obj_to_glm_array('./objects/shrek/shrek.obj')
    ini = vet[14]['inicio'] + vet[14]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_16)/8)})
    texture_aux = loadTexture("./objects/shrek/shrek.jpg")
    textures.append(texture_aux)
    texture_aux = loadTexture("./objects/shrek/leather.jpg")
    textures.append(texture_aux)
    vet_idx['shrek'] = 15

    combined_vertices = glm.array(glm.float32, *vertexes_aux_1[:], *vertexes_aux_2[:], *vertexes_aux_3[:], *vertexes_aux_4[:], 
                                  *vertexes_aux_5[:], *vertexes_aux_6[:], *vertexes_aux_7[:], *vertexes_aux_8[:], *vertexes_aux_9[:],
                                  *vertexes_aux_10[:], *vertexes_aux_11[:], *vertexes_aux_12[:], *vertexes_aux_13[:], *vertexes_aux_14[:],
                                  *vertexes_aux_15[:], *vertexes_aux_16[:])

    plant_positions = get_positions_plants()
    # first, configure the cube's VAO (and VBO)
    cubeVAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, combined_vertices.nbytes, combined_vertices.ptr, GL_STATIC_DRAW)

    glBindVertexArray(cubeVAO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(3 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(6 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(2)

    # second, configure the light's VAO (VBO stays the same the vertices are the same for the light object which is also a 3D cube)
    lightCubeVAO = glGenVertexArrays(1)
    glBindVertexArray(lightCubeVAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # note that we update the lamp's position attribute's stride to reflect the updated buffer data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)


    # specularMap = loadTexture("container2_specular.png")

    # shader configuration
    # --------------------
    lightingShader.use()
    lightingShader.setInt("material.diffuse", 0)
    lightingShader.setInt("material.specular", 1)

    # render loop
    # -----------
    while (not glfwWindowShouldClose(window)):

        # per-frame time logic
        # --------------------
        currentFrame = glfwGetTime()
        deltaTime = currentFrame - lastFrame
        lastFrame = currentFrame

        # input
        # -----
        camera = processInput(window, deltaTime)

        # render
        # ------
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        pointLightPositions = get_lights_positions()

        x_min = -4.8
        x_max = 4.7
        z_min = -23.7
        z_max = -5
        y_max = 10

        # be sure to activate shader when setting uniforms/drawing objects
        lightingShader.use()
        lightingShader.setVec3("viewPos", camera.Position)
        lightingShader.setFloat("material.shininess", 2.0)
           
        # directional light
        lightingShader.setVec3("dirLight.direction", -0.2, -1.0, -0.3)
        lightingShader.setVec3("dirLight.ambient", 0.5, 0.5, 0.5)
        lightingShader.setVec3("dirLight.diffuse", 0.5, 0.5, 0.5)
        lightingShader.setVec3("dirLight.specular", 0.5, 0.5, 0.5)
        lightingShader.setFloat("dirLight.space", 1)
        lightingShader.setFloat("dirLight.normal_correction", 1)
        # point light 1
        lightingShader.setVec3("pointLights[0].position", pointLightPositions[0])
        lightingShader.setVec3("pointLights[0].ambient", 0.8 * kb.ambient * kb.is_lamp_on, (0.7)* kb.ambient * kb.is_lamp_on, (0.3)* kb.ambient * kb.is_lamp_on)
        lightingShader.setVec3("pointLights[0].diffuse", 1.0 *  kb.is_lamp_on * kb.diffuse, 0.9 *  kb.is_lamp_on * kb.diffuse, 0.5 *  kb.is_lamp_on * kb.diffuse)
        lightingShader.setVec3("pointLights[0].specular", 0.0 *  kb.is_lamp_on * kb.specular, 0.0 *  kb.is_lamp_on * kb.specular, 0.0 *  kb.is_lamp_on * kb.specular)
        lightingShader.setFloat("pointLights[0].space", 1)
        lightingShader.setFloat("pointLights[0].normal_correction", 1)
        lightingShader.setFloat("pointLights[0].constant", 1.0)
        lightingShader.setFloat("pointLights[0].linear", 0.0009)
        lightingShader.setFloat("pointLights[0].quadratic", 0.00032)
        # point light 2
        lightingShader.setVec3("pointLights[1].position", pointLightPositions[1])
        lightingShader.setVec3("pointLights[1].ambient", 0.3 * kb.ambient * kb.is_ball_on, 0.3 * kb.ambient * kb.is_ball_on, 0.9 * kb.ambient * kb.is_ball_on)
        lightingShader.setVec3("pointLights[1].diffuse", 0.5 * kb.diffuse * kb.is_ball_on, 0.7 * kb.diffuse * kb.is_ball_on, 1.0 * kb.diffuse * kb.is_ball_on)
        lightingShader.setVec3("pointLights[1].specular", 0.6 * kb.specular * kb.is_ball_on, 0.7 * kb.specular * kb.is_ball_on, 1.0 * kb.specular * kb.is_ball_on)
        lightingShader.setFloat("pointLights[1].space", 1)
        lightingShader.setFloat("pointLights[1].normal_correction", 1)
        lightingShader.setFloat("pointLights[1].constant", 1.0)
        lightingShader.setFloat("pointLights[1].linear", 0.09)
        lightingShader.setFloat("pointLights[1].quadratic", 0.032)
        # point light 3
        lightingShader.setVec3("pointLights[2].position", pointLightPositions[2])
        lightingShader.setVec3("pointLights[2].ambient", 0.9 * kb.ambient * kb.is_fire_on, 0.3 * kb.ambient * kb.is_fire_on, 0.3 * kb.ambient * kb.is_fire_on)
        lightingShader.setVec3("pointLights[2].diffuse", 1.0 * kb.diffuse * kb.is_fire_on, 0.2 * kb.diffuse * kb.is_fire_on, 0.2 * kb.diffuse * kb.is_fire_on)
        lightingShader.setVec3("pointLights[2].specular", 1.0 * kb.specular * kb.is_fire_on, 0.2 * kb.specular * kb.is_fire_on, 0.2 * kb.specular * kb.is_fire_on)
        lightingShader.setFloat("pointLights[2].space", 0)
        lightingShader.setFloat("pointLights[2].normal_correction", 1)
        lightingShader.setFloat("pointLights[2].constant", 1.0)
        lightingShader.setFloat("pointLights[2].linear", 0.02)
        lightingShader.setFloat("pointLights[2].quadratic", 0.0032)

        # view/projection transformations
        projection = glm.perspective(glm.radians(camera.Zoom), SCR_WIDTH / SCR_HEIGHT, 0.1, 1000.0)
        view = camera.GetViewMatrix()
        lightingShader.setMat4("projection", projection)
        lightingShader.setMat4("view", view)

        # world transformation
        model = glm.mat4(1.0)
        lightingShader.setMat4("model", model)

        # render containers

        kb.bird_angle = (kb.bird_angle + kb.bird_speed) % 360
        kb.sky_rotation_angle = (kb.sky_rotation_angle + 0.1) % 360

        # drawing internal objects
        lightingShader.setFloat("pointLights[0].space", 1)
        lightingShader.setFloat("pointLights[1].space", 1)
        lightingShader.setFloat("pointLights[2].space", 0)
        draw_object(cubeVAO, textures, vet, vet_idx['rose'], lightCubeShader)    
        draw_object(cubeVAO, textures, vet, vet_idx['drawer'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['bed'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['vase'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['magic_ball'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['magic_ball_stand'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['lamp'], lightCubeShader)
        position = kb.get_camera_pos()
        lightingShader.setFloat("pointLights[0].space", 0)
        lightingShader.setFloat("pointLights[1].space", 0)
        lightingShader.setFloat("pointLights[2].space", 1)
        # drawing  external objects
        draw_object(cubeVAO, textures, vet, vet_idx['bird'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['bathroom'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['ground'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['sky'], lightCubeShader)
        draw_plants(cubeVAO, textures, vet, lightCubeShader,plant_positions)
        draw_shrek(cubeVAO, textures, vet, vet_idx['shrek'], lightCubeShader)
        draw_object(cubeVAO, textures, vet, vet_idx['lantern'], lightCubeShader)
        if(x_min <= position[0] <= x_max) and (z_min <= position[2] <= z_max) and (position[1] <= y_max):
            lightingShader.setFloat("pointLights[0].space", 1)
            lightingShader.setFloat("pointLights[1].space", 1)
            lightingShader.setFloat("pointLights[2].space", 0)
            lightingShader.setFloat("pointLights[0].normal_correction", -1)
            lightingShader.setFloat("pointLights[1].normal_correction", -1)
        else:        
            lightingShader.setFloat("pointLights[2].normal_correction", -1)
        draw_object(cubeVAO, textures, vet, vet_idx['house'], lightCubeShader)

        # also draw the lamp object(s)
        lightCubeShader.use()
        lightCubeShader.setMat4("projection", projection)
        lightCubeShader.setMat4("view", view)
        
        # we now draw as many light bulbs as we have point lights.
        glBindVertexArray(lightCubeVAO)
        for i in range(0):

            model = glm.mat4(1.0)
            model = glm.translate(model, pointLightPositions[i])
            model = glm.scale(model, glm.vec3(0.07)) # Make it a smaller cube

            lightCubeShader.setMat4("model", model)
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, textures[i])

            glDrawArrays(GL_TRIANGLES, vet[i]['inicio'], vet[i]['tam'])

        # glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        # -------------------------------------------------------------------------------
        glfwSwapBuffers(window)
        glfwPollEvents()

    # optional: de-allocate all resources once they've outlived their purpose:
    # ------------------------------------------------------------------------
    glDeleteVertexArrays(1, (cubeVAO,))
    glDeleteVertexArrays(1, (lightCubeVAO,))
    glDeleteBuffers(1, (VBO,))

    # glfw: terminate, clearing all previously allocated GLFW resources.
    # ------------------------------------------------------------------
    glfwTerminate()