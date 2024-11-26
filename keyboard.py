# File that handles all keyboard functionalities.

import glm
from glfw import _GLFWwindow as GLFWwindow
from glfw.GLFW import *
from OpenGL.GL import *
import camera as cam
import config_screen as cs

camera = cam.Camera(glm.vec3(0.0, 0.0, 3.0))
lastX = cs.WIDTH / 2.0
lastY = cs.HEIGHT / 2.0
firstMouse = True

lastFrame = 0.0

# Transformations auxiliar variables.
rose_scale_y = 0.05
sky_rotation_angle = 0.0
bird_speed = 0.00
bird_radius = 80.0
bird_angle = 0.0
shrek_step = 0.0
shrek_side_step = 0.0

# Turn on/off lights auxiliar variables.
is_lamp_on = 1
is_ball_on = 1
is_fire_on = 1
is_sun_on = 1

# Increase/decrease light components auxiliar variables.
ambient = 1
diffuse = 1
specular = 1

def mouse_callback(window: GLFWwindow, xpos: float, ypos: float) -> None:
    '''
    Whenever the mouse moves, this callback is called.
    '''
    
    global lastX, lastY, firstMouse

    if (firstMouse):

        lastX = xpos
        lastY = ypos
        firstMouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos # Reversed since y-coordinates go from bottom to top.

    lastX = xpos
    lastY = ypos

    camera.ProcessMouseMovement(xoffset, yoffset)

def scroll_callback(window: GLFWwindow, xoffset: float, yoffset: float) -> None:
    '''
    Whenever the mouse scroll wheel scrolls, this callback is called.
    '''

    camera.ProcessMouseScroll(yoffset)

def processInput(window: GLFWwindow, deltaTime) -> None:
    '''
    Process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly.
    '''

    global rose_scale_y
    global bird_speed
    global shrek_side_step
    global shrek_step
    global is_lamp_on
    global is_ball_on
    global is_fire_on
    global is_sun_on
    global ambient
    global diffuse
    global specular

    # House and bathroom (Shrek cant enter these areas).
    exclusion_zones = [
        (-8, -30, 6, 1),
        (5, -9, 25, -2),             
    ]

    # Closes window.
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS):
        glfwSetWindowShouldClose(window, True)

    # Movees camera.
    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS):
        camera.ProcessKeyboard(cam.Camera_Movement.FORWARD, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS):
        camera.ProcessKeyboard(cam.Camera_Movement.BACKWARD, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS):
        camera.ProcessKeyboard(cam.Camera_Movement.LEFT, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS):
        camera.ProcessKeyboard(cam.Camera_Movement.RIGHT, deltaTime)

    # Scales rose.
    if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS):
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)
    if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS):
        aux = rose_scale_y - 0.01
        rose_scale_y = max(aux,0.05)

    # Moves Shrek.
    if (glfwGetKey(window, GLFW_KEY_I) == GLFW_PRESS):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 1.9 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step - 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step -= 0.5
    if (glfwGetKey(window, GLFW_KEY_J) == GLFW_PRESS):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step -0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step - 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step -= 0.5 
    if (glfwGetKey(window, GLFW_KEY_K) == GLFW_PRESS):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 2.1 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step + 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step += 0.5
    if (glfwGetKey(window, GLFW_KEY_L) == GLFW_PRESS):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step +0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step + 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step += 0.5

    # Turn on/off lights.
    if (glfwGetKey(window, GLFW_KEY_Z) == GLFW_PRESS):
        is_lamp_on = not is_lamp_on
    if (glfwGetKey(window, GLFW_KEY_X) == GLFW_PRESS):
        is_ball_on = not is_ball_on 
    if (glfwGetKey(window, GLFW_KEY_C) == GLFW_PRESS):
        is_fire_on = not is_fire_on
    if (glfwGetKey(window, GLFW_KEY_V) == GLFW_PRESS):
        is_sun_on = not is_sun_on

    # Increases/decreses light components intensity.
    if (glfwGetKey(window, GLFW_KEY_1) == GLFW_PRESS):
        ambient -= 0.1
        if(ambient < 0):
            ambient = 0
    if (glfwGetKey(window, GLFW_KEY_2) == GLFW_PRESS):
            ambient += 0.1 
    if (glfwGetKey(window, GLFW_KEY_3) == GLFW_PRESS):
        diffuse -= 0.1
        if(diffuse < 0):
            diffuse = 0
    if (glfwGetKey(window, GLFW_KEY_4) == GLFW_PRESS):
        diffuse += 0.1 
    if (glfwGetKey(window, GLFW_KEY_5) == GLFW_PRESS):
        specular -= 0.1
        if(specular < 0):
            specular = 0
    if (glfwGetKey(window, GLFW_KEY_6) == GLFW_PRESS):
        specular += 0.1   

    # Speed up/down bird.
    if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS):
        aux = bird_speed + 0.01
        bird_speed = min(aux, 0.05)
    if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS):
        aux = bird_speed - 0.01
        bird_speed = max(aux, 0.0)

    return camera

def framebuffer_size_callback(window: GLFWwindow, width: int, height: int) -> None:
    '''
    Whenever the window size changed (by OS or user resize) this callback function executes.
    '''

    # Make sure the viewport matches the new window dimensions note that width and 
    # height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height)

def get_camera_pos():
    '''
    Returns camera current position.
    '''
    
    return camera.Position 