from livewires import games
import motorLib


right = motorLib.Motor()
left = motorLib.Motor(12,16,18,22)


games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):
    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
            left.fwd()
            right.fwd()
        elif games.keyboard.is_pressed(games.K_s):
            self.y += 1
            left.rev()
            right.rev()
        elif games.keyboard.is_pressed(games.K_a):
            self.x -= 1
            right.fwd()
            left.rev()
        elif games.keyboard.is_pressed(games.K_d):
            self.x += 1
            left.fwd()
            right.rev()
        else:
            left.stop()
            right.stop()

def main():
    ship_image = games.load_image("missile.bmp")
    the_ship = Ship(image = ship_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()

main()    
