from traceback import print_tb
from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # Go to take the one less than the length
    # ABI
    # Address
    print(simple_storage.retreve())

def main():
    read_contract()