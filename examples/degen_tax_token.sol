// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DegenTaxToken {
    string public name = "DegenTaxToken";
    string public symbol = "DTT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;
    mapping(address => uint256) public balanceOf;
    mapping(address => bool) public blacklist;

    uint256 public taxFeeBps = 1500; // 15%
    uint256 public burnFeeBps = 500; // 5%

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        totalSupply = 1_000_000 ether;
        balanceOf[msg.sender] = totalSupply;
    }

    function setTaxFee(uint256 _newFeeBps) external onlyOwner {
        taxFeeBps = _newFeeBps;
    }

    function setBlacklist(address user, bool isBlacklisted) external onlyOwner {
        blacklist[user] = isBlacklisted;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require(!blacklist[from] && !blacklist[to], "blacklisted");
        uint256 tax = (amount * taxFeeBps) / 10_000;
        uint256 burn = (amount * burnFeeBps) / 10_000;
        uint256 sendAmount = amount - tax - burn;
        balanceOf[from] -= amount;
        balanceOf[to] += sendAmount;
    }
}
