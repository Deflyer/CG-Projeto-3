from OpenGL.GL import *
from glfw.GLFW import *

import config_screen as cs

from shader import Shader
from keyboard import *
from utils import *
from transformations_info import *
from drawing import *
from lights import *
from vertexes import *

if __name__ == '__main__':
    
    window = cs.init_window()
    cs.set_callbacks(window, framebuffer_size_callback, mouse_callback, scroll_callback)

    # Tell GLFW to capture our mouse.
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED)

    # Configure global opengl state.
    glEnable(GL_DEPTH_TEST)

    # Build and compile our shader program.
    lightingShader = Shader("./shaders/scene.vs", "./shaders/scene.fs")

    combined_vertexes, textures, vet, vet_idx = get_vertexes_textures()

    plant_positions = get_positions_plants()

    # Configuring the cube's VAO (and VBO).
    cubeVAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    lightCubeVAO = cs.send_data_to_gpu(cubeVAO, VBO, combined_vertexes)

    # Render loop.
    while (not glfwWindowShouldClose(window)):

        # Per-frame time logic.
        currentFrame = glfwGetTime()
        deltaTime = currentFrame - lastFrame
        lastFrame = currentFrame

        # Getting input.
        camera = processInput(window, deltaTime)

        # Rendering.
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Invisible box around house.
        x_min = -4.8
        x_max = 4.7
        z_min = -23.7
        z_max = -5
        y_max = 10

        # Be sure to activate shader when setting uniforms/drawing objects.
        lightingShader.use()
        lightingShader.setVec3("viewPos", camera.Position)
        lightingShader.setFloat("material.shininess", 2.0)

        # View/projection transformations.
        projection = glm.perspective(glm.radians(camera.Zoom), cs.WIDTH / cs.HEIGHT, 0.1, 1000.0)
        view = camera.GetViewMatrix()
        lightingShader.setMat4("projection", projection)
        lightingShader.setMat4("view", view)

        # World transformation.
        model = glm.mat4(1.0)
        lightingShader.setMat4("model", model)

        # Rotating bird and sky.
        kb.bird_angle = (kb.bird_angle + kb.bird_speed) % 360
        kb.sky_rotation_angle = (kb.sky_rotation_angle + 0.1) % 360

        position = kb.get_camera_pos()
        pointLightPositions = get_lights_positions()

        # Drawing all the objects.
        draw_internal_objects(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions)
        draw_external_objects(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions, plant_positions)
        draw_house(lightingShader, cubeVAO, textures, vet, vet_idx, pointLightPositions, x_min, x_max, z_min, z_max, y_max, position)

        # Swap buffers and poll IO events (keys pressed/released, mouse moved, etc).
        glfwSwapBuffers(window)
        glfwPollEvents()

    # De-allocate all resources once they've outlived their purpose.
    glDeleteVertexArrays(1, (cubeVAO,))
    glDeleteVertexArrays(1, (lightCubeVAO,))
    glDeleteBuffers(1, (VBO,))

    # Clearing all previously allocated GLFW resources.
    glfwTerminate()