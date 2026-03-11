import json
import hashlib
import sys


def compute_hash(data):
    """
    Compute SHA256 hash of the JSON bundle excluding the hash field.
    """
    canonical = json.dumps(data, sort_keys=True).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def validate_rpo(path):
    with open(path, "r") as f:
        bundle = json.load(f)

    if "hash" not in bundle:
        print("❌ No hash field found in bundle.")
        return

    provided_hash = bundle["hash"]

    # remove hash field before recomputing
    bundle_copy = dict(bundle)
    del bundle_copy["hash"]

    calculated_hash = compute_hash(bundle_copy)

    if provided_hash == calculated_hash:
        print("✅ RPO integrity verified.")
    else:
        print("❌ Hash mismatch.")
        print("Expected:", provided_hash)
        print("Computed:", calculated_hash)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validator.py example-bundle.json")
        sys.exit(1)

    validate_rpo(sys.argv[1])
