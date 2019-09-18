pragma solidity 0.5.11;

contract FastStorage {
	mapping (address => string[]) dataBase;
	
	function storeData(string memory ipfsHash) public {
		dataBase[msg.sender].push(ipfsHash);
	}

	function retrieveData() public view returns (string memory){
		string memory ret = "";
		if(dataBase[msg.sender].length > 0) {
			uint256 len = dataBase[msg.sender].length;
			ret = dataBase[msg.sender][len-1];
		}
		return ret;
	}
}
