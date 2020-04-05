# MechgCoin

MechgCoin is a cryptocurrency using Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MechgCoin.

```bash
pip install mechgcoin
```

## Usage

```python
from blockchain import BlockChain
from block import Block

blockchain.new_data(
    sender="0",  #it implies that this node has created a new block
    recipient="Joziel CDB",  #let's send Joziel some coins!
    quantity=
    1,  #creating a new block (or identifying the proof number) is awarded with 1
)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENCE.md)