#!/usr/bin/env python3
from list import segids
import json
import kmdrpc

CHAIN = input('Please specify chain:')
AMOUNT = input("Please specify the amount to send to each address:")

# iterate addresses list, construct dictionary,
# with amount as value for each address
addresses_dict = {}
for e in segids:
    address = e[-1]
    addresses_dict[address] = AMOUNT

# make rpc call, issue transaction
sendmany_result = kmdrpc.sendmany_rpc(CHAIN, addresses_dict)
print("Success! txid:" + sendmany_result['result'])
