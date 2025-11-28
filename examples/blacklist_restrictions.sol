// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BlacklistRestrictions {
    address public owner;
    mapping(address => bool) public blacklisted;
    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 50000 ether;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function setBlacklist(address user, bool b) external onlyOwner {
        blacklisted[user] = b;
    }

    function transfer(address to, uint256 amount) external {
        require(!blacklisted[msg.sender], "blacklisted");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
    }
}
