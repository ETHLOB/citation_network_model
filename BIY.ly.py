import warnings
import pandas as pd
import numpy as np
import scipy as sp
import networkx as nx

gen0 = pd.read_csv('0gen.csv')
agen1 = pd.read_csv('1gen_1.csv') 
bgen1 = pd.read_csv('1gen_2.csv')
cgen1 = pd.read_csv('1gen_3.csv')
dgen1 = pd.read_csv('1gen_4.csv')
egen1 = pd.read_csv('1gen_5.csv')
for i in range(1, 51):
    try: 
        globals()['agen2_'+str(i)] = pd.read_csv('2gen_1/2gen_'+str(i)+'.csv')
    except: continue
for i in range(1, 51):
    for j in range(1, 150):
        try:
            globals()['agen3_'+str(i)+'_'+str(j)] = pd.read_csv('3gen_1/3gen_'+str(i)+'_'+str(j)+'.csv')
        except: continue
for i in range(1, 28):
    try: 
        globals()['bgen2_'+str(i)] = pd.read_csv('2gen_2/2gen_'+str(i)+'.csv')
    except: continue
for i in range(1, 28):
    for j in range(1, 397):
        try:
            globals()['bgen3_'+str(i)+'_'+str(j)] = pd.read_csv('3gen_2/3gen_'+str(i)+'_'+str(j)+'.csv')
        except: continue
for i in range(1, 31):
    try: 
        globals()['cgen2_'+str(i)] = pd.read_csv('2gen_3/2gen_'+str(i)+'.csv')
    except: continue
for i in range(1, 31):
    for j in range(1, 70):
        try:
            globals()['cgen3_'+str(i)+'_'+str(j)] = pd.read_csv('3gen_3/3gen_'+str(i)+'_'+str(j)+'.csv')
        except: continue
for i in range(1, 32):
    try: 
        globals()['dgen2_'+str(i)] = pd.read_csv('2gen_4/2gen_'+str(i)+'.csv')
    except: continue
for i in range(1, 32):
    for j in range(1, 147):
        try:
            globals()['dgen3_'+str(i)+'_'+str(j)] = pd.read_csv('3gen_4/3gen_'+str(i)+'_'+str(j)+'.csv')
        except: continue
for i in range(1, 49):
    try: 
        globals()['egen2_'+str(i)] = pd.read_csv('2gen_5/2gen_'+str(i)+'.csv')
    except: continue
for i in range(1, 49):
    for j in range(1, 171):
        try:
            globals()['egen3_'+str(i)+'_'+str(j)] = pd.read_csv('3gen_5/3gen_'+str(i)+'_'+str(j)+'.csv')
        except: continue

alink0_1 = pd.concat([gen0['EID'], agen1['EID']], axis=1, keys=['FROM', 'TO'])
alink0_1['FROM'] = alink0_1['FROM'][0]
blink0_1 = pd.concat([gen0['EID'], bgen1['EID']], axis=1, keys=['FROM', 'TO'])
blink0_1['FROM'] = blink0_1['FROM'][1]
clink0_1 = pd.concat([gen0['EID'], cgen1['EID']], axis=1, keys=['FROM', 'TO'])
clink0_1['FROM'] = clink0_1['FROM'][2]
dlink0_1 = pd.concat([gen0['EID'], dgen1['EID']], axis=1, keys=['FROM', 'TO'])
dlink0_1['FROM'] = dlink0_1['FROM'][3]
elink0_1 = pd.concat([gen0['EID'], egen1['EID']], axis=1, keys=['FROM', 'TO'])
elink0_1['FROM'] = elink0_1['FROM'][4]

aLOCAL = nx.DiGraph()
bLOCAL = nx.DiGraph()
cLOCAL = nx.DiGraph()
dLOCAL = nx.DiGraph()
eLOCAL = nx.DiGraph()
GENERAL = nx.DiGraph()

aLOCAL.add_edges_from(alink0_1.values)
bLOCAL.add_edges_from(blink0_1.values)
cLOCAL.add_edges_from(clink0_1.values)
dLOCAL.add_edges_from(dlink0_1.values)
eLOCAL.add_edges_from(elink0_1.values)

GENERAL.add_edges_from(alink0_1.values)
GENERAL.add_edges_from(blink0_1.values)
GENERAL.add_edges_from(clink0_1.values)
GENERAL.add_edges_from(dlink0_1.values)
GENERAL.add_edges_from(elink0_1.values)

