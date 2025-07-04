import requests
import turtle

def main():
    # Make a request to the dummyjson endpoint and parse out the quote and the author
    response = requests.get("https://dummyjson.com/quotes/random")
    data = response.json()
    author = data["author"]
    quote = data["quote"]

    # Create and setup turtle screen background color
    screen = turtle.Screen()
    screen.bgcolor("lightyellow")

    # Initialize and hide the turtle object
    t = turtle.Turtle()
    t.hideturtle()

    # Move turtle and write the quote
    t.penup()
    t.goto(0, 50)
    t.write(quote, align="center", font=("TimeNewRoman", 16, "italic"))

    # Move turtle and write the author
    t.penup()
    t.goto(0, -50)
    t.write(f"-{author}", align="center", font=("TimeNewRoman", 14, "bold"))

    # Show the output and wait for manually close window
    turtle.done()

if __name__ == "__main__":
    main()