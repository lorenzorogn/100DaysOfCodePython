# import turtle

# timmy = turtle.Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkRed")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electic", "Water", "Fire"])

table.align = "l"

print(table)


