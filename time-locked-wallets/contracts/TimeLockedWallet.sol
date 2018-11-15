pragma solidity ^0.4.18;

import "./ERC20.sol";

contract TimeLockedWallet {

    address public creator;
    address public owner;
    address public advisor;
    address public crowd;
    uint256 public unlockDate;
    uint256 public createdAt;

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    modifier onlyAdvisor {
        require(msg.sender == advisor);
        _;
    }
    modifier onlyCrowd {
        require(msg.sender == crowd);
        _;
    }

    function TimeLockedWallet(
        address _creator,
        address _owner,
        address _advisor,
        address _crowd,
        uint256 _unlockDate,
        uint256 _unlockDate_advisor,
        uint256 _unlockDate_crowd
    ) public {
        creator = _creator;
        owner = _owner;
        advisor = _advisor;
        crowd = _crowd;
        unlockDate = _unlockDate;
        unlockDate_advisor = _unlockDate_advisor;
        unlockDate_crowd = _unlockDate_crowd;
        createdAt = now;
    }

    // keep all the ether sent to this address
    function() payable public { 
        Received(msg.sender, msg.value);
    }

    // callable by owner only, after specified time
    function withdraw() onlyOwner public {
       require(now >= unlockDate);
       //now send all the balance
       msg.sender.transfer(this.balance);
       Withdrew(msg.sender, this.balance);
    }

    function withdraw() onlyAdvisor public {
       require(now >= unlockDate_advisor);
       //now send all the balance
       msg.sender.transfer(this.balance);
       Withdrew(msg.sender, this.balance);
    }

    function withdraw() onlyCrowd public {
       require(now >= unlockDate_crowd);
       //now send all the balance
       msg.sender.transfer(this.balance);
       Withdrew(msg.sender, this.balance);
    }

    // callable by owner only, after specified time, only for Tokens implementing ERC20
    function withdrawTokens(address _tokenContract) onlyOwner public {
       require(now >= unlockDate);
       ERC20 token = ERC20(_tokenContract);
       //now send all the token balance
       uint256 tokenBalance = token.balanceOf(this);
       token.transfer(owner, tokenBalance);
       WithdrewTokens(_tokenContract, msg.sender, tokenBalance);
    }

    function withdrawTokens(address _tokenContract) onlyAdvisor public {
       require(now >= unlockDate);
       ERC20 token = ERC20(_tokenContract);
       //now send all the token balance
       uint256 tokenBalance = token.balanceOf(this);
       token.transfer(owner, tokenBalance);
       WithdrewTokens(_tokenContract, msg.sender, tokenBalance);
    }
    function withdrawTokens(address _tokenContract) onlyCrowd public {
       require(now >= unlockDate_crowd);
       ERC20 token = ERC20(_tokenContract);
       //now send all the token balance
       uint256 tokenBalance = token.balanceOf(this);
       token.transfer(owner, tokenBalance);
       WithdrewTokens(_tokenContract, msg.sender, tokenBalance);
    }

    function info() public view returns(address, address, uint256, uint256, uint256) {
        return (creator, owner, unlockDate, createdAt, this.balance);
    }

    event Received(address from, uint256 amount);
    event Withdrew(address to, uint256 amount);
    event WithdrewTokens(address tokenContract, address to, uint256 amount);
}
