const fs = require("fs");
const Web3 = require("web3");
const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));

async function log_retrieve(line) {
	fs.appendFileSync("build/plot_data/slow_storage_tx_time_retrieve.txt", line + "\n", (err) => {
		if(err) console.log(err);
	});
}

async function log_store(size, timestamp, tx) {
	web3.eth.getTransaction(tx).then(function(object){
		var block_hash = object.blockHash;
		web3.eth.getBlock(block_hash).then(function(object){
			var block_timestamp = object.timestamp * 1000;
			var str = timestamp + " " + (parseInt(block_timestamp, 10) - timestamp);
			fs.appendFileSync("build/plot_data/slow_storage_tx_time_store.txt", str + "\n", (err) => {
				if(err) console.log(err);
			});
		})
	}); 
}

fs.readFile("buffer.txt", (err, data) => {
	if(err) throw err;
	var lines = data.toString().split("\n");
	for(var line of lines) {
		if(line.length == 0) break;
		var words = line.toString().split(" ");
		if(words[1].length < 12) log_retrieve(line); // If not a transaction hash
		else log_store(words[0], words[1], words[2]);
	}
});
