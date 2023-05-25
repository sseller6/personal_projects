"""
Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import arcade
import math

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_ENEMY = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Player Controlled Sprite and Autonomous Enemy Sprite"

MOVEMENT_SPEED = 5

ENEMY_SPEED = 3.0


class Player(arcade.Sprite):

    """ Player Class """
    character_width = 20
    character_height = 20


    def update(self):

        """ Move the player """

        # Move player.

        # Remove these lines if physics engine is moving player.

        self.center_x += self.change_x

        self.center_y += self.change_y



        # Check for out-of-bounds

        if self.left < 0:

            self.left = 0

        elif self.right > SCREEN_WIDTH - 1:

            self.right = SCREEN_WIDTH - 1



        if self.bottom < 0:

            self.bottom = 0

        elif self.top > SCREEN_HEIGHT - 1:

            self.top = SCREEN_HEIGHT - 1

class Enemy(arcade.Sprite):
    """
    This class represents the Enemy on our screen.
    """

    def __init__(self, image, scale, position_list):
        super().__init__(image, scale)
        self.position_list = position_list
        self.cur_position = 0
        self.speed = ENEMY_SPEED

    def update(self):
        """ Have a sprite follow a path """

        # Where are we
        start_x = self.center_x
        start_y = self.center_y

        # Where are we going
        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

        # X and Y diff between the two
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # Calculate angle to get there
        angle = math.atan2(y_diff, x_diff)

        # How far are we?
        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        # How fast should we go? If we are close to our destination,
        # lower our speed so we don't overshoot.
        speed = min(self.speed, distance)

        # Calculate vector to travel
        change_x = math.cos(angle) * speed
        change_y = math.sin(angle) * speed

        # Update our location
        self.center_x += change_x
        self.center_y += change_y

        # How far are we?
        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        # If we are there, head to the next point.
        if distance <= self.speed:
            self.cur_position += 1

            # Reached the end of the list, start over.
            if self.cur_position >= len(self.position_list):
                self.cur_position = 0

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player("player_move\mage_1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # List of points the enemy will travel to.
        position_list = [[50, 50],
                         [700, 50],
                         [700, 500],
                         [50, 500]]
        
        # Create the enemy
        enemy = Enemy("player_move/enemy_melee_2.0.png",
                        SPRITE_SCALING_ENEMY,
                        position_list)
        
        # Set initial location of the enemy at the first point
        enemy.center_x = position_list[0][0]
        enemy.center_x = position_list[0][1]

        # Add the enemy to the enemy list
        self.enemy_list.append(enemy)

    def on_draw(self):
        """
        Render the screen. This MUST include drawing the player and the enemy. (In the future it will include obstacles list.)
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.player_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """


        # Move the player

        self.player_list.update()

        # Move the enemy

        self.enemy_list.update()



    def on_key_press(self, key, modifiers):

        """Called whenever a key is pressed. """



        # If the player presses a key, update the speed

        if key == arcade.key.UP:

            self.player_sprite.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:

            self.player_sprite.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.LEFT:

            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:

            self.player_sprite.change_x = MOVEMENT_SPEED



    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """



        # If a player releases a key, zero out the speed.

        # This doesn't work well if multiple keys are pressed.

        # Use 'better move by keyboard' example if you need to

        # handle this.

        if key == arcade.key.UP or key == arcade.key.DOWN:

            self.player_sprite.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:

            self.player_sprite.change_x = 0



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()