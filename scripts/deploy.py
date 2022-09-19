from brownie import accounts, config, SimpleStorage, network
import os
# brownie accounts new name == to create new account with code and private key
# brownie networks list == to see all the networks
def deploy_simple_storage():
    # 1 method
    # account = accounts [0]
    # print(account)
    # 2 method
    # account = accounts.load("fxop02")
    # print(account)
    # 3 method
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    # 4 method
    #account = accounts.add(config["wallets"]["from_key"])
    account = getAccount()
    simple_storage = SimpleStorage.deploy({"from" : account})
    strored_value = simple_storage.retrive()
    print(strored_value)
    transaction = simple_storage.store(15, {"from" : account})
    transaction.wait(1)
    update_transaction = simple_storage.retrive()
    print(update_transaction)

def getAccount():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()