# Configures all the needed components of our screen.

from glfw.GLFW import *
from OpenGL.GL import *
import glm

WIDTH = 1920
HEIGHT = 1080

def init_window():

    glfwInit()
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

    window = glfwCreateWindow(WIDTH, HEIGHT, "Project 3", None, None)
    glfwMakeContextCurrent(window)

    return window

def set_callbacks(window, frame_cb, mouse_cb, scroll_cb):
    '''
    Inicializates all the needed callbacks.
    '''

    glfwSetFramebufferSizeCallback(window, frame_cb)
    glfwSetCursorPosCallback(window, mouse_cb)
    glfwSetScrollCallback(window, scroll_cb)

def send_data_to_gpu(cubeVAO, VBO, combined_vertexes):
    '''
    Requests GPU slots to our program data and then sends this data to the slot.
    '''

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, combined_vertexes.nbytes, combined_vertexes.ptr, GL_STATIC_DRAW)

    glBindVertexArray(cubeVAO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(3 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(6 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(2)

    # Configure the light's VAO (VBO stays the same the vertices are the same for the light object which is also a 3D cube).
    lightCubeVAO = glGenVertexArrays(1)
    glBindVertexArray(lightCubeVAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)

    return lightCubeVAO