"""Geometry-only counterfactuals for replay scorer deaths, never game inputs."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(WORK / 'bots/coordinated_escape'))
import main as bot
import helper as h

result = []
for name in sys.argv[1:]:
    for record in json.loads(Path(name).read_text(encoding='utf-8')):
        for death in record['scorerHeadDeaths']:
            snap = death['victimBefore']
            width, height = snap['width'], snap['height']
            bot.game = h.game = h.Game(width, height, 64)
            bot.ct = SimpleNamespace(get_unit_count=lambda: 10,
                                     get_length=lambda: snap['length'],
                                     get_id=lambda: death['id'],
                                     get_team=lambda: h.Team.A)
            tiles = {}
            for cell in snap['cells']:
                p = cell.get('part')
                pos = h.Position(cell['x'], cell['y'])
                part = h.DragonPart(pos, p['id'], h.Team(p['team']), h.Direction.NORTH, p['head']) if p else None
                edges = tuple(h.Edge(i % 2 == 0, h.EdgeType(kind), portal)
                              for i, (kind, portal) in enumerate(cell['edges']))
                tiles[cell['x'], cell['y']] = h.Tile(pos, part, -1, False, edges)
            occupied = {p for p, tile in tiles.items() if tile.get_dragon() is not None}
            graph, frontier = bot.visible_graph(tiles, occupied, width, height)
            danger = bot.head_risks(tiles, graph, death['id'], h.Team.A)
            here = snap['head']['x'], snap['head']['y']
            route = bot.scorer_escape(tiles, occupied, here, graph, danger, width, height)
            steps = [(d.value, q, danger.get(q, 0)) for d, q in
                     zip(bot.DIRECTIONS, bot.neighbours(here, width, height))
                     if tiles[here].get_edge(d).get_edge_type() == h.EdgeType.EMPTY
                     and q in tiles and q not in occupied]
            option_details = [{'direction': direction, 'position': q,
                               'risk': risk, 'exits': graph[q], 'frontier': frontier[q],
                               'area': bot.inspect_route(q, graph, frontier, tiles, danger, snap['round'])[0]}
                              for direction, q, risk in steps]
            # Diagnostic only: determine whether the all-first-unsafe gate
            # excludes an otherwise geometrically verified escape.
            forced_gate = dict(danger)
            forced_gate.update({q: max(1050, danger.get(q, 0)) for q in graph[here]})
            counter_route = bot.scorer_escape(tiles, occupied, here, graph, forced_gate, width, height)
            result.append({'replay': record['file'], 'fatal_round': death['round'],
                           'pre_action_round': snap['round'], 'id': death['id'],
                           'length': death['length'], 'head': here,
                           'own_visible_parts': sum(tile.get_dragon() is not None
                                                    and tile.get_dragon().get_id() == death['id']
                                                    for tile in tiles.values()),
                           'actual_action': death['victimAction'],
                           'enemy_action': death['actorAction'],
                           'ordinary_options': steps,
                           'option_details': option_details,
                           'geometry_escape': ''.join(d.value for d in route) if route else None,
                           'route_if_first_step_gate_relaxed': ''.join(d.value for d in counter_route) if counter_route else None,
                           'limitation': 'Pearls omitted; route tie preference can differ. Risk is visible-head estimate, not full counterfactual match result.'})
print(json.dumps(result, indent=2))
