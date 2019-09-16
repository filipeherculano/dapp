const Web3 = require("web3");
const fs = require("fs");

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));
const abi = JSON.parse(fs.readFileSync("build/abi/SlowStorage.abi").toString());
const SlowStorage = new web3.eth.Contract(abi);

function sleep(delay) {
	var timestamp = Date.now();
	while(Date.now() - timestamp <= delay); 
}

function getRandom(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}

function img_to_byte() {
	var len = getRandom(1000, 5000); // Images from 1Kb to 5Kb
	var bytes = new Array(len);
	for(var i = 0; i < len; i++) {
		var value = getRandom(0,256).toString(16);
		var byte = (value.length == 1 ? "0x0":"0x") + value;
		bytes[i] = byte;
	}
	return Buffer.from(bytes);
}

async function store(response) {
	var idx = getRandom(0, 1000);
	var data = img_to_byte();
	const gasEstimate = await SlowStorage.methods.storeData(data).estimateGas({from: response[idx]}).catch(function(error){
		throw error;
	});
	const fee = getRandom(0, 118180); // 0.0013 ETH on fee avarage
	var before_call = Date.now();
	await SlowStorage.methods.storeData(data).send({from : response[idx], gas: (gasEstimate + fee)}).on('transactionHash', function(value){
		fs.appendFileSync("buffer.txt", data.length + " " + before_call + " " + value + "\n", (err) => {
			if(err) console.log(err);
		});
	}).catch(function(error){
		throw error;
	});
}

async function retrieve(response) {
	var before_call = Date.now();
	SlowStorage.methods.retrieveDataArray(0).call({from: response[idx]}, function(error, result){
		fs.appendFileSync("buffer.txt", before_call + " " + (Date.now() - item) + "\n", (err) => {
			if(err) console.log(err);
		});
	});
}

web3.eth.getAccounts().then(response => {
	SlowStorage.deploy({
		data: "0x608060405234801561001057600080fd5b5061045c806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80631622bc1114610046578063ac5c8535146100ed578063bc9083aa146101a8575b600080fd5b6100726004803603602081101561005c57600080fd5b81019080803590602001909291905050506101c6565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100b2578082015181840152602081019050610097565b50505050905090810190601f1680156100df5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6101a66004803603602081101561010357600080fd5b810190808035906020019064010000000081111561012057600080fd5b82018360208201111561013257600080fd5b8035906020019184600183028401116401000000008311171561015457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506102bb565b005b6101b0610339565b6040518082815260200191505060405180910390f35b60606000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020828154811061021157fe5b906000526020600020018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102af5780601f10610284576101008083540402835291602001916102af565b820191906000526020600020905b81548152906001019060200180831161029257829003601f168201915b50505050509050919050565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819080600181540180825580915050906001820390600052602060002001600090919290919091509080519060200190610334929190610382565b505050565b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002080549050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103c357805160ff19168380011785556103f1565b828001600101855582156103f1579182015b828111156103f05782518255916020019190600101906103d5565b5b5090506103fe9190610402565b5090565b61042491905b80821115610420576000816000905550600101610408565b5090565b9056fea265627a7a72315820c06e0a95947fd176df28b92641d313a3026a48f74fc3c1670f37cdf9949bef4d64736f6c634300050b0032"
	}).send({
		from: response[0],
		gas: 350815
	}).then((newContractInstance) => {
		SlowStorage.options.address = newContractInstance.options.address
		var TEST_TIME = 5, TRANS_PER_SEC = 25;
		var loop = TEST_TIME * TRANS_PER_SEC, hash;
		var before_call = new Array(), data_imgs = new Array(), data_imgs_cpy = new Array(); 
		for(var i = 0; i < loop; i++){
			sleep(40); // Sleep for 40 miliseconds
			if(getRandom(0,2) == 1) store(response);
			else retrieve(response);
		}
	});
});
