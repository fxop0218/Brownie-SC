from brownie import SimpleStorage, accounts
    # Arrange

    # Act

    # Assert
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from" : account})
    starting_val = simple_storage.retrive()
    expected = 0
    # Assert
    assert starting_val == expected

def test_update():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})

    # Assert
    assert expected == simple_storage.retrive()