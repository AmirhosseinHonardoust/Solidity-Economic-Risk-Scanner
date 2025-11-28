// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UnsafeLending {
    mapping(address => uint256) public collateral;
    mapping(address => uint256) public debt;
    int256 public price = 1e18;

    function deposit() external payable {
        collateral[msg.sender] += msg.value;
    }

    function borrow(uint256 amount) external {
        debt[msg.sender] += amount;
    }

    //  No LTV check at all, huge economic risk
    function liquidate(address user) external {
        require(int256(collateral[user]) * price < int256(debt[user]), "healthy");
        debt[user] = 0;
        collateral[user] = 0;
    }

    function setPrice(int256 p) external {
        price = p;
    }
}
