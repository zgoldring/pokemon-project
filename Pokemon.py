
import csv
import sys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# our csv file in the current directory as a global variaable
FILENAME = "PokemonSpreadSheat.csv" 

def write_movies(pokemon_products):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(pokemon_products)
    except Exception as e:
        print(type(e), e)
        exit_program()
        
def read_list():
    try:
        movie_list = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movie_list.append(row)
        return movie_list
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_product(pokemon_products):
    for i in range(len(pokemon_products)):
        products = pokemon_products[i]
        print(str(i+1) + ". Product:" + products[0] + "\n\t Bought Price: $" + products[2] +  "\n\t Current Sell Price: $"+ products[1])
    print()
    
def add_product(pokemon_products):
    name = input("Product Name: ")
    price = input("Product Sell Price: ")
    bought_price = input("Purchased Price:")
    products = []
    products.append(name)
    products.append(price)
    products.append(bought_price)
    pokemon_products.append(products)
    write_movies(pokemon_products)
    print(products[0] + " was added.\n")
    
def exit_program():
    print("Terminating program.")
    sys.exit()
    
def delete_product(pokemon_products):
    bad_data = True
    while bad_data:
        try:
            number = int(input("Product number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(pokemon_products):
            print("There is no product with that number. " +
                  "Please try again.\n")
        else:
            bad_data = False
            
    product = pokemon_products.pop(number-1)
    write_movies(pokemon_products)
    print(product[0] + " was deleted.\n")
def search_product(pokemon_products):
    name = input("Product to search for: ")
    for i in len(pokemon_products):
        products = pokemon_products[i]
        if name == products[0]:
            print(str(i+1) + ". Product:" + products[0] + "\n\t Bought Price: $" + products[2] +  "\n\t Current Sell Price: $"+ products[1])
        
                
def display_menu():
    print("The Pokemon Product List Program\n")
    print("list - List all product")
    print("add - Add a product")
    print("del - Delete a product")
    print("search - Search for a certain product")
    print("exit - Exit program\n")
    
def main():
        display_menu()
        pokemon_products = read_list()
        print(pokemon_products)
        command = input("Enter Command: ")
        
        while (command.lower() != "exit"):
            if command.lower() == "list":
                list_product(pokemon_products)
                display_menu()
                command = input("Enter Command: ")
            elif command.lower() == "add":
                add_product(pokemon_products)
                display_menu()
                command = input("Enter Command: ")
            elif command.lower() == "del":
                delete_product(pokemon_products)
                display_menu()
                command = input("Enter Command: ")
            elif command.lower() == "search":
                search_product(pokemon_products)
                display_menu()
                command = input("Enter Command: ")
            elif command.lower() == "exit":
                continue
            else:
                print("Not a valid command.  Please try again.\n")
                command = input("Enter Command: ")

        print("You'll be back!")     
        
if __name__ == "__main__":
    main()