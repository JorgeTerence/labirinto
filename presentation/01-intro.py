from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("What is a graph?", font="Consolas").scale(1.5)
        self.play(Write(title))
        # creature = 
        self.wait(1)