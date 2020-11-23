
import json

def greeting(name):
    print(f"Hello, {name}.")

def letter_text(**kwargs):
    if "name" and "amount" and "denomination" in kwargs.keys():
        print(f"Hello {kwargs['name']}, this letter is to inform you that you have won {kwargs['amount']} {kwargs['denomination']}.")
    else:
        print("Incorrect parameters supplied.")

my_json_data = {}

with open("input.json","r") as infile:
    my_json_data = json.load(infile)

