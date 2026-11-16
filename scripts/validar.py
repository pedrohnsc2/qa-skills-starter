#!/usr/bin/env python3
"""Valida metadados, caminhos de memória, links locais e exportações do kit."""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / 'scripts/exportar.py'), '--check'], check=True)
expected_names = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
assert len(expected_names) == 8
packages = [ROOT / '.claude', ROOT / 'integracoes/cursor/.cursor',
            ROOT / 'integracoes/agentes/.agents', ROOT / 'integracoes/gemini-cli/.gemini']
for package in packages:
    assert {p.parent.name for p in (package / 'skills').glob('*/SKILL.md')} == expected_names, package
    for name in ['known-red-tests.md', 'known-traps.md']:
        assert (package / 'references/test-investigation' / name).is_file(), package
    for p in (package / 'skills').glob('*/SKILL.md'):
        for prefix in ['.claude', '.cursor', '.agents', '.gemini']:
            if prefix != package.name:
                assert prefix + '/references/' not in p.read_text(encoding='utf-8'), p

count = 0
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:
        continue
    text = p.read_text(encoding='utf-8')
    if p.name == 'SKILL.md':
        _, front, body = text.split('---', 2)
        fields = dict(line.split(': ', 1) for line in front.strip().splitlines())
        assert fields['name'] == p.parent.name, p
        assert re.fullmatch('[a-z0-9-]+', fields['name']), p
        assert isinstance(json.loads(fields['description']), str), p
        assert body.strip(), p
        count += 1
    # Os links de navegação, fora dos exemplos em blocos de código.
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)]+)\)', prose):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        local = unquote(target.split('#', 1)[0])
        assert (p.parent / local).exists(), f'Link quebrado: {p}: {target}'
assert count == 43, count  # 8 fontes, 4 pacotes de 8 e 3 skills para chat.
for p in (ROOT / 'prompts').glob('*.md'):
    if p.name != 'README.md':
        assert 'não execute comandos' in p.read_text(encoding='utf-8'), p
print(f'OK: {count} SKILL.md, memória, modo chat e links locais.')
