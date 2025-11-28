// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VariableTaxToken {
    address public owner;
    uint256 public buyTaxBps;
    uint256 public sellTaxBps;

    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        buyTaxBps = 500;
        sellTaxBps = 1000;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function setBuyTax(uint256 newTax) external onlyOwner {
        buyTaxBps = newTax; // can be set to 10000 → 100% tax
    }

    function setSellTax(uint256 newTax) external onlyOwner {
        sellTaxBps = newTax;
    }

    function transfer(address to, uint256 amount) external {
        uint256 tax = amount * buyTaxBps / 10000;
        uint256 sendAmount = amount - tax;
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += sendAmount;
    }
}
