"""Validate the M0 documentation package; this does not test an Android HAL."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DIRECTORIES = (
    "docs", "manager-app", "vfeed-service", "camera-provider", "common",
    "aosp/patches", "aosp/vintf", "aosp/init", "aosp/sepolicy", "aosp/product",
    "tests/camera2-test", "tests/provider-tests", "tests/media-tests",
    "tools/diagnostics", "tools/frame-generator", "reference",
)
DOCUMENTS = (
    "README.md", "PROJECT_STATUS.md", "DEVICE_PROFILE.md", "ROADMAP.md",
    "docs/ARCHITECTURE.md", "docs/AOSP_RESEARCH.md", "docs/BUILD_AND_TEST.md",
    "docs/RECOVERY.md", "docs/COMMAND_LOG.md",
)


def main():
    errors = []
    for directory in DIRECTORIES:
        if not (ROOT / directory).is_dir():
            errors.append(f"Missing directory: {directory}")
    for document in DOCUMENTS:
        path = ROOT / document
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty document: {document}")
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            candidate = (path.parent / target.split("#", 1)[0]).resolve()
            if not candidate.is_relative_to(ROOT) or not candidate.exists():
                errors.append(f"Broken/outside local link in {path.relative_to(ROOT)}: {target}")
    if errors:
        print("M0 bootstrap validation FAILED")
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(DIRECTORIES)} required directories, {len(DOCUMENTS)} documents and local Markdown links")
    print("Scope: M0 documentation only; Android build and camera acceptance remain unverified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
