"""Check skill metadata, portable references and release file boundaries.

Development dependency: PyYAML. Does not access the network or mutate files.
Run from any working directory: python path/to/tools/validate.py
"""
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit('Install the development dependency: python -m pip install PyYAML')

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills' / 'layout-logic'
errors = []

def release_file(path):
    """Git internals and Python caches are not part of the release."""
    return path.is_file() and not {'.git', '__pycache__'}.intersection(path.relative_to(ROOT).parts)

def check(condition, message):
    if not condition:
        errors.append(message)

def within(path, base):
    return path.resolve().is_relative_to(base.resolve())

text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
front = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
check(bool(front), 'SKILL.md must start with YAML frontmatter')
if front:
    meta = yaml.safe_load(front.group(1))
    check(isinstance(meta, dict), 'Frontmatter must be a mapping')
    if isinstance(meta, dict):
        check(meta.get('name') == SKILL.name, 'Skill name and folder differ')
        check(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(meta.get('name', '')))), 'Invalid skill name')
        check(len(str(meta.get('name', ''))) < 64, 'Skill name is too long')
        description = meta.get('description')
        check(isinstance(description, str) and 0 < len(description) <= 1024, 'Missing/invalid description')
        check(set(meta) <= {'name', 'description', 'license', 'allowed-tools', 'metadata'}, 'Unsupported frontmatter key')

ui = yaml.safe_load((SKILL / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
interface = ui.get('interface', {})
check(25 <= len(interface.get('short_description', '')) <= 64, 'UI description must be 25–64 characters')
check('$layout-logic' in interface.get('default_prompt', ''), 'Default prompt must name the skill')
check(ui.get('policy', {}).get('allow_implicit_invocation') is True, 'Automatic discovery unexpectedly disabled')

markdown = [path for path in ROOT.rglob('*.md') if release_file(path)]
links = 0
for path in markdown:
    body = path.read_text(encoding='utf-8')
    check(not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/[^\s/]+/', body), f'Nonportable local path: {path.relative_to(ROOT)}')
    check(not re.search(r'\[TODO:|\[INSERT HERE\]', body, re.I), f'Unfinished scaffold: {path.relative_to(ROOT)}')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
        target = target.strip().strip('<>')
        if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        resolved = path.parent / target
        links += 1
        check(within(resolved, ROOT), f'Link escapes repository: {target}')
        check(resolved.exists(), f'Broken reference in {path.relative_to(ROOT)}: {target}')
        if within(path, SKILL):
            check(within(resolved, SKILL), f'Skill depends on a file outside its install folder: {target}')

allowed_suffixes = {'.md', '.yaml', '.py'}
for path in ROOT.rglob('*'):
    if not release_file(path):
        continue
    check(path.suffix in allowed_suffixes or path.name in {'LICENSE', '.gitignore'}, f'Unexpected release file: {path.relative_to(ROOT)}')

check((ROOT / 'LICENSE').exists(), 'Missing license')
check((ROOT / 'examples' / 'evaluation-cases.md').exists(), 'Missing behavioral evaluation cases')

if errors:
    print('\n'.join('FAIL: ' + message for message in errors))
    sys.exit(1)
print(f'PASS: metadata, {links} local links, portable skill resources and release boundaries')
print('This is structural validation, not a visual or behavioral test.')
