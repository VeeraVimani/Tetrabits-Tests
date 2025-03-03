from ursina import *

app = Ursina()

# Load assets
car = Entity(model='cube', color=color.red, scale=(1, 0.5, 2), position=(0, 0, 0))
road = Entity(model='plane', texture='white_cube', scale=(10, 1, 100), position=(0, -0.5, 50))

camera.position = (0, 5, -10)
camera.rotation_x = 30

def update():
    car.x -= held_keys['a'] * 5 * time.dt
    car.x += held_keys['d'] * 5 * time.dt
    car.z += 5 * time.dt

app.run()
