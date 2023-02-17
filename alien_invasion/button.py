import pygame.font # font module can render texts to the screen


class Button:

    def __init__(self, ai_settings, screen, msg):
        """initialize the attributes of buttons"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the size and other properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # None means using the default font
        self.font = pygame.font.SysFont(None, 48)

        # create rect object of the button and place it in the middle of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the label for the button only need to be created once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """render the msg as an image, and center it on the button"""
        # font.render() render the text to image
        # the 2nd param indicates anti-aliasing, which make the edges smoother
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a button filled with colors and then draw the text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
