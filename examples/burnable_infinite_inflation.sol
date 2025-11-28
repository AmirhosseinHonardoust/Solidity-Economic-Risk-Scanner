// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BurnableInfiniteInflation {
    address public owner;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        totalSupply = 1000 ether;
        balanceOf[msg.sender] = totalSupply;
    }

    function burn(uint256 amount) external {
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;
    }

    // Also infinite minting
    function mint(uint256 amount) external {
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
    }
}
