# Configures all the needed components of our screen.

from glfw.GLFW import *

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