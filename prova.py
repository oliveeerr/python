import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
def centro(x,y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 25, arcade.color.OLIVE_DRAB)
    arcade.draw_circle_filled(x, y, 5, arcade.color.WHITE)

def pilota(x,y):
    arcade.draw_circle_filled(x, y, 20, arcade.color.ORANGE)

def lluna(x,y):
    arcade.draw_circle_filled(x+15, y, 30, arcade.color.GOLD)
    arcade.draw_circle_filled(x, y+5, 30, arcade.color.MIDNIGHT_BLUE)

def linea(x,y):
    arcade.draw_lrtb_rectangle_filled(x, 7+x, y+300, y, arcade.csscolor.WHITE)

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.OLIVE_DRAB)

def porteria(x,y):
    arcade.draw_lrtb_rectangle_filled(x, 5+x, y+150, y, arcade.csscolor.WHITE)


def nuvol (x,y):
    arcade.draw_circle_filled(x, y, 35, arcade.csscolor.SILVER)
    arcade.draw_circle_filled(40+x, y, 35, arcade.csscolor.SILVER)
    arcade.draw_circle_filled(80+x, +y, 35, arcade.csscolor.SILVER)

def draw_snow_person(x, y,color):
    """ Draw a snow person """
   # Snow
    arcade.draw_circle_filled(x,90 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 110 + y, 25, color)
    arcade.draw_circle_filled(x, 140 + y, 25, arcade.color.WHITE)

  
    # Eyes
    arcade.draw_circle_filled(x - 10, 150 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 10, 150 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(x , 140 + y, 3, arcade.color.SIENNA)
def ninots():
    draw_grass()
    draw_snow_person(150, 100,arcade.color.BLACK)
    draw_snow_person(400, 90,arcade.color.BLACK)
    draw_snow_person(100, 30,arcade.color.BLACK)
    draw_snow_person(250, 100,arcade.color.DEEP_PINK)
    draw_snow_person(500, 100,arcade.color.DEEP_PINK)
    draw_snow_person(550, 10,arcade.color.DEEP_PINK)
    nuvol(100,500)
    lluna(450,500)
    linea(296,0)
    centro(300,150)
    porteria(0,75)
    porteria(595,80)
    pilota(130,100)

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1


        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class Gel (Ball):
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        
        
        if self.position_y < 0:
            self.position_y = SCREEN_HEIGHT

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE)

        self.llista = []    

                # Attributes to store where our ball is
        self.llista.append(Gel(10, 50, 0, -5, 5, arcade.color.WHITE))
        self.llista.append(Gel(50, 40, 0, -6, 5, arcade.color.WHITE))
        self.llista.append(Gel(100, 20, 0, -3, 5, arcade.color.WHITE))
        self.llista.append(Gel(130, 50, 0, -6, 5, arcade.color.WHITE))
        self.llista.append(Gel(150, 40, 0, -7, 5, arcade.color.WHITE))
        self.llista.append(Gel(200, 110, 0, -4, 5, arcade.color.WHITE))
        self.llista.append(Gel(250, 30, 0, -8, 5, arcade.color.WHITE))
        self.llista.append(Gel(300, 10, 0, -7, 5, arcade.color.WHITE))
        self.llista.append(Gel(350, 50, 0, -6, 5, arcade.color.WHITE))
        self.llista.append(Gel(400, 40, 0, -5, 5, arcade.color.WHITE))
        self.llista.append(Gel(450, 20, 0, -7, 5, arcade.color.WHITE))
        self.llista.append(Gel(500, 110, 0, -4, 5, arcade.color.WHITE))
        self.llista.append(Gel(550, 30, 0, -5, 5, arcade.color.WHITE))
        self.llista.append(Gel(600, 10, 0, -6, 5, arcade.color.WHITE))
        self.llista.append(Gel(25, 40, 0, -2, 5, arcade.color.WHITE))
        self.llista.append(Gel(175, 20, 0, -9, 5, arcade.color.WHITE))
        self.llista.append(Gel(275, 110, 0, -5, 5, arcade.color.WHITE))
        self.llista.append(Gel(375, 30, 0, -3, 5, arcade.color.WHITE))
        self.llista.append(Gel(475, 10, 0, -5, 5, arcade.color.WHITE))
        self.llista.append(Gel(575, 10, 0, -8, 5, arcade.color.WHITE))

    def on_draw(self):
        """ Called whenever we need to draw the window. """

        arcade.start_render()
        ninots()


        
        for i in self.llista:
                i.draw()

      

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        for i in self.llista:
                i.update()
  
    


def main():

    
    window=MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    
    
    
    ninots()
    

    # Finish and run
    arcade.run()

main()