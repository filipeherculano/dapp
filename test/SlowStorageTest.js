const Web3 = require("web3");
const fs = require("fs");

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));
const abi = JSON.parse(fs.readFileSync("build/abi/SlowStorage.abi").toString());
const SlowStorage = new web3.eth.Contract(abi);

var stored_idx = []

function sleep(delay) {
	var timestamp = Date.now();
	while(Date.now() - timestamp <= delay); 
}

function getRandom(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}

function img_to_byte() {
	var len = getRandom(2500, 5000); // Images from 2.5Kb to 5Kb
	var bytes = new Array(len);
	for(var i = 0; i < len; i++) {
		var value = getRandom(0,256).toString(16);
		var byte = (value.length == 1 ? "0x0":"0x") + value;
		bytes[i] = byte;
	}
	return Buffer.from(bytes);
}

async function process(response) {
	var idx = getRandom(0, 1000);
	var data = img_to_byte();
	const gasEstimate = await SlowStorage.methods.storeData(data).estimateGas({from: response[idx]}).catch(err => {
		throw new Error(err);
	});
	const fee = getRandom(0, 118180); // 0.0013 ETH on avarage fee 
	var before_call = Date.now();
	SlowStorage.methods.storeData(data).send({from : response[idx], gas: (gasEstimate + fee)}).once('receipt', function(receipt){
		stored_idx.push(idx);
		fs.appendFileSync("SlowStorage_buffer.txt", data.length + " " + before_call + " " + receipt.transactionHash + "\n", (err) => {
			if(err) console.log(err);
		});

		before_call = Date.now();
		SlowStorage.methods.retrieveDataArray().call({from: response[idx]}).then(function(result){
			fs.appendFileSync("SlowStorage_buffer.txt", data.length + " " + before_call + " " + (Date.now() - before_call) / 1000.0 + "\n", (err) => {
				if(err) console.log(err);
			});
		}).catch(err => {
			throw new Error(err);
		});

	}).catch(err => {
		throw new Error(err);
	});
}

web3.eth.getAccounts().then(response => {
	SlowStorage.deploy({
		data: "0x608060405234801561001057600080fd5b50610477806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c80636705ce3e1461003b578063ac5c8535146100be575b600080fd5b610043610179565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610083578082015181840152602081019050610068565b50505050905090810190601f1680156100b05780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b610177600480360360208110156100d457600080fd5b81019080803590602001906401000000008111156100f157600080fd5b82018360208201111561010357600080fd5b8035906020019184600183028401116401000000008311171561012557600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050919291929050505061031f565b005b6060806040518060400160405280600181526020016000815250905060008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054905011156103185760008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054905090506000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600182038154811061027157fe5b906000526020600020018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561030f5780601f106102e45761010080835404028352916020019161030f565b820191906000526020600020905b8154815290600101906020018083116102f257829003601f168201915b50505050509150505b8091505090565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081908060018154018082558091505090600182039060005260206000200160009091929091909150908051906020019061039892919061039d565b505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103de57805160ff191683800117855561040c565b8280016001018555821561040c579182015b8281111561040b5782518255916020019190600101906103f0565b5b509050610419919061041d565b5090565b61043f91905b8082111561043b576000816000905550600101610423565b5090565b9056fea265627a7a72315820f72b7ce10603aacbc68cbec61492a2c5da99d1972e7129c6b987781318d1d4e464736f6c634300050b0032"
	}).send({
		from: response[0],
		gas: 357801
	}).then((newContractInstance) => {
		SlowStorage.options.address = newContractInstance.options.address
		var TEST_TIME = 1, TRANS_PER_SEC = 5;
		var loop = TEST_TIME * TRANS_PER_SEC, hash;
		for(var i = 0; i < loop; i++){
			sleep(40); // Sleep for 40 miliseconds
			process(response);
		}
	}).catch(err => {
		throw new Error(err);
	});
});
