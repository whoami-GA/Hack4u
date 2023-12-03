games = ["Super Mario", "Zelda", "CyberBug2077", "FinalFantasy VII"]
top = int(input("The Value of sales that you want: "))
# Gener
genres = {
        "Super Mario": "Aventure",
        "Zelda": "Aventure",
        "CyberBug2077": "Rol",
        "FinalFantasy VII": "Rol"
}

# Sales and stocks
sales_and_stocks = {
        "Super Mario": (400,  200),
        "Zelda": (600, 20),
        "CyberBug2077": (40, 1000),
        "FinalFantasy VII": (924, 3)
}

# Customers
customers = {
        "Super Mario": {"Adrian", "Shadow", "Striker", "Securiters","DragStar"},
        "Zelda": {"Adrian", "Shadow", "Striker", "Ion", "Vasile"},
        "CyberBug2077": {"Adrian", "Shadow", "Securiters", "Raquel", "Albert"},
        "FinalFantasy VII": {"Adrian", "Striker", "Shadow", "Maichel", "Ulm"}
}

#game = input(f"what do to want to check?{games}: ")

def sumarios(game):
    # Sumario
    print(f"\n[i]Resume of the Game: {game}\n")
    print(f"\t[+]Genres of the Game: {genres[game]}")
    print(f"\t[+]Total Sales of this Game: {sales_and_stocks[game][0]} has saled")
    print(f"\t[+]Total Stock of this Game: {sales_and_stocks[game][1]} missing to sell")
    print(f"\t[+]Customers thath has acquired the Game: {', '.join(customers[game])}")

for game in games:
    if sales_and_stocks[game][0] > top:
        sumarios(game)
                                                      #.item because is an tuple
total_sales = lambda: sum(sales for game, (sales, _) in sales_and_stocks.items() if sales_and_stocks[game][0] > to
                                #is a tuple and the oputpu need to have()
print(f"\nThe total sales are {total_sales()} products\n")


jame = input("Print el juego: ")
if jame == "Zelda":
    print(f"\t[+]All the cusmoters that have the game are: {', '.join(customers[jame])}\n")
if jame == "FinalFantasy VII":
    print(f"\t[+]All the cusmoters that have the game are: {', '.join(customers[jame])}\n")
if jame == "Super Mario":
    print(f"\t[+]All the cusmoters that have the game are: {', '.join(customers[jame])}\n")
if jame == "CyberBug2077":
    print(f"\t[+]All the cusmoters that have the game are: {', '.join(customers[jame])}\n")
