// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ManualPriceOracle {
    address public owner;
    int256 public price;

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    constructor(int256 initialPrice) {
        owner = msg.sender;
        price = initialPrice;
    }

    function setPrice(int256 newPrice) external onlyOwner {
        price = newPrice;
    }

    function getPrice() external view returns (int256) {
        return price;
    }
}