for i in range(1, 51):
    try:       
        globals()['alink1_2'+str(i)] = pd.concat([agen1['EID'], globals()['agen2_'+str(i)]['EID']], 
                                                 axis=1, keys=['FROM','TO'])
        globals()['alink1_2'+str(i)]['FROM'] = globals()['alink1_2'+str(i)]['FROM'][i-1]
        aLOCAL.add_edges_from(globals()['alink1_2'+str(i)].dropna().values)
        GENERAL.add_edges_from(globals()['alink1_2'+str(i)].dropna().values)
    except: continue
for i in range(1, 28):
    try:
        globals()['blink1_2'+str(i)] = pd.concat([bgen1['EID'], globals()['bgen2_'+str(i)]['EID']], 
                                                 axis=1, keys=['FROM','TO'])
        globals()['blink1_2'+str(i)]['FROM'] = globals()['blink1_2'+str(i)]['FROM'][i-1]
        bLOCAL.add_edges_from(globals()['blink1_2'+str(i)].dropna().values)
        GENERAL.add_edges_from(globals()['blink1_2'+str(i)].dropna().values)
    except: continue
for i in range(1, 31):
    try:
        globals()['clink1_2'+str(i)] = pd.concat([cgen1['EID'], globals()['cgen2_'+str(i)]['EID']], 
                                                 axis=1, keys=['FROM','TO'])
        globals()['clink1_2'+str(i)]['FROM'] = globals()['clink1_2'+str(i)]['FROM'][i-1]
        cLOCAL.add_edges_from(globals()['clink1_2'+str(i)].dropna().values)
        GENERAL.add_edges_from(globals()['clink1_2'+str(i)].dropna().values)
    except: continue
for i in range(1, 32):
    try:
        globals()['dlink1_2'+str(i)] = pd.concat([dgen1['EID'], globals()['dgen2_'+str(i)]['EID']], 
                                                 axis=1, keys=['FROM','TO'])
        globals()['dlink1_2'+str(i)]['FROM'] = globals()['dlink1_2'+str(i)]['FROM'][i-1]
        dLOCAL.add_edges_from(globals()['dlink1_2'+str(i)].dropna().values)
        GENERAL.add_edges_from(globals()['dlink1_2'+str(i)].dropna().values)
    except: continue
for i in range(1, 49):
    try:
        globals()['elink1_2'+str(i)] = pd.concat([egen1['EID'], globals()['egen2_'+str(i)]['EID']], 
                                                 axis=1, keys=['FROM','TO'])
        globals()['elink1_2'+str(i)]['FROM'] = globals()['elink1_2'+str(i)]['FROM'][i-1]
        eLOCAL.add_edges_from(globals()['elink1_2'+str(i)].dropna().values)
        GENERAL.add_edges_from(globals()['elink1_2'+str(i)].dropna().values)
    except: continue
for i in range(1, 56):
    for j in range(1, 150):
        try:
            globals()['alink2_3'+str(i)+'_'+str(j)] = pd.concat([globals()['agen2_'+str(i)]['EID'], 
                                                                 globals()['agen3_'+str(i)+'_'+str(j)]['EID']], 
                                                                axis=1, keys=['FROM','TO'])
            globals()['alink2_3'+str(i)+'_'+str(j)]['FROM'] = globals()['alink2_3'+str(i)+'_'+str(j)]['FROM'][j-1]
            aLOCAL.add_edges_from(globals()['alink2_3'+str(i)+'_'+str(j)].dropna().values)
            GENERAL.add_edges_from(globals()['alink2_3'+str(i)+'_'+str(j)].dropna().values)
        except: continue
for i in range(1, 28):
    for j in range(1, 397):
        try:
            globals()['blink2_3'+str(i)+'_'+str(j)] = pd.concat([globals()['bgen2_'+str(i)]['EID'], 
                                                                 globals()['bgen3_'+str(i)+'_'+str(j)]['EID']], 
                                                                axis=1, keys=['FROM','TO'])
            globals()['blink2_3'+str(i)+'_'+str(j)]['FROM'] = globals()['blink2_3'+str(i)+'_'+str(j)]['FROM'][j-1]
            bLOCAL.add_edges_from(globals()['blink2_3'+str(i)+'_'+str(j)].dropna().values)
            GENERAL.add_edges_from(globals()['blink2_3'+str(i)+'_'+str(j)].dropna().values)
        except: continue
for i in range(1, 31):
    for j in range(1, 70):
        try:
            globals()['clink2_3'+str(i)+'_'+str(j)] = pd.concat([globals()['cgen2_'+str(i)]['EID'], 
                                                                 globals()['cgen3_'+str(i)+'_'+str(j)]['EID']], 
                                                                axis=1, keys=['FROM','TO'])
            globals()['clink2_3'+str(i)+'_'+str(j)]['FROM'] = globals()['clink2_3'+str(i)+'_'+str(j)]['FROM'][j-1]
            cLOCAL.add_edges_from(globals()['clink2_3'+str(i)+'_'+str(j)].dropna().values)
            GENERAL.add_edges_from(globals()['clink2_3'+str(i)+'_'+str(j)].dropna().values)
        except: continue
