# import math
# import sys
# from os import rename

# name = input("Your Name: ")
# print("Hi!!", name)

import requests

r = requests.get("https://coreyms.com")


# def greet(who_to_greet):
#    greeting = f"Hello, {who_to_greet}"
#    return greeting


print(r.status_code)
print(r.ok)
# print(greet("Vicky"))
