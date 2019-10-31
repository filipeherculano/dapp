const fs = require("fs");
const Web3 = require("web3");
const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));

async function log_retrieve(size, timestamp, elapsed, test) {
	var str = size + " " + timestamp + " " + elapsed + " -1\n";
	fs.appendFileSync("build/plot_data/" + test + "_retrieve.txt", str, (err) => {
		if(err) console.log(err);
	});
}

async function log_store(size, timestamp, tx, spent, store_time, test) {
	var trans = await web3.eth.getTransaction(tx);
	var block = await web3.eth.getBlock(trans.blockHash);

	var str = size + " " + timestamp + " " + (parseInt(block.timestamp, 10)*1000 - timestamp)/1000.0 + " " + block.number + " " + spent + " " + store_time +"\n";
	fs.appendFileSync("build/plot_data/" + test + "_store.txt", str, (err) => {
		if(err) console.log(err);
	});
}

// Increment this array when adding new tests
tests = ["SlowStorage", "FastStorageIPFS", "FastStorageSWARM", "FastStorageSIA"];

for (var test of tests) {
	var path = test + "_buffer.txt";

	if(fs.existsSync(path)) {
		fs.unlink("build/plot_data/" + test + "_store.txt", (err) => {});
		fs.unlink("build/plot_data/" + test + "_retrieve.txt", (err) => {});

		data = fs.readFileSync(path);
		var lines = data.toString().split("\n");
		for(var line of lines) {
			if(line.length == 0) break;
			var words = line.toString().split(" ");
			if(words[2].length < 12) log_retrieve(words[0], words[1], words[2], test); // If not a transaction hash
			else log_store(words[0], words[1], words[2], words[3], words[4], test);
		}
	}
}
