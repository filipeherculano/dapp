const fs = require("fs");
const Web3 = require("web3");
const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));

async function log_retrieve(size, timestamp) {
	var str = size + " " + timestamp;
	fs.appendFileSync("build/plot_data/slow_storage_tx_time_retrieve.txt", str + "\n", (err) => {
		if(err) console.log(err);
	});
}

async function log_store(size, timestamp, tx) {
	var block_hash = await web3.eth.getTransaction(tx);
	var block_timestamp = await web3.eth.getBlock(block_hash.blockHash);

	var str = timestamp + " " + (parseInt(block_timestamp.timestamp, 10)*1000 - timestamp);
	fs.appendFileSync("build/plot_data/slow_storage_tx_time_store.txt", str + "\n", (err) => {
		if(err) console.log(err);
	});
}

fs.readFile("buffer.txt", (err, data) => {
	if(err) throw err;
	var lines = data.toString().split("\n");
	for(var line of lines) {
		if(line.length == 0) break;
		var words = line.toString().split(" ");
		if(words[2].length < 12) log_retrieve(words[1], words[2]); // If not a transaction hash
		else log_store(words[0], words[1], words[2]);
	}
});
