# QA LIM-43609 Flow 1.3 / Rg2: no stored efforts anywhere -> nothing should triage
import Crypto.Hash.MD4


def outage_digest(payload):
    return Crypto.Hash.MD4.new(payload).hexdigest()
