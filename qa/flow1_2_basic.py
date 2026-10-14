# QA LIM-43609 Flow 1.2 marker: BASIC tier target
import Crypto.Hash.MD4


def basic_tier_digest(payload):
    return Crypto.Hash.MD4.new(payload).hexdigest()
