// Giricoins ICO

// Version of compiler
pragma solidity ^0.4.11;

contract giricoin_ico {
    // Introducing the maximum number of Giricoins available for sale
    uint public max_giricoins = 1000000;

    // Introducing the USD to Giricoins conversion rate
    uint public usd_to_giricoins = 1000;

    // Introducing the total number of Giricoins that have been bought by the investors
    uint public total_giricois_bought = 0;

    // Mapping from the invstor address to its equity in Giricoins and USD
    mapping(address => uint) equity_giricoins;
    mapping(address => uint) equity_usd;

    // Checking if an investor can buy Giricoins
    modifier can_buy_giricoins(uint usd_invested) {
        require (usd_invested * usd_to_giricoins + total_giricois_bought <= max_giricoins);
        _;
    }

    // Getting the equity in Giricoins of an investor
    function equity_in_giricoins(address investor) external constant {
        equity_giricoins[investor];
    }

    // Getting the quity in USD of an investor
    function equity_in_usd(address investor) external constant {
        equity_usd[investor];
    }

    // Buying Giricoins
    function buy_giricoins(address investor, uint usd_invested) external
    can_buy_giricoins(usd_invested) {
        uint giricoins_bought = usd_invested * usd_to_giricoins;
        equity_giricoins[investor] += giricoins_bought;
        equity_usd[investor] = equity_giricoins[investor] / 1000;
        total_giricois_bought += giricoins_bought;
    }

    // Selling Giricoins
    function sell_giricoins(address investor, uint giricoin_sold) external {
        equity_giricoins[investor] -= giricoin_sold;
        equity_usd[investor] = equity_giricoins[investor] / 1000;
        total_giricois_bought -= giricoin_sold;
    }

}