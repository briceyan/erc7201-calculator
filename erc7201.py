from Crypto.Hash import keccak


def keccak256(data: bytes) -> bytes:
    return keccak.new(digest_bits=256, data=data).digest()


def erc7201(namespace: str) -> str:
    inner = int.from_bytes(keccak256(namespace.encode()), "big") - 1
    outer = int.from_bytes(keccak256(inner.to_bytes(32, "big")), "big")
    return f"0x{(outer & ~0xff):064x}"


def format_solidity(namespace: str, slot: str) -> str:
    parts = namespace.replace("-", "_").split(".")
    name = parts[-1]
    struct_name = name + "Storage"
    const_name = name.upper() + "_STORAGE_LOCATION"
    return f"""/// @custom:storage-location erc7201:{namespace}
struct {struct_name} {{}}

// keccak256(abi.encode(uint256(keccak256("{namespace}")) - 1)) & ~bytes32(uint256(0xff))
bytes32 private constant {const_name} = {slot};

"""
