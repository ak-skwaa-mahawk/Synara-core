
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Gwich’in Tribal Coin — For the People, For the Earth
contract TribalCoinGTC {
    string public name = "Gwich’in Tribal Coin";
    string public symbol = "GTC";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public creator;

    mapping(address => uint256) public balanceOf;
    mapping(address => bool) public verifiedTribal;
    mapping(address => bool) public blessings;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event BlessingSent(address from, address to, string message);

    modifier onlyCreator() {
        require(msg.sender == creator, "Not authorized.");
        _;
    }

    modifier onlyVerified() {
        require(verifiedTribal[msg.sender], "Not a verified community member.");
        _;
    }

    constructor(uint256 initialSupply) {
        creator = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balanceOf[creator] = totalSupply;
    }

    function verifyTribalWallet(address user) public onlyCreator {
        verifiedTribal[user] = true;
    }

    function transfer(address to, uint256 value) public returns (bool success) {
        require(balanceOf[msg.sender] >= value, "Not enough balance.");
        require(balanceOf[to] + value <= totalSupply / 50, "No wallet can own more than 2%.");
        require(value <= 1000 * (10 ** uint256(decimals)), "Transfer too large — coin is for the people.");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function sendBlessing(address to, string memory message) public returns (bool) {
        blessings[to] = true;
        emit BlessingSent(msg.sender, to, message);
        return true;
    }

    function reclaimDormantCoins(address user) public onlyCreator {
        // In final version, would check timestamp to verify 1 year inactivity
        uint256 reclaimed = balanceOf[user];
        balanceOf[user] = 0;
        balanceOf[creator] += reclaimed;
    }
}
