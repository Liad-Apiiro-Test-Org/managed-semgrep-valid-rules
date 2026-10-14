import Crypto.Hash.MD4


def legacy_digest(data):
    return Crypto.Hash.MD4.new(data).hexdigest()
