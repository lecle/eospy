import eospy.cleos
import eospy.keys
from eospy.types import Abi, Action
from eospy.utils import parse_key_file
import os
import pytz
import json
from os import path

ce = eospy.cleos.Cleos(url='https://jungle3.cryptolions.io:443')
current_dir_path = path.abspath(path.dirname(__file__))
abi_file = path.join(current_dir_path, 'eosio.token.abi')
#tx_result = ce.set_abi('fqrmqfwxdsge', 'active', abi_file, '5K4VnEqfF6KkhQUyzNSHC3KQ39tMrYUPj65zpPo5HrqSft9qVHU')
# got transaction_id: c6fcc585cbadcc1fbfa4fd45da961b804cb8748c8ba1acf31d2e76dcae3bf6c2
#print(tx_result['transaction_id'])

code_file = path.join(current_dir_path, 'eosio.token.wasm')
#tx_result = ce.set_code('fqrmqfwxdsge', 'active', code_file, '5K4VnEqfF6KkhQUyzNSHC3KQ39tMrYUPj65zpPo5HrqSft9qVHU')
# got transaction_id: dcb8b2289c61e749c8965da4981b87b07a950539426a623f06e75c6bbb69406b
#print(tx_result['transaction_id'])
