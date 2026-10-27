"""Visible geometry only; no bot or replay mutations."""
import json
from pathlib import Path
from types import SimpleNamespace
from test_coordinated_body import load_bot

WORK=Path(__file__).resolve().parent
record=json.loads((WORK/'frontier_scorer_snapshots.json').read_text(encoding='utf-8-sig'))
out=[]
for death in record['deaths']:
    snap=death['victimBefore']
    h,bot=load_bot('coordinated_body_hunter')
    width,height=snap['width'],snap['height']
    bot.game=h.game=h.Game(width,height,64)
    bot.ct=SimpleNamespace(get_unit_count=lambda:snap['count'],get_length=lambda:snap['length'],
                           get_id=lambda:snap['id'],get_team=lambda:h.Team(snap['team']))
    tiles={}
    for cell in snap['cells']:
        p=cell.get('part');pos=h.Position(cell['x'],cell['y'])
        part=h.DragonPart(pos,p['id'],h.Team(p['team']),h.Direction.NORTH,p['head']) if p else None
        edges=tuple(h.Edge(i%2==0,h.EdgeType(kind),portal) for i,(kind,portal) in enumerate(cell['edges']))
        tiles[cell['x'],cell['y']]=h.Tile(pos,part,-1,cell['pearl'],edges)
    occupied={p for p,t in tiles.items() if t.get_dragon() is not None}
    graph,frontier=bot.visible_graph(tiles,occupied,width,height)
    risk=bot.head_risks(tiles,graph,snap['id'],h.Team(snap['team']))
    nonself={p for p in occupied if tiles[p].get_dragon().get_id()!=snap['id']}
    transparent,_=bot.visible_graph(tiles,nonself,width,height)
    transparent_risk=bot.head_risks(tiles,transparent,snap['id'],h.Team(snap['team']))
    here=snap['head']['x'],snap['head']['y']
    options=[]
    for d,q in zip(bot.DIRECTIONS,bot.neighbours(here,width,height)):
        if tiles[here].get_edge(d).get_edge_type()!=h.EdgeType.EMPTY or q not in tiles or q in occupied:
            continue
        info=bot.inspect_route(q,graph,frontier,tiles,risk,snap['round'])
        options.append({'dir':d.value,'to':q,'risk':risk.get(q,0),'unshieldedRisk':transparent_risk.get(q,0),
                        'pearl':tiles[q].has_pearl(),'area':info[0],'exits':graph[q], 'frontier':frontier[q]})
    queue=[(here,'',(),snap['length'],0)]
    escapes=[]
    for p,route,trail,length,food in queue:
        if len(route)>=3 or (route and length<=2):
            continue
        for d,q in zip(bot.DIRECTIONS,bot.neighbours(p,width,height)):
            if (tiles[p].get_edge(d).get_edge_type()!=h.EdgeType.EMPTY or q not in tiles
                    or q in occupied or q in trail):
                continue
            following=route+d.value
            eaten=int(tiles[q].has_pearl())
            new_length=length-int(bool(route))+eaten
            next_trail=trail+(q,)
            if len(following)>=2 and transparent_risk.get(q,0)==0:
                onward=[z for z in graph[q] if z not in next_trail and transparent_risk.get(z,0)==0]
                if onward:
                    escapes.append({'route':following,'to':q,'remainingLength':new_length,
                                    'food':food+eaten,'onward':onward})
            queue.append((q,following,next_trail,new_length,food+eaten))
    out.append({'round':death['round'],'preRound':snap['round'],'id':snap['id'],'length':snap['length'],
                'head':here,'actual':death['victimAction'],'actor':death['actor'],
                'actorHead':death['actorHead'],'actorLength':death['actorLength'],'attack':death['actorAction'],
                'actorVisible':any(v['id']==death['actor'] for v in snap['visibleHeads']),
                'options':options,'escapes':escapes,'visibleEnemies':[v for v in snap['visibleHeads'] if v['team']!=snap['team']]})
(WORK/'frontier_scorer_geometry.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