for i in range(1, 32):
    for j in range(1, 147):
        try:
            globals()['dlink2_3'+str(i)+'_'+str(j)] = pd.concat([globals()['dgen2_'+str(i)]['EID'], 
                                                                 globals()['dgen3_'+str(i)+'_'+str(j)]['EID']], 
                                                                axis=1, keys=['FROM','TO'])
            globals()['dlink2_3'+str(i)+'_'+str(j)]['FROM'] = globals()['dlink2_3'+str(i)+'_'+str(j)]['FROM'][j-1]
            dLOCAL.add_edges_from(globals()['dlink2_3'+str(i)+'_'+str(j)].dropna().values)
            GENERAL.add_edges_from(globals()['dlink2_3'+str(i)+'_'+str(j)].dropna().values)
        except: continue
for i in range(1, 49):
    for j in range(1, 171):
        try:
            globals()['elink2_3'+str(i)+'_'+str(j)] = pd.concat([globals()['egen2_'+str(i)]['EID'], 
                                                                 globals()['egen3_'+str(i)+'_'+str(j)]['EID']], 
                                                                axis=1, keys=['FROM','TO'])
            globals()['elink2_3'+str(i)+'_'+str(j)]['FROM'] = globals()['elink2_3'+str(i)+'_'+str(j)]['FROM'][j-1]
            eLOCAL.add_edges_from(globals()['elink2_3'+str(i)+'_'+str(j)].dropna().values)
            GENERAL.add_edges_from(globals()['elink2_3'+str(i)+'_'+str(j)].dropna().values)
        except: continue

aLOCAL.remove_edges_from(nx.selfloop_edges(aLOCAL))
bLOCAL.remove_edges_from(nx.selfloop_edges(bLOCAL))
cLOCAL.remove_edges_from(nx.selfloop_edges(cLOCAL))
dLOCAL.remove_edges_from(nx.selfloop_edges(dLOCAL))
eLOCAL.remove_edges_from(nx.selfloop_edges(eLOCAL))
GENERAL.remove_edges_from(nx.selfloop_edges(GENERAL))

nx.set_node_attributes(GENERAL, gen0[['Year', 'Document Type', 'Access Type', 'Title', 
                                      'EID']].set_index('EID').to_dict('index'))
for i in ('a', 'b', 'c', 'd', 'e'):
    nx.set_node_attributes(globals()[i+'LOCAL'], gen0[['Year', 'Document Type', 'Access Type', 'Title', 'Cited by',
                                                       'EID']].set_index('EID').to_dict('index'))
    nx.set_node_attributes(GENERAL, globals()[i+'gen1'][['Year', 'Document Type', 'Access Type', 'Title', 'Cited by',
                                                         'EID']].set_index('EID').to_dict('index'))
    nx.set_node_attributes(globals()[i+'LOCAL'], globals()[i+'gen1'][['Year', 'Document Type', 'Access Type', 'Title', 'Cited by',
                                                                      'EID']].set_index('EID').to_dict('index'))

for k in ('a', 'b', 'c', 'd', 'e'):
    for i in range(1, 56):
        try: 
            nx.set_node_attributes(GENERAL, globals()[k+'gen2_'+str(i)][['Year', 'Document Type', 'Access Type', 'Title', 'Cited by', 
                                                                         'EID']].set_index('EID').to_dict('index'))
            nx.set_node_attributes(globals()[k+'LOCAL'], globals()[k+'gen2_'+str(i)][['Year', 'Document Type,
                                                                                      'Access Type', 'Title', 'Cited by',
                                                                                      'EID'
                                                                                      ]].set_index('EID').to_dict('index'))
            for j in range(1, 400):
                try:
                    nx.set_node_attributes(GENERAL, 
                                           globals()[k+'gen3_'+str(i)+'_'+str(j)][['Year', 'Document Type', 'Access Type', 
                                                                                   'Title', 'Cited by', 
                                                                                   'EID'
                                                                                   ]].set_index('EID').to_dict('index'))
                    nx.set_node_attributes(globals()[k+'LOCAL'],
                                           globals()[k+'gen3_'+str(i)+'_'+str(j)][['Year', 'Document Type', 'Access Type',
                                                                                   'Title', 'Cited by',
                                                                                   'EID'
                                                                                   ]].set_index('EID').to_dict('index'))
                except: continue                   
        except: continue

viz = pd.read_csv('viz.csv', engine='python')
nx.set_node_attributes(GENERAL, viz[['EID', 'Group', 'Magnitude']].set_index('EID').to_dict('index'))