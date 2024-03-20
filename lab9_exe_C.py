'''
Name : lab9_exe_C.py
Assignment : Lab 9 , Exercise C
Author ( s ) : Aaryan Dhand , Mohammed Yassin
Submission : March 20, 2024
Description : External jason data with python.

'''
import requests
import json

def fetch_product_data(url):
    try :
        response = requests.get( url )
        # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure includes a ' products ' key
        return response.json() ['products']
    except requests.exceptions.RequestException as e :
        print (f"Error fetching data : { e }")
        return None
    
def list_all_products(products):
    for product in products:
        # Print product title for each product
        print(product['title'])

def search_product(products, name):
    for product in products:
        #prints product details if the name matches the titl
        if product['title'] == name:
            # Print product details with 4 indents
            print(f"                ID: {product['id']}")
            print(f"                Product Name: {product['title']}")
            print(f"                Product Description: {product['description']}")
            print(f"                Product Price: {product['price']}")
            print(f"                Discount Percentage: {product['discountPercentage']}")
            print(f"                Rating: {product['rating']}")
            print(f"                Stock: {product['stock']}")
            print(f"                Brand: {product['brand']}")
            print(f"                Category: {product['category']}")
            print(f"                Thumbnail: {product['thumbnail']}")
            print(f"                Images: {product['images']}")
            return

    print("Product not found.")

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            #take user input for options
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")
            #check if input matches the options
            if choice == '1':
                #calls list_all_products function
                list_all_products(products)
            elif choice == '2':
                #takes user input and calls search_product function
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                #exits while loop ending the program
                break
            else:
                #if there is no match prints invalid choice
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
    main()
    