from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()   # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency
        self.play(Create(circle))  # show the circle on screen
        




class FadingText(Scene):
    def construct(self):
        # Create the text
        text = Tex("Hello, Manim!", color=WHITE).scale(2)

        # Fade in the text
        self.play(FadeIn(text))

        # Wait for a moment
        self.wait(2)

        # Fade out the text
        self.play(FadeOut(text))

        # Wait for a moment
        self.wait()