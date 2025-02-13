# neurokit/utils/checksum.py
import hashlib
import os

def verify_checksum(file_path: str, expected_checksum: str = "") -> bool:
    """
    Verifies the checksum of the given file. If expected_checksum is provided,
    compares the computed checksum with it.
    """
    if not os.path.exists(file_path):
        return False
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
    except Exception:
        return False
    computed_checksum = sha256.hexdigest()
    if expected_checksum:
        return computed_checksum == expected_checksum
    return True
