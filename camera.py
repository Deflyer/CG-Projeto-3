# File that handles all camera functionalities by creating the Camera and Camera_Movement classes. 
# This code was created by our professor Jean Roberto Ponciano.

import glm
from enum import Enum

# Default camera values
YAW         = -90.0
PITCH       =  0.0
SPEED       =  12.5
SENSITIVITY =  0.1
ZOOM        =  45.0

skyfix = glm.vec3(0.0,  -72.0,  0.0)

class Camera_Movement(Enum):
    '''
    Defines several possible options for camera movement. Used as abstraction to stay away from window-system specific input methods.
    '''

    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class Camera:
    '''
    An abstract camera class that processes input and calculates the corresponding Euler Angles, Vectors and Matrices for use in OpenGL.
    '''

    def __init__(self, *args, **kwargs):

        if (len(args) == 8 and len(kwargs) == 0):
            posX, posY, posZ, upX, upY, upZ, yaw, pitch = args
            
            self.Position = glm.vec3(posX, posY, posZ)
            self.WorldUp = glm.vec3(upX, upY, upZ)
            self.Yaw = yaw
            self.Pitch = pitch

        elif (len(args) + len(kwargs) <= 4):
            keyword_arguments = ("position", "up", "yaw", "pitch")
            keyword_arguments_defaults = {"position" : glm.vec3(), "up" : glm.vec3(0,1,0), "yaw" : YAW, "pitch" : PITCH}

            for i in range(len(args)):
                kw = keyword_arguments[i]
                value = args[i]
                kwargs[kw] = value

            keyword_arguments_defaults.update(kwargs)

            self.Position = keyword_arguments_defaults["position"]
            self.WorldUp = keyword_arguments_defaults["up"]
            self.Yaw = keyword_arguments_defaults["yaw"]
            self.Pitch = keyword_arguments_defaults["pitch"]

        else:
            raise TypeError("Invalid argument count for Camera()")

        self.Front = glm.vec3(0.0, 0.0, -1.0)
        self.Up = glm.vec3()
        self.Right = glm.vec3()
        self.MovementSpeed = SPEED
        self.MouseSensitivity = SENSITIVITY
        self.Zoom = ZOOM
        
        self.updateCameraVectors()

    def GetViewMatrix(self) -> glm.mat4:
        '''
        Returns the view matrix calculated using Euler Angles and the LookAt Matrix.
        '''
        
        return glm.lookAt(self.Position, self.Position + self.Front, self.Up)

    def ProcessKeyboard(self, direction: Camera_Movement, deltaTime: float) -> None:
        '''
        Processes input received from any keyboard-like input system. Accepts input parameter in the form of
        camera defined ENUM (to abstract it from windowing systems).
        '''
        
        velocity = self.MovementSpeed * deltaTime
        if (direction == Camera_Movement.FORWARD):
            valid = True
            nova_pos =  self.Position + self.Front * velocity
            if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
                valid = False
            if valid:
                self.Position = nova_pos
        if (direction == Camera_Movement.BACKWARD):
            valid = True
            nova_pos =  self.Position - self.Front * velocity
            if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
                valid = False
            if valid:
                self.Position = nova_pos
        if (direction == Camera_Movement.LEFT):
            valid = True
            nova_pos =  self.Position - self.Right * velocity
            if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
                valid = False
            if valid:
                self.Position = nova_pos
        if (direction == Camera_Movement.RIGHT):
            valid = True
            nova_pos =  self.Position + self.Right * velocity
            if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
                valid = False
            if valid:
                self.Position = nova_pos

    def ProcessMouseMovement(self, xoffset: float, yoffset: float, constrainPitch: bool = True) -> None:
        '''
        Processes input received from a mouse input system. Expects the offset value in both the x and y direction.
        '''
        
        xoffset *= self.MouseSensitivity
        yoffset *= self.MouseSensitivity

        self.Yaw   += xoffset
        self.Pitch += yoffset

        # Make sure that when pitch is out of bounds, screen doesn't get flipped.
        if (constrainPitch):
            if (self.Pitch > 89.0):
                self.Pitch = 89.0
            if (self.Pitch < -89.0):
                self.Pitch = -89.0

        # Update Front, Right and Up Vectors using the updated Euler angles.
        self.updateCameraVectors()

    def ProcessMouseScroll(self, yoffset: float) -> None:
        '''
        Processes input received from a mouse scroll-wheel event. Only requires input on the vertical wheel-axis.
        '''

        self.Zoom -= yoffset
        if (self.Zoom < 1.0):
            self.Zoom = 1.0
        if (self.Zoom > 45.0):
            self.Zoom = 45.0
            
    def updateCameraVectors(self) -> None:
        '''
        Calculates the front vector from the Camera's (updated) Euler Angles.
        '''
        
        # Calculate the new Front vector.
        front = glm.vec3()
        front.x = glm.cos(glm.radians(self.Yaw)) * glm.cos(glm.radians(self.Pitch))
        front.y = glm.sin(glm.radians(self.Pitch))
        front.z = glm.sin(glm.radians(self.Yaw)) * glm.cos(glm.radians(self.Pitch))
        self.Front = glm.normalize(front)

        # Also re-calculate the Right and Up vector.
        # Normalize the vectors, because their length gets closer to 0 the more you look up or down which results in slower movement.
        self.Right = glm.normalize(glm.cross(self.Front, self.WorldUp))
        self.Up    = glm.normalize(glm.cross(self.Right, self.Front))