from OpenGL.GL import *
from glfw.GLFW import *

from glfw import _GLFWwindow as GLFWwindow
from PIL import Image

from shader_m import Shader
from keyboard import *
from config_screen import *
from vertexes import *

import platform, ctypes, os

# the relative path where the textures are located
IMAGE_RESOURCE_PATH = "./texturas/"

# function that loads and automatically flips an image vertically
LOAD_IMAGE = lambda name: Image.open(os.path.join(IMAGE_RESOURCE_PATH, name)).transpose(Image.FLIP_TOP_BOTTOM)

# settings
SCR_WIDTH = 1920
SCR_HEIGHT = 1080

# lighting
lightPos = glm.vec3(1.2, 1.0, 2.0)

def main() -> int:
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
    lightingShader = Shader("6.multiple_lights.vs", "6.multiple_lights.fs")
    lightCubeShader = Shader("6.light_cube.vs", "6.light_cube.fs")
    # set up vertex data (and buffer(s)) and configure vertex attributes
    # ------------------------------------------------------------------
    
    vet = []
    vertices1 = load_obj_to_glm_array('./rose.obj')
    vet.append({'inicio': 0, 'fim': int(len(vertices1)/8)})
    
    vertices2 = load_obj_to_glm_array('./drawer.obj')
    ini = vet[0]['fim']
    vet.append({'inicio': ini, 'fim': ini + int(len(vertices1)/8)})
    
    combined_vertices = glm.array(glm.float32, *vertices1[:], *vertices2[:])

    cubePositions = get_cubes_positions()
    pointLightPositions = get_lights_positions()

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

    # load textures (we now use a utility function to keep the code more organized)
    # -----------------------------------------------------------------------------
    textures = []
    
    texture0 = loadTexture("./rose_texture.jpg")
    textures.append(texture0)

    texture1 = loadTexture("./drawer_texture.png")
    textures.append(texture1)

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

        # be sure to activate shader when setting uniforms/drawing objects
        lightingShader.use()
        lightingShader.setVec3("viewPos", camera.Position)
        lightingShader.setFloat("material.shininess", 32.0)

        
        #   Here we set all the uniforms for the 5/6 types of lights we have. We have to set them manually and index 
        #   the proper PointLight struct in the array to set each uniform variable. This can be done more code-friendly
        #   by defining light types as classes and set their values in there, or by using a more efficient uniform approach
        #   by using 'Uniform buffer objects', but that is something we'll discuss in the 'Advanced GLSL' tutorial.
           
        # directional light
        lightingShader.setVec3("dirLight.direction", -0.2, -1.0, -0.3)
        lightingShader.setVec3("dirLight.ambient", 0.05, 0.05, 0.05)
        lightingShader.setVec3("dirLight.diffuse", 0.4, 0.4, 0.4)
        lightingShader.setVec3("dirLight.specular", 0.5, 0.5, 0.5)
        # point light 1
        lightingShader.setVec3("pointLights[0].position", pointLightPositions[0])
        lightingShader.setVec3("pointLights[0].ambient", 0.0, 0.0, 0.05)  # Azul escuro para o ambiente
        lightingShader.setVec3("pointLights[0].diffuse", 0.0, 0.0, 0.8)   # Azul médio para a luz difusa
        lightingShader.setVec3("pointLights[0].specular", 0.0, 0.0, 1.0)  # Azul brilhante para o specular
        lightingShader.setFloat("pointLights[0].constant", 1.0)
        lightingShader.setFloat("pointLights[0].linear", 0.09)
        lightingShader.setFloat("pointLights[0].quadratic", 0.032)
        # point light 2
        lightingShader.setVec3("pointLights[1].position", pointLightPositions[1])
        lightingShader.setVec3("pointLights[1].ambient", 0.05, 0.05, 0.05)
        lightingShader.setVec3("pointLights[1].diffuse", 0.8, 0.8, 0.8)
        lightingShader.setVec3("pointLights[1].specular", 1.0, 1.0, 1.0)
        lightingShader.setFloat("pointLights[1].constant", 1.0)
        lightingShader.setFloat("pointLights[1].linear", 0.09)
        lightingShader.setFloat("pointLights[1].quadratic", 0.032)
        # point light 3
        lightingShader.setVec3("pointLights[2].position", pointLightPositions[2])
        lightingShader.setVec3("pointLights[2].ambient", 0.05, 0.05, 0.05)
        lightingShader.setVec3("pointLights[2].diffuse", 0.8, 0.8, 0.8)
        lightingShader.setVec3("pointLights[2].specular", 1.0, 1.0, 1.0)
        lightingShader.setFloat("pointLights[2].constant", 1.0)
        lightingShader.setFloat("pointLights[2].linear", 0.09)
        lightingShader.setFloat("pointLights[2].quadratic", 0.032)
        # point light 4
        lightingShader.setVec3("pointLights[3].position", pointLightPositions[3])
        lightingShader.setVec3("pointLights[3].ambient", 0.05, 0.05, 0.05)
        lightingShader.setVec3("pointLights[3].diffuse", 0.8, 0.8, 0.8)
        lightingShader.setVec3("pointLights[3].specular", 1.0, 1.0, 1.0)
        lightingShader.setFloat("pointLights[3].constant", 1.0)
        lightingShader.setFloat("pointLights[3].linear", 0.09)
        lightingShader.setFloat("pointLights[3].quadratic", 0.032)
        # spotLight
        lightingShader.setVec3("spotLight.position", camera.Position)
        lightingShader.setVec3("spotLight.direction", camera.Front)
        lightingShader.setVec3("spotLight.ambient", 0.0, 0.0, 0.0)
        lightingShader.setVec3("spotLight.diffuse", 0, 0, 0)
        lightingShader.setVec3("spotLight.specular", 0, 0, 0)
        lightingShader.setFloat("spotLight.constant", 0)
        lightingShader.setFloat("spotLight.linear", 0.09)
        lightingShader.setFloat("spotLight.quadratic", 0.032)
        lightingShader.setFloat("spotLight.cutOff", glm.cos(glm.radians(12.5)))
        lightingShader.setFloat("spotLight.outerCutOff", glm.cos(glm.radians(15.0)))     

        # view/projection transformations
        projection = glm.perspective(glm.radians(camera.Zoom), SCR_WIDTH / SCR_HEIGHT, 0.1, 100.0)
        view = camera.GetViewMatrix()
        lightingShader.setMat4("projection", projection)
        lightingShader.setMat4("view", view)

        # world transformation
        model = glm.mat4(1.0)
        lightingShader.setMat4("model", model)

        # bind diffuse map
        
        # bind specular map
        # glActiveTexture(GL_TEXTURE1)
        # glBindTexture(GL_TEXTURE_2D, specularMap)

        # render containers
        glBindVertexArray(cubeVAO)
        for i in range(2):

            # calculate the model matrix for each object and pass it to shader before drawing
            model = glm.mat4(1.0)
            model = glm.translate(model, cubePositions[0])
            angle = 20.0 * i
            model = glm.scale(model, glm.vec3(0.2))
            model = glm.rotate(model, glm.radians(angle), glm.vec3(1.0, 0.3, 0.5))
            lightingShader.setMat4("model", model)

            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, textures[i])

            glDrawArrays(GL_TRIANGLES, vet[i]['inicio'], vet[i]['fim'])
        

        # also draw the lamp object(s)
        lightCubeShader.use()
        lightCubeShader.setMat4("projection", projection)
        lightCubeShader.setMat4("view", view)
        
        # we now draw as many light bulbs as we have point lights.
        glBindVertexArray(lightCubeVAO)
        for i in range(1):

            model = glm.mat4(1.0)
            model = glm.translate(model, pointLightPositions[i])
            model = glm.scale(model, glm.vec3(0.007)) # Make it a smaller cube

            lightCubeShader.setMat4("model", model)

            glDrawArrays(GL_TRIANGLES, vet[i]['inicio'], vet[i]['fim'])

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
    return 0

# utility function for loading a 2D texture from file
# ---------------------------------------------------
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


main()