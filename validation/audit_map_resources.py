"""Separate a replay's visible geometry from a playable spawn configuration."""
import hashlib
import json
from pathlib import Path

WORK = Path(__file__).resolve().parent
ROOT = WORK.parent


def summarize(path):
    lines = [line.split() for line in path.read_text(encoding='utf-8').splitlines()
             if line.startswith('TILE ')]
    return {'name': path.stem, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'tiles': len(lines), 'active_spawners': sum(int(row[4]) > 0 for row in lines)}


current = [summarize(ROOT / 'v7_work/maps' / (name + '.map'))
           for name in (WORK / 'current_maps.txt').read_text().split()]
replays = [summarize(p) for p in sorted((ROOT / 'v7_work/maps').glob('M547*.map'))]
assert all(row['active_spawners'] > 0 for row in current)
proof = {'benchmark_maps': current, 'new_replay_exports': replays,
         'interpretation': 'Current benchmark maps retain natural spawners. Zero-spawner exports cannot reproduce live pearl schedules; use their terrain only.',
         'rules': 'https://game.battlecode.au/docs/map-files'}
(WORK / 'map_resource_audit.json').write_text(json.dumps(proof, indent=2) + '\n', encoding='utf-8')
print('Benchmark maps with resources:', len(current))
print('Latest replay exports with zero spawners:', sum(row['active_spawners'] == 0 for row in replays), '/', len(replays))
