import pygame as pg



# Set a class for the player
class Player:
        def __init__(self, size, x_cord, y_cord, speed):
            self.size = size
            self.speed = speed
            self.x_cord = x_cord
            self.y_cord = y_cord
            self.bottom_border = y_cord - (size/2)
            self.top_border = y_cord + (size/2)
            self.left_border = x_cord - (size/2)
            self.right_border = x_cord + (size/2) 
            self.color = 0xff8200
            self.score = 0

        # Method that scores a point for the player  
        def score_point(self):
            self.score += 1   




# Set a class for the basket
class Basket:
    def __init__(self, length, height, x_cord, y_cord, top_barrier):

        self.length = length
        self.height = height
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.top_barrier1 = top_barrier
        self.barrier_list = []
    def set_barrier_list(self):
        for i in range(self.y_cord - 49, self.y_cord + 19):
            self.barrier_list.append(i)

def main():
    # Initialise screen
    pg.init()
    screen_width = 900
    screen_height = 500
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption('Basketall Game')

    ball = Player(50, ((screen_width - 50) // 2), ((screen_height - 50) // 2),  1)
    basket = Basket(100, 20, 800, 150, 100)
    basket.set_barrier_list()
 


    # Fill background
    background_color = (135, 206, 235)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(background_color)


    # Function to update the screen
    def update_screen():
        screen.fill(background_color)
        pg.draw.rect(screen, ball.color, (ball.x_cord, ball.y_cord, ball.size, ball.size))
        pg.draw.rect(screen, 0xFF0000, (basket.x_cord, basket.y_cord, basket.length, basket.height))
        font = pg.font.SysFont(None, 36)
        score_text = font.render("Score: " + str(ball.score), True, (255, 255, 255))
        text_width = score_text.get_width()
        text_x = (screen_width - text_width) // 2
        screen.blit(score_text, (text_x, 10))  # Position the score text at the top left corner
        
        pg.display.flip()

    # Display some text
    font = pg.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

  

    # Event loop
    running = True
    keys = {pg.K_LEFT: False, pg.K_RIGHT: False, pg.K_UP: False, pg.K_DOWN: False}
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                # Set the corresponding key state to True when a key is pressed
                if event.key in keys:
                    keys[event.key] = True
            elif event.type == pg.KEYUP:
                # Set the corresponding key state to False when a key is released
                if event.key in keys:
                    keys[event.key] = False

        # Update the square's position based on key states
        if keys[pg.K_LEFT]:
            if(ball.x_cord != 0 and not (ball.x_cord == 800 and basket.barrier_list.__contains__(ball.y_cord))):
                ball.x_cord -= ball.speed
        if keys[pg.K_RIGHT]:
            if(ball.x_cord != screen_width - ball.size and not (ball.x_cord == 750 and 
                                                                    basket.barrier_list.__contains__(ball.y_cord))):
                ball.x_cord += ball.speed
        if keys[pg.K_UP]:
            if(ball.y_cord != 0 and not (ball.y_cord == (basket.y_cord+20) and ball.x_cord > (basket.x_cord-50))):
                ball.y_cord -= ball.speed
        if keys[pg.K_DOWN]:
            if(ball.y_cord != screen_height-ball.size and not (ball.x_cord > 750 and ball.x_cord < 800 and ball.y_cord == basket.y_cord - ball.size )):
                ball.y_cord += ball.speed
                if(ball.y_cord == basket.y_cord - basket.height and ball.x_cord > 800):
                    ball.score_point()

        # Redraw the screen with the updated position of the square
        update_screen()

main()
# Quit the game
pg.quit()


