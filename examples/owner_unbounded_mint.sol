// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract OwnerUnboundedMint {
    address public owner;
    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000 ether;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function mint(address to, uint256 amount) external onlyOwner {
        balanceOf[to] += amount;
    }
}
