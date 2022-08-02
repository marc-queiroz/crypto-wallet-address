from Crypto.Hash import keccak
import codecs

# convert base64 to hex
# base64 = BCT4ALtlDp9SkeQaN9SsLm2rcnhC8IAAwFqHbOYiR2U2vRusCalc2WTyvYjfzcVEv6zWXV+4WDXqgcwSCjVrUNo=
# converted to hex = 0424f800bb650e9f5291e41a37d4ac2e6dab727842f08000c05a876ce622476536bd1bac09a95cd964f2bd88dfcdc544bfacd65d5fb85835ea81cc120a356b50da

# public_key_bytes = codecs.decode('0424f800bb650e9f5291e41a37d4ac2e6dab727842f08000c05a876ce622476536bd1bac09a95cd964f2bd88dfcdc544bfacd65d5fb85835ea81cc120a356b50da', 'hex')


public_key_bytes = codecs.decode('0287ac846aef38622d48f979c0a5234ebc73d31f7b9287e92856664d69ccb12752', 'hex')

keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_bytes)
keccak_digest = keccak_hash.hexdigest()
# The last 20 bytes of the string is the address
wallet_len = 40
wallet = '0x' + keccak_digest[-wallet_len:]
print('Wallet Address: ' + wallet)
# '0xadafa47536826711c7a58cac8eb7b3f814123ad2'
