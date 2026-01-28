alien = {'color': 'green', 'points' : 5, 
         'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
new_points = alien['points']

if(alien['speed'] == 'slow'):
    x_increment = 1
elif(alien['speed'] == 'medium'):
    x_increment = 2
else:
    x_increment = 3

print(f"you just earned {new_points} points")
print(f"original position: {alien['x_position']}")
print(alien)

alien['x_position'] = alien['x_position'] + x_increment

print(f"new position: {alien['x_position']}")

for key, value in alien.items():
    print(f"\nKey: {key}")
    print(f"{value}")

for key in alien.keys():
    print(f"\n key: {key}")

# tem os métodos key()s, values(), items, set()-> pega valores únicos

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)