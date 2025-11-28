// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DeflationaryTaxToken {
    address public owner;
    uint256 public burnBps = 2000; // 20%
    uint256 public taxBps = 800;   // 8%

    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 20000 ether;
    }

    function transfer(address to, uint256 amount) external {
        uint256 burn = amount * burnBps / 10000;
        uint256 tax = amount * taxBps / 10000;
        uint256 sendAmount = amount - burn - tax;

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += sendAmount;
        // burn and tax tokens disappear or go to owner
    }
}
