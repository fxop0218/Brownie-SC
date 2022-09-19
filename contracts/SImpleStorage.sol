// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    // Initializen in 0
    uint256 public favoriteNumber;
    bool favoriteBool;

    // OOP 
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people; // Array 
    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People(123,  "Pepe");

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // View, pure
    function retrive() public view returns(uint256) {
        return favoriteNumber; 
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name)); // Add any thing in the array
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
