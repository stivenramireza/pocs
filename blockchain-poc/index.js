// const Blockchain = require('./src/not_mine/blockchain');
// const Block = require('./src/not_mine/block');

const Blockchain = require('./src/mine/blockchain');
const Block = require('./src/mine/block');


const run_without_mine = async() => {
    const blockchain = await new Blockchain();

    const block1 = new Block({data: 'Block #1'});
    await blockchain.addBlock(block1);

    const block2 = new Block({data: 'Block #2'});
    await blockchain.addBlock(block2);

    const block3 = new Block({data: 'Block #3'});
    await blockchain.addBlock(block3);

    blockchain.print();
}

const run_with_mine = () => {
    const blockchain = new Blockchain();

    for (let i = 0; i < 10; i++) {
        const block = blockchain.addBlock(`Block #${i}`);
        console.log(block.toString());
    }

}

const run = async() => {
    // Run blockchain without mine
    // await run_without_mine();

    // Run blockchain with mine
    run_with_mine();
}

run();
