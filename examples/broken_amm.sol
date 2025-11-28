// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BrokenAMM {
    uint256 public reserve0;
    uint256 public reserve1;

    constructor(uint256 r0, uint256 r1) {
        reserve0 = r0;
        reserve1 = r1;
    }

    //  No invariant check x * y = k
    function swap0for1(uint256 amountIn) external {
        reserve0 += amountIn;
        uint256 amountOut = amountIn / 2; // nonsense
        reserve1 -= amountOut;
    }
}
