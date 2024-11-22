from glfw import _GLFWwindow as GLFWwindow
from glfw.GLFW import *
from OpenGL.GL import *
from camera import Camera, Camera_Movement
import glm

WIDTH = 1920
HEIGHT = 1080

camera = Camera(glm.vec3(0.0, 0.0, 3.0))
lastX = WIDTH / 2.0
lastY = HEIGHT / 2.0
firstMouse = True

# timing
lastFrame = 0.0

rose_scale_y = 0.05
sky_rotation_angle = 0.0
bird_speed = 0.00
bird_radius = 80.0
bird_angle = 0.0
shrek_step = 0.0
shrek_side_step = 0.0

# glfw: whenever the mouse moves, this callback is called
# -------------------------------------------------------
def mouse_callback(window: GLFWwindow, xpos: float, ypos: float) -> None:
    global lastX, lastY, firstMouse

    if (firstMouse):

        lastX = xpos
        lastY = ypos
        firstMouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos # reversed since y-coordinates go from bottom to top

    lastX = xpos
    lastY = ypos

    camera.ProcessMouseMovement(xoffset, yoffset)

# glfw: whenever the mouse scroll wheel scrolls, this callback is called
# ----------------------------------------------------------------------
def scroll_callback(window: GLFWwindow, xoffset: float, yoffset: float) -> None:

    camera.ProcessMouseScroll(yoffset)


# process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
# ---------------------------------------------------------------------------------------------------------
def processInput(window: GLFWwindow, deltaTime) -> None:

    global rose_scale_y
    global bird_speed
    global bird_radius
    global bird_angle
    global shrek_side_step
    global shrek_step

    exclusion_zones = [
        (-8, -30, 6, 1),
        (5, -9, 25, -2),             
    ]

    deltaTime *= 5

    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS):
        glfwSetWindowShouldClose(window, True)

    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS):
        camera.ProcessKeyboard(Camera_Movement.FORWARD, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS):
        camera.ProcessKeyboard(Camera_Movement.BACKWARD, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS):
        camera.ProcessKeyboard(Camera_Movement.LEFT, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS):
        camera.ProcessKeyboard(Camera_Movement.RIGHT, deltaTime)
    if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS):
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)
    if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS):
        aux = rose_scale_y - 0.01
        rose_scale_y = max(aux,0.05)
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

    # Speed up bird ('→' key).
    if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS):
        aux = bird_speed + 0.01
        bird_speed = min(aux, 0.05)

    # Speed down bird ('←' key).
    if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS):
        aux = bird_speed - 0.01
        bird_speed = max(aux, 0.0)

    return camera

# glfw: whenever the window size changed (by OS or user resize) this callback function executes
# ---------------------------------------------------------------------------------------------
def framebuffer_size_callback(window: GLFWwindow, width: int, height: int) -> None:

    # make sure the viewport matches the new window dimensions note that width and 
    # height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height)