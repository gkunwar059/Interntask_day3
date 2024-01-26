# 16. Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.


class Mario:
    def __init__(self):
        self.position = [0, 0] # [x, y] coordinates
        self.score = 0
        self.health = 100
        self.level = 1

    def move(self, direction):
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1

    def jump(self):
        self.position[1] += 2

    def collect_coin(self):
        self.score += 10

    def kill_enemy(self):
        self.score += 100
        self.health += 10

# Test
mario = Mario()
mario.move('right')
mario.jump()
mario.collect_coin()
mario.kill_enemy()
print(mario.position) 
print(mario.score) 
print(mario.health) 
