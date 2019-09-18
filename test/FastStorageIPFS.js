const Web3 = require("web3");
const fs = require("fs");
const IPFS = require("ipfs");

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));
const abi = JSON.parse(fs.readFileSync("build/abi/FastStorageIPFS.abi").toString());
const FastStorage = new web3.eth.Contract(abi);

var ipfs = new IPFS().on('error', err => console.log(err));

function sleep(delay) {
	var timestamp = Date.now();
	while(Date.now() - timestamp <= delay); 
}

function getRandom(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}

async function img_to_byte() {
	var len = getRandom(2500, 5000); // Images from 2.5Kb to 5Kb
	var bytes = new Array(len);
	for(var i = 0; i < len; i++) {
		var value = getRandom(0,256).toString(16);
		var byte = (value.length == 1 ? "0x0":"0x") + value;
		bytes[i] = byte;
	}
	return bytes;
}

async function process(response) {
	await ipfs.ready;
	var idx = getRandom(0, 1000);
	var data = Array(img_to_byte());
	const fee = getRandom(0, 118180); // 0.0013 ETH on avarage fee 

	var before_call = Date.now();
	ipfs.add(Buffer.from(data), function(err, res){
		if(err) throw new Error(err);
		const hash = res[0].hash;
		FastStorage.methods.storeData(hash).send({from : response[idx], gas: (106555 + fee)}).once('receipt', function(receipt){
			const str = hash.length + " " + before_call + " " + receipt.transactionHash + "\n";
			fs.appendFileSync("FastStorageIPFS_buffer.txt", str, (err) => { throw new Error(err); });

			before_call = Date.now();
			FastStorage.methods.retrieveData().call({from: response[idx]}).then(function(result){
				ipfs.get(hash, function(err, res) {
					if(err) throw new Error(err);
					const str = hash.length + " " + before_call + " " + (Date.now() - before_call)/1000.0 + "\n";
					fs.appendFileSync("FastStorageIPFS_buffer.txt", str, (err) => { throw new Error(err); });
				});
			}).catch(err => { throw new Error(err); });
		}).catch(err => { throw new Error(err); });
	});
}

web3.eth.getAccounts().then(response => {
	FastStorage.deploy({
		data: "0x608060405234801561001057600080fd5b50610470806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806351e0556d1461003b578063fb218f5f146100be575b600080fd5b610043610179565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610083578082015181840152602081019050610068565b50505050905090810190601f1680156100b05780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b610177600480360360208110156100d457600080fd5b81019080803590602001906401000000008111156100f157600080fd5b82018360208201111561010357600080fd5b8035906020019184600183028401116401000000008311171561012557600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610318565b005b60608060405180602001604052806000815250905060008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054905011156103115760008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054905090506000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600182038154811061026a57fe5b906000526020600020018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103085780601f106102dd57610100808354040283529160200191610308565b820191906000526020600020905b8154815290600101906020018083116102eb57829003601f168201915b50505050509150505b8091505090565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819080600181540180825580915050906001820390600052602060002001600090919290919091509080519060200190610391929190610396565b505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103d757805160ff1916838001178555610405565b82800160010185558215610405579182015b828111156104045782518255916020019190600101906103e9565b5b5090506104129190610416565b5090565b61043891905b8082111561043457600081600090555060010161041c565b5090565b9056fea265627a7a7231582047425bd005a1a551104ae9638a9aafa3d4a7609f18fceff29ae94f2fec490eb664736f6c634300050b0032"
	}).send({
		from: response[0],
		gas: 355925
	}).then((newContractInstance) => {
		FastStorage.options.address = newContractInstance.options.address
		var TEST_TIME = 10, TRANS_PER_SEC = 25;
		var loop = TEST_TIME * TRANS_PER_SEC, hash;
		for(var i = 0; i < loop; i++){
			sleep(40); // Sleep for 40 miliseconds
			process(response);
		}
	}).catch(err => { throw new Error(err); });
});
