"""news-image-20261124 entry runner.

Copies the bundled broadsheet front page (``entry.png``, 1024x1024,
titled THE WORLD, summarising the world's news on Tuesday
24 November 2026) to ``$MAKEFUN_OUTPUT_DIR/entry.png``.

Standard library only, no network access, fully deterministic:
repeated runs write byte-identical output. After copying, the
SHA-256 digest of the output is checked against the bundled image
so a truncated or corrupted copy fails loudly instead of silently
producing a wrong entry.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.png"
# SHA-256 of the bundled entry.png (1024x1024 front page). The copy is
# verified against this digest so any corruption is caught at run time.
EXPECTED_SHA256 = "93d9d1f4ab748db50c78f1c6b236e4ea4b67e94536b17f593bd85483f4c6f6d6"


def bundled_image_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def output_dir():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if chosen:
        return chosen
    return DEFAULT_OUTPUT_DIR


def output_path():
    return os.path.join(output_dir(), OUTPUT_NAME)


def copy_bundled_image(source, destination):
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, destination)
    return destination


def check_copy(source, destination):
    source_size = os.path.getsize(source)
    destination_size = os.path.getsize(destination)
    if source_size != destination_size:
        raise SystemExit(
            "copy mismatch: source is %d bytes but output is %d bytes"
            % (source_size, destination_size)
        )
    return source_size


def digest_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_integrity(source, destination):
    source_digest = digest_file(source)
    destination_digest = digest_file(destination)
    if source_digest != EXPECTED_SHA256:
        raise SystemExit(
            "bundled image digest mismatch: expected %s, got %s"
            % (EXPECTED_SHA256, source_digest)
        )
    if destination_digest != source_digest:
        raise SystemExit(
            "output digest mismatch: expected %s, got %s"
            % (source_digest, destination_digest)
        )
    return destination_digest


def describe(source, destination, size):
    print("source: %s" % source)
    print("output: %s" % destination)
    print("bytes: %d" % size)
    print("done: %s copied deterministically" % OUTPUT_NAME)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        print("usage: python3 main.py", file=sys.stderr)
        print("reads MAKEFUN_OUTPUT_DIR (default /output)", file=sys.stderr)
        return 2
    source = bundled_image_path()
    if not os.path.isfile(source):
        raise SystemExit("missing bundled image: %s" % source)
    destination = output_path()
    copy_bundled_image(source, destination)
    size = check_copy(source, destination)
    digest = verify_integrity(source, destination)
    print("sha256: %s" % digest)
    describe(source, destination, size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
