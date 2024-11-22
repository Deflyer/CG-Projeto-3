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
    
    # Grows rose ('↑' key).
    if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS):
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)

    # Decreses rose ('↓' key).
    if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS):
        aux = rose_scale_y - 0.01
        rose_scale_y = max(aux,0.05)

    return camera

# glfw: whenever the window size changed (by OS or user resize) this callback function executes
# ---------------------------------------------------------------------------------------------
def framebuffer_size_callback(window: GLFWwindow, width: int, height: int) -> None:

    # make sure the viewport matches the new window dimensions note that width and 
    # height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height)