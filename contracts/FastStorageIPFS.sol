pragma solidity 0.5.11;

contract FastStorage {
	mapping (address => string[]) dataBase;
	
	function storeData(string memory ipfsHash) public {
		dataBase[msg.sender].push(ipfsHash);
	}

	function retrieveDataArray(uint256 index) public view returns (string memory){
		return dataBase[msg.sender][index];
	}
}
