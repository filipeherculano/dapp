pragma solidity 0.5.11;

contract SlowStorage {
	mapping (address => bytes[]) dataBase;
	
	function storeData(bytes memory rawData) public {
		dataBase[msg.sender].push(rawData);
	}

	function retrieveDataArray(uint256 index) public view returns (bytes memory) {
		return dataBase[msg.sender][index];
	}

	function dataArraySize() public view returns (uint) {
		return dataBase[msg.sender].length;
	}
}
