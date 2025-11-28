// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ManualOracle {
    address public owner;
    int256 public price;

    constructor(int256 p) {
        owner = msg.sender;
        price = p;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function setPrice(int256 p) external onlyOwner {
        price = p; //  dangerous: owner can set any price
    }

    function getPrice() external view returns (int256) {
        return price;
    }
}
