import pygame


class Button:
    def __init__(self,*, pos, width, height, value="", onclick=None, disabled=False, font=None) -> None:
        self.__pos = pos
        self.__width = width
        self.__height = height
        self.__onclick = onclick
        self.disabled = disabled
        
        self.__value = value
        self.__font = font

        self.__over_time = 0
    
    def is_inside(self, pos):
        fx,fy = self.__pos[0] - self.__width//2, self.__pos[1] - self.__height//2
        tx,ty = pos
        if tx < fx:
            return False
        if tx > fx + self.__width:
            return False
        if ty < fy:
            return False
        if ty > fy + self.__height:
            return False

        return True


    def enable(self):
        self.disabled = False
    def disable(self):
        self.disabled = True

    def click(self):
        self.__onclick()

    def show(self, screen, mousepos):
        fx,fy = self.__pos[0] - self.__width//2, self.__pos[1] - self.__height//2

        if self.disabled:
            pygame.draw.rect(screen, (100,100,100), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)
        else:
            pygame.draw.rect(screen, (max(100, 255-self.__over_time),max(100, 255-self.__over_time),max(100, 255-self.__over_time)), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)

            if self.is_inside(mousepos):
                self.__over_time = min(155, self.__over_time+20)
            else:
                self.__over_time = max(0, self.__over_time-20)

        if self.__value != "" and self.__font != None:
            text_surface = self.__font.render(str(self.__value), False, (0,0,0))

            dx = text_surface.get_rect().width//2
            dy = text_surface.get_rect().height//2

            screen.blit(text_surface, (self.__pos[0]-dx, self.__pos[1]-dy))