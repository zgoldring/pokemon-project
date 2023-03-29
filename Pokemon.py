# Pokemon inventory sorter and searcher
import csv
import sys
import PySimpleGUI as sg

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
##Done
def list_product(pokemon_products):
    for i in range(len(pokemon_products)):
        if len(pokemon_products[i]) > 1:
            products = pokemon_products[i]
            list = [
                [sg.Text("Product Name:" + products[0])], 
                [sg.Text("Number of Products:" + products[1])], 
                [sg.Text("Is it Sealed?:" + products[2])],
                [sg.Text("What Condition is the Product?:" + products[3])],
                [sg.Text("Purchased Price:" + products[4])],
                [sg.Text("Product Market Value:" + products[5])],
                [sg.Button("Continue")],
                [sg.Button("Back")],
                [sg.Button("Exit")]
                ]   
            window = sg.Window('List Products', list)
            event, values = window.read()
            window.close()
            if event in (sg.Button, "Continue"):
                continue
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
##done 
def add_product(pokemon_products):
    add = [
        [sg.Text("Product Name:"), sg.InputText()], 
        [sg.Text("Number of Products:"), sg.InputText()], 
        [sg.Text("Is it Sealed?:"), sg.InputText()],
        [sg.Text("What Condition is the Product?:"), sg.InputText()],
        [sg.Text("Purchased Price:"), sg.InputText()],
        [sg.Text("Product Market Value:"), sg.InputText()],
        [sg.Button("Add Product to List")],
        [sg.Button("Back")]
        ]
        
    window = sg.Window('Add Product', add)
    event, values = window.read()
    window.close()
    name = values[0]
    quantity = values[1]
    sealed = values[2]
    condition = values[3]
    bought_price = values[4]
    price = values[5]
    if event in (sg.Button, "Add Product to List"):
        products = []
        products.append(name)
        products.append(quantity)
        products.append(sealed)
        products.append(condition)
        products.append(bought_price)
        products.append(price)
        pokemon_products.append(products)
        write_movies(pokemon_products)
        output = [
            [sg.Text("Product Has Been Added!")],
            [sg.Button("Close")]
        ]
        window = sg.Window('Proudct Added', output)
        event, values = window.read()
        window.close()
#Done
def delete_product(pokemon_products):
    search = [
        [sg.Text("Enter Product to delete"), sg.InputText()],
        [sg.Button("Search")],
        [sg.Button("Exit")]
    ]
    window = sg.Window('Search Products', search)
    
    event, values = window.read()
    window.close()
    if event in (sg.Button, "Search"):
        for i in range(len(pokemon_products)):
            products = pokemon_products[i]
            found = False
            if values[0] == products[0]:
                if len(pokemon_products[i]) > 1:
                    found = True
                    product = pokemon_products.pop(i)
                    write_movies(pokemon_products)
                    found_product = [
                        [sg.Text(values[0] + " has been deleted!")], 
                        [sg.Button("Close")]
                        ]   
                    window = sg.Window('Searched Product', found_product)
                    event, values = window.read()
                    window.close()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
        if found == False:
                not_found = [
                    [sg.Text("Product Does Not Exist!")]
                ]
                window = sg.Window('Product not found', not_found)
                event,something = window.read()

##Done
def search_product(pokemon_products):
    search = [
        [sg.Text("Enter Product to search for"), sg.InputText()],
        [sg.Button("Search")],
        [sg.Button("Exit")]
    ]
    window = sg.Window('Search Products', search)
    
    event, values = window.read()
    window.close()
    if event in (sg.Button, "Search"):
        for i in range(len(pokemon_products)):
            products = pokemon_products[i]
            found = False
            if values[0] == products[0]:
                if len(pokemon_products[i]) > 1:
                    found = True
                    found_product = [
                        [sg.Text("Product Name:" + products[0])], 
                        [sg.Text("Number of Products:" + products[1])], 
                        [sg.Text("Is it Sealed?:" + products[2])],
                        [sg.Text("What Condition is the Product?:" + products[3])],
                        [sg.Text("Purchased Price:" + products[4])],
                        [sg.Text("Product Market Value:" + products[5])],
                        [sg.Button("Close")]
                        ]   
                    window = sg.Window('Searched Product', found_product)
                    event, values = window.read()
                    window.close()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
        if found == False:
                not_found = [
                    [sg.Text("Product Does Not Exist!")]
                ]
                window = sg.Window('Product not found', not_found)
                event,something = window.read()
                    
##Done
def display_menu():
    layout = [
        [sg.Button("Add Product")],
        [sg.Button("List All Products")],
        [sg.Button("Search for a Product")],
        [sg.Button("Delete a Product")],
        [sg.Button("Exit")]
    ]
    pokemon_products = read_list()
    window = sg.Window("Pokemon Project", layout)
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Add Product":
            add_product(pokemon_products)
        if event == "List All Products":
            list_product(pokemon_products)
        if event == "Search for a Product":
            search_product(pokemon_products)
        if event == "Delete a Product":
            delete_product(pokemon_products)
    window.close()
    
def main():
    display_menu()
if __name__ == "__main__":
    main()