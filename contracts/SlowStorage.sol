pragma solidity 0.5.11;

contract SlowStorage {
	mapping (address => bytes[]) dataBase;
	
	function storeData(bytes memory rawData) public {
		dataBase[msg.sender].push(rawData);
	}

	function retrieveDataArray() public view returns (bytes memory) {
		bytes memory ret = "\x00";
		if(dataBase[msg.sender].length > 0) {
			uint256 len = dataBase[msg.sender].length;
			ret = dataBase[msg.sender][len-1];
		}
		return ret;
	}
}
