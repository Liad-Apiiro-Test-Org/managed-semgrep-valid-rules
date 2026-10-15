# QA LIM-43609 NF5: triager outage during triage - recovery check
import Crypto.Hash.MD4


def outage_probe(payload):
    return Crypto.Hash.MD4.new(payload).hexdigest()
