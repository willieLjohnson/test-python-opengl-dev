import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos


def main():
    # Initialize the library
    if not glfw.init():
        raise Exception("Can not be initalized!")
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    vertices = [-0.5, -0.5, 0.0,
                0.5, -0.5, 0.0,
                0.0, 0.5, 1.0]

    colors = [1.5, 0.0, 0.0,
              0.0, 1.0, 0.0,
              0.0, 0.0, 1.0]

    vertices = np.array(vertices, dtype=np.float32)
    colors = np.array(colors, dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glClearColor(0, 0.1, 0.1, 1)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)

        ct = glfw.get_time()

        glLoadIdentity()
        glScale(abs(sin(ct)), abs(sin(ct)), 1)
        glRotatef(sin(ct) * 45, 0, 0, 1)
        glTranslatef(sin(ct), cos(ct), 0)

        glDrawArrays(GL_TRIANGLES, 0, 3)
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
