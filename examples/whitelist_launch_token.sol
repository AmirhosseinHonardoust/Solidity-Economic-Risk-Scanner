// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract WhitelistLaunchToken {
    address public owner;
    mapping(address => bool) public whitelist;
    mapping(address => uint256) public balanceOf;

    bool public tradingEnabled;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 100000 ether;
    }

    modifier onlyOwner() { require(msg.sender == owner, "not owner"); _; }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }

    function addToWhitelist(address user) external onlyOwner {
        whitelist[user] = true;
    }

    function transfer(address to, uint256 amount) external {
        require(tradingEnabled || whitelist[msg.sender], "trading not live");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
    }
}
