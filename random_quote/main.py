import requests
import turtle

QUOTES = "https://dummyjson.com/quotes/random"
AUTHOR = "author"
QUOTE = "quote"
BGCOLOR = "lightyellow"
ALIGNMENT = "center"
FONT = "TimeNewRoman"
BOLD = "bold"
ITALIC = "italic"

def main():
    # Make a request to the dummyjson endpoint and parse out the quote and the author
    response = requests.get(QUOTES)
    data = response.json()
    author = data[AUTHOR]
    quote = data[QUOTE]

    # Create and setup turtle screen background color
    screen = turtle.Screen()
    screen.bgcolor(BGCOLOR)

    # Initialize and hide the turtle object
    t = turtle.Turtle()
    t.hideturtle()

    # Move turtle and write the quote
    t.penup()
    t.goto(0, 50)
    t.write(quote, align=ALIGNMENT, font=(FONT, 16, ITALIC))

    # Move turtle and write the author
    t.penup()
    t.goto(0, -50)
    t.write(f"-{author}", align=ALIGNMENT, font=(FONT, 14, BOLD))

    # Show the output and wait for manually close window
    turtle.done()

if __name__ == "__main__":
    main()