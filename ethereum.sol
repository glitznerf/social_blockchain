pragma solidity >=0.6.0;

// Assumptions:
//      - people can be entitled to funding of multiple groups


contract Government {
    
    address public gov;
    
    address[] public elderly;
    string c1 = "elderly";
    
    mapping(address => uint) entitlement;
    
    string public group;
    
    
    constructor() public { 
        gov = msg.sender;
    }


    function register(string memory group_) public returns(bool) {
        group = group_;
        
        // If elderly
        if (keccak256(abi.encodePacked((group))) == keccak256(abi.encodePacked((c1)))) {
            // If already registered, stop
            for(uint a = 0; a < elderly.length; a = a + 1 ){
                if (msg.sender == elderly[a]){
                    return false;
                }
            }
            // Else register
            elderly.push(msg.sender);
            return true;
        }
        return false;
    }
    
    
    function distributeFunds(string memory group_) public payable {
    //TODO: Only gov should be able to
        group = group_; 
        uint amount = msg.value;
        
        // If elderly
        if (keccak256(abi.encodePacked((group))) == keccak256(abi.encodePacked((c1)))) {
            uint individual_amount = amount / elderly.length;
            for(uint a = 0; a < elderly.length; a = a + 1 ){
                entitlement[elderly[a]] += individual_amount;
            }
        }
    }
    
    
   function claimFunds() public returns(uint) {
        // Look up entitlement
        uint amount = entitlement[msg.sender];
        msg.sender.transfer(amount);
   }
    
}
