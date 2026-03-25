"""Skill Evolution shared library — auto-loads .env on import."""

import os
from pathlib import Path

# Root of the skill-dev directory (scripts/../)
SKILL_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_dotenv():
    """Load .env from trusted paths only: SKILL_ROOT and current working directory.

    SECURITY: Only loads from predefined paths to prevent path traversal attacks.
    Does NOT walk up the directory tree from cwd.
    """
    # Trusted paths: skill root directory and current working directory
    trusted_paths = [SKILL_ROOT, Path.cwd()]

    for base_path in trusted_paths:
        env_file = base_path / ".env"
        if env_file.is_file() and env_file.exists():
            try:
                # Verify the file is within the trusted path (defense in depth)
                env_file_resolved = env_file.resolve()
                base_path_resolved = base_path.resolve()
                if not env_file_resolved.is_relative_to(base_path_resolved):
                    continue

                for line in env_file.read_text().splitlines():
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    # Don't overwrite existing env vars (explicit env takes priority)
                    if key and key not in os.environ:
                        os.environ[key] = value
            except OSError:
                pass
            return


def get_publisher_key():
    """Read publisher key from env var or skill-local .publisher_key file.

    Returns the key string, or empty string if not found.
    """
    key = os.environ.get("PUBLISHER_KEY", "").strip()
    if key:
        return key

    key_file = SKILL_ROOT / ".publisher_key"
    if key_file.exists():
        key = key_file.read_text().strip()
        if key:
            os.environ["PUBLISHER_KEY"] = key
            return key

    return ""


def save_publisher_key(key):
    """Save publisher key to skill-local .publisher_key file."""
    key_file = SKILL_ROOT / ".publisher_key"
    try:
        key_file.write_text(key + "\n")
    except OSError as e:
        print(
            f"WARNING: could not save key to {key_file}: {e}",
            file=__import__("sys").stderr,
        )
    os.environ["PUBLISHER_KEY"] = key


_load_dotenv()
