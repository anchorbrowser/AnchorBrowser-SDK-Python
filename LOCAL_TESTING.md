# Building & testing the SDK locally

How to build, verify, and try the SDK on your machine before anything is
released to PyPI.

## One-time setup

```sh
./scripts/bootstrap        # installs Rye (if missing) and syncs .venv
```

## The full local quality gate

This is the same gate CI and the Release workflow run:

```sh
./scripts/lint             # ruff + pyright + mypy + import check
./scripts/generate --check # generated code matches spec/openapi.yaml + sdk-manifest.yaml
rye build --clean          # publishable sdist + wheel into dist/
./scripts/test             # unit + spec-coverage + wire-parity suites
```

What each safety net covers:

| Check                            | Fails when                                                                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `tests/spec_suite/test_wire_parity.py` | any SDK method sends a different HTTP request (method, path, query, headers, body) than `wire_parity_golden.json`, or sync/async diverge |
| `tests/spec_suite/test_spec_coverage.py` | spec, `spec/sdk-manifest.yaml`, and the generated client disagree (e.g. a new spec operation without a naming entry)  |
| `tests/spec_suite/test_v1_regression.py` | an operation the v0 (Stainless) SDK exposed disappears from the spec without a reviewed `v1_removed` entry            |
| `./scripts/generate --check`     | `src/anchorbrowser/types/` or `resources/` doesn't match `spec/`                                                              |

## Trying the SDK in another project

### Option A — local wheel (closest to a real pip install)

```sh
./scripts/pack-local
# ==> Local wheel ready: .../dist/anchorbrowser-<version>-py3-none-any.whl
```

Then in any test project:

```sh
python -m venv .venv && source .venv/bin/activate
pip install /path/to/AnchorBrowser-SDK-Python/dist/anchorbrowser-<version>-py3-none-any.whl
```

```python
from anchorbrowser import Anchorbrowser

client = Anchorbrowser()  # reads ANCHORBROWSER_API_KEY from the environment
session = client.sessions.create_session()
print(session.data.id)
```

This exercises the exact artifact `publish-pypi.yml` would upload.

### Option B — editable install (fast iteration)

```sh
# in your test project's virtualenv
pip install -e /path/to/AnchorBrowser-SDK-Python
```

Code changes apply immediately; run `./scripts/generate` after changing
`spec/`, and prefer Option A for release validation.

## Updating the wire golden intentionally

When you _intend_ to change wire behavior (e.g. adding an endpoint after a
spec sync):

```sh
./scripts/generate            # regenerate models + resources from spec/
./scripts/update-wire-golden  # refresh tests/spec_suite/wire_parity_golden.json
```

Both diffs are committed and reviewable — they are the record of the change.

## Release rehearsal

Everything the Release workflow does can be rehearsed locally without
publishing:

```sh
sed -i '' -E 's/^version = "[^"]*"/version = "9.9.9"/' pyproject.toml   # bump (revert afterwards)
./scripts/pack-local                                                    # build the exact artifact
git checkout pyproject.toml                                             # undo the rehearsal bump
```

The real release is cut from the Actions tab: **Release** workflow → enter
the version (PEP 440, e.g. `1.2.0` or `1.2.0rc1`). It runs the full gate
above, bumps/tags/creates the GitHub release, and dispatches
`publish-pypi.yml` (PyPI OIDC trusted publishing).
