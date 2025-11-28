// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ReflectionToken {
    uint256 public totalSupply = 1_000_000 ether;
    mapping(address => uint256) public balanceOf;

    uint256 public taxBps = 500;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 amount) external {
        uint256 tax = amount * taxBps / 10000;
        uint256 sendAmount = amount - tax;

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += sendAmount;

        // redistribute tax equally (simplified)
        balanceOf[msg.sender] += tax;
    }
}
