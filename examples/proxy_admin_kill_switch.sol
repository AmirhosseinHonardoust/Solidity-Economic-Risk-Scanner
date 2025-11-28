// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ProxyAdminKillSwitch {
    address public admin;
    address public implementation;

    constructor(address impl) {
        admin = msg.sender;
        implementation = impl;
    }

    function upgrade(address newImpl) external {
        require(msg.sender == admin, "not admin");
        implementation = newImpl;
    }

    //  Kill switch, can freeze all calls
    function pause() external {
        require(msg.sender == admin, "not admin");
        implementation = address(0);
    }
}
