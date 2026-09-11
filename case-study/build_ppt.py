# StainlessCarbon(TM) - Round 1 deck v4 "BLUEPRINT + VOICE"
# Blueprint wirework kept; hierarchy restored: action titles, one hero per
# slide, dashboard mockup back, recommendations block, 8pt floor, no redundancy.
# All numbers trace to research/22-canonical-model-v1.md (LOCKED).

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

BG      = RGBColor(0x10, 0x14, 0x1A)
PANEL   = RGBColor(0x18, 0x1E, 0x27)
PANEL2  = RGBColor(0x20, 0x28, 0x33)
INK     = RGBColor(0x0B, 0x0E, 0x13)
LINE    = RGBColor(0x39, 0x44, 0x52)
LINE2   = RGBColor(0x2A, 0x33, 0x3F)
WHITE   = RGBColor(0xF2, 0xF5, 0xF8)
MUTED   = RGBColor(0xA6, 0xB2, 0xBF)
FAINT   = RGBColor(0x74, 0x80, 0x8D)
AMBER   = RGBColor(0xF5, 0xA6, 0x23)
TEAL    = RGBColor(0x2D, 0xD4, 0xBF)
RED     = RGBColor(0xE8, 0x5D, 0x5D)
GREEN   = RGBColor(0x5D, 0xC9, 0x86)
BLUE    = RGBColor(0x5B, 0x9B, 0xEE)

SW, SH = Inches(13.333), Inches(7.5)
prs = Presentation(); prs.slide_width, prs.slide_height = SW, SH
blank = prs.slide_layouts[6]

def slide_bg(s):
    s.background.fill.solid(); s.background.fill.fore_color.rgb = BG

def box(s, x, y, w, h, fill=PANEL, line=None, lw=0.75):
    shp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    if fill is None: shp.fill.background()
    else: shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(lw)
    shp.shadow.inherit = False
    return shp

def txt(s, x, y, w, h, runs, size=9, color=WHITE, bold=False, align=PP_ALIGN.LEFT,
        anchor=MSO_ANCHOR.TOP, space_after=1, line_spacing=1.0):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Pt(1.5); tf.margin_top = tf.margin_bottom = Pt(0.5)
    if isinstance(runs, str): runs = [runs]
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space_after); p.line_spacing = line_spacing
        if isinstance(para, str): para = [(para, {})]
        for t, st in para:
            r = p.add_run(); r.text = t; f = r.font
            f.size = Pt(st.get('size', size)); f.bold = st.get('bold', bold)
            f.color.rgb = st.get('color', color); f.name = st.get('font', 'Segoe UI')
            if st.get('italic'): f.italic = True
    return tb

def hline(s, x, y, w, color=LINE2, weight=0.8):
    return box(s, x, y, w, Pt(weight), fill=color)

def vline(s, x, y, h, color=LINE2, weight=0.8):
    return box(s, x, y, Pt(weight), h, fill=color)

def module(s, x, y, w, h, num, title, sub='', accent=AMBER):
    box(s, x, y, w, h, fill=PANEL, line=LINE, lw=1.0)
    box(s, x, y, Inches(0.46), Inches(0.3), fill=accent)
    txt(s, x, y+Inches(0.015), Inches(0.46), Inches(0.27),
        [[(num, {'size': 12, 'bold': True, 'color': INK})]], align=PP_ALIGN.CENTER)
    txt(s, x+Inches(0.56), y+Inches(0.035), w-Inches(0.62), Inches(0.26),
        [[(title, {'size': 10.5, 'bold': True, 'color': WHITE}),
          (('   '+sub) if sub else '', {'size': 8, 'color': MUTED})]])
    hline(s, x, y+Inches(0.32), w, color=LINE)
    return y + Inches(0.38)

def set_cell(cell, paras, size=8, color=WHITE, bold=False, align=PP_ALIGN.LEFT, fill=PANEL):
    cell.fill.solid(); cell.fill.fore_color.rgb = fill
    tf = cell.text_frame; tf.word_wrap = True
    tf.margin_left = Pt(3); tf.margin_right = Pt(3); tf.margin_top = Pt(0.5); tf.margin_bottom = Pt(0.5)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    if isinstance(paras, str): paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if isinstance(para, str): para = [(para, {})]
        for t, st in para:
            r = p.add_run(); r.text = t; f = r.font
            f.size = Pt(st.get('size', size)); f.bold = st.get('bold', bold)
            f.color.rgb = st.get('color', color); f.name = 'Segoe UI'

def mktable(s, rows, cols, x, y, w, h):
    tb = s.shapes.add_table(rows, cols, x, y, w, h).table
    tbl = tb._tbl
    el = tbl.find(qn('a:tableStyleId'))
    if el is not None: tbl.remove(el)
    return tb

M = Inches(0.28)

# =====================================================================
# SLIDE 1
# =====================================================================
s = prs.slides.add_slide(blank); slide_bg(s)

# ---- ACTION TITLE ----
txt(s, M, Inches(0.05), Inches(9.75), Inches(0.58),
    [[('60–80% of stainless steel’s carbon is invisible to every existing tool —', {'size': 16.5, 'bold': True, 'color': WHITE})],
     [('StainlessCarbon', {'size': 16.5, 'bold': True, 'color': AMBER}),
      ('™', {'size': 16.5, 'bold': True, 'color': AMBER}),
      (' is the first calculator built to see it', {'size': 16.5, 'bold': True, 'color': WHITE})]],
    space_after=0, line_spacing=1.0)
txt(s, M, Inches(0.635), Inches(9.75), Inches(0.22),
    [[('Stainless alloy chain (FeCr + Ni)  ·  India’s real grid & captive-coal economics  ·  metallurgical guardrails  ·  every tonne priced in CBAM euros', {'size': 9.5, 'color': MUTED})]])
meta_x = Inches(10.18)
box(s, meta_x, Inches(0.09), Inches(2.87), Inches(0.70), fill=None, line=LINE, lw=1.0)
txt(s, meta_x+Inches(0.08), Inches(0.13), Inches(2.73), Inches(0.62),
    [[('JINDAL STAINLESS · PROBLEM STATEMENT 3', {'size': 7.6, 'bold': True, 'color': AMBER})],
     [('ROUND 1 EXECUTIVE SUMMARY · 11 SEP 2026', {'size': 7.6, 'color': MUTED})],
     [('TEAM: [ADD NAME]  ·  LIVE TOOL: [ADD LINK]', {'size': 7.6, 'bold': True, 'color': TEAL})],
     [('BOUNDARY: S1+S2+S3 · ISSF-ALIGNED', {'size': 7.6, 'color': MUTED})]],
    space_after=1.2)
hline(s, M, Inches(0.86), SW-2*M, color=LINE, weight=1.2)

# ---- 01 CHAIN ----
y1 = Inches(0.94); ch_h = Inches(1.20)
yy = module(s, M, y1, SW-2*M, ch_h, '01', 'THE PHYSICAL → REGULATORY CHAIN',
            'where CO₂ enters each tonne, and where the EU prices it · fig 1.1', accent=AMBER)
stages = [
    ('CHARGE MAKE-UP', 'S3', RED,   'scrap 70% (cap 80%) · FeCr 5.4–5.9', 'NPI 60–85 tCO₂/t contained Ni'),
    ('EAF MELT', 'S2', TEAL,        '400–600 kWh/t melt', 'grid 0.710 · captive 1.045'),
    ('AOD REFINE', 'S1', AMBER,     'O₂/Ar decarburization', 'process CO₂ (unavoidable)'),
    ('CAST + REHEAT', 'S1', AMBER,  'FO/LSHS 71.9 gCO₂/MJ', '→ NG −31% · Bio-LDO ≈ 0'),
    ('ROLL + FINISH', 'S1', AMBER,  'anneal · pickle · BA lines', 'propane → green H₂'),
    ('MILL GATE', 'KPI', GREEN,     'S1+2 = 1.76 tCO₂e/tcs', 'cradle-to-gate 3.03'),
    ('EU BORDER', '€', BLUE,        'default 8.44 → €446/t', 'verified 0.9–1.4 → €48–74'),
]
n = len(stages); gap = Inches(0.10)
cw = (SW - 2*M - Inches(0.24) - gap*(n-1)) / n
cx = M + Inches(0.12)
for i,(t1, tag, cc, a1, a2) in enumerate(stages):
    ch = s.shapes.add_shape(MSO_SHAPE.CHEVRON, cx, yy+Inches(0.02), cw+Inches(0.12), Inches(0.30))
    ch.adjustments[0] = 0.35
    ch.fill.solid(); ch.fill.fore_color.rgb = PANEL2
    ch.line.color.rgb = cc; ch.line.width = Pt(1.1); ch.shadow.inherit = False
    tf = ch.text_frame; tf.word_wrap = False
    tf.margin_left = Pt(6); tf.margin_right = Pt(2); tf.margin_top = Pt(0); tf.margin_bottom = Pt(0)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = t1; r.font.size = Pt(7.8); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name='Segoe UI'
    txt(s, cx+Inches(0.02), yy+Inches(0.365), cw-Inches(0.02), Inches(0.42),
        [[(tag+'  ', {'size': 8, 'bold': True, 'color': cc}),
          (a1, {'size': 8, 'color': MUTED})],
         [(a2, {'size': 8, 'color': MUTED})]],
        line_spacing=0.95, space_after=0)
    cx += cw + gap

# ---- middle band ----
y2 = y1 + ch_h + Inches(0.10)
mid_h = Inches(3.34)

# 02 GAPS
W02 = Inches(3.55)
yy = module(s, M, y2, W02, mid_h, '02', 'FOUR STRUCTURAL GAPS', 'in every existing tool', accent=RED)
gaps = [
    ('G1  Alloy blindspot', 'Ferrochrome + nickel drive the stainless footprint, yet carbon-steel tools model 0% of the alloy chain.'),
    ('G2  India blindspot', 'Western tools assume 0.2–0.4 t/MWh grids; India’s reality is 2–5× dirtier power (CEA v21.0).'),
    ('G3  Feasibility blindspot', 'Sliders to 100% scrap ignore Cu/Sn tramp hot-shortness and India’s 23–25% scrap pool → real cap ~80%.'),
    ('G4  Finance blindspot', 'No tool prices the tonne at the EU border — a €372–398/t default-vs-verified swing by 2030.'),
]
gy = yy + Inches(0.04)
for head, body in gaps:
    box(s, M+Inches(0.10), gy+Inches(0.02), Inches(0.045), Inches(0.52), fill=RED)
    txt(s, M+Inches(0.22), gy, W02-Inches(0.34), Inches(0.64),
        [[(head, {'size': 9.2, 'bold': True, 'color': WHITE})],
         [(body, {'size': 8.2, 'color': MUTED})]], line_spacing=0.96, space_after=1)
    gy += Inches(0.645)
hline(s, M+Inches(0.10), gy+Inches(0.03), W02-Inches(0.2))
txt(s, M+Inches(0.10), gy+Inches(0.08), W02-Inches(0.2), Inches(0.3),
    [[('Evidence: UX teardown of Primetals CO₂ Calculator & SSAB EcoUpgraded — 5 gaps documented (research file 07).', {'size': 7.5, 'color': FAINT, 'italic': True})]], line_spacing=0.95)

# 03 THE PRODUCT (hero)
X03 = M + W02 + Inches(0.12); W03 = Inches(5.55)
yy = module(s, X03, y2, W03, mid_h, '03', 'THE PRODUCT — LIVE CALCULATOR', '4 levers · instant CO₂/t · optimizer · fig 1.2', accent=TEAL)
mx, my = X03+Inches(0.12), yy+Inches(0.05)
mw, mh = W03-Inches(0.24), mid_h-Inches(0.78)
box(s, mx, my, mw, mh, fill=INK, line=LINE, lw=1.0)
# sliders
spx = mx+Inches(0.12); spw = Inches(2.0)
sliders = [('Scrap charge', '70%', 0.70, TEAL),
           ('Ni source: scrap ↔ NPI', '60%', 0.60, TEAL),
           ('Renewable electricity', '47%', 0.47, AMBER),
           ('Clean fuel (H₂ · Bio-LDO)', '30%', 0.30, AMBER)]
spy = my+Inches(0.14)
for name, val, frac, acc in sliders:
    txt(s, spx, spy, spw, Inches(0.18),
        [[(name, {'size': 8.2, 'color': MUTED}), ('   '+val, {'size': 8.6, 'bold': True, 'color': WHITE})]])
    box(s, spx, spy+Inches(0.205), spw, Inches(0.05), fill=LINE)
    box(s, spx, spy+Inches(0.205), Emu(int(spw*frac)), Inches(0.05), fill=acc)
    box(s, spx+Emu(int(spw*frac))-Inches(0.035), spy+Inches(0.172), Inches(0.08), Inches(0.11), fill=WHITE)
    spy += Inches(0.435)
box(s, spx+Emu(int(spw*0.8)), my+Inches(0.32), Inches(0.02), Inches(0.13), fill=RED)
txt(s, spx, spy-Inches(0.03), spw+Inches(0.2), Inches(0.2),
    [[('⚠ 80% hard cap — Cu/Sn tramp guardrail', {'size': 7.8, 'bold': True, 'color': RED})]])
txt(s, spx, spy+Inches(0.17), spw+Inches(0.35), Inches(0.2),
    [[('Presets: ', {'size': 7.4, 'color': MUTED}),
      ('FY26 Actual', {'size': 7.4, 'bold': True, 'color': TEAL}),
      (' · FY35 Target · Max-Green', {'size': 7.4, 'color': MUTED})]], space_after=0)
# gauge hero
gx = spx + spw + Inches(0.22); gw = mw - spw - Inches(0.46)
box(s, gx, my+Inches(0.12), gw, Inches(1.18), fill=PANEL2, line=TEAL, lw=1.0)
txt(s, gx+Inches(0.1), my+Inches(0.16), gw-Inches(0.2), Inches(0.2),
    [[('LIVE INTENSITY — SCOPE 1+2', {'size': 8, 'bold': True, 'color': MUTED})]])
txt(s, gx+Inches(0.06), my+Inches(0.30), gw-Inches(0.2), Inches(0.62),
    [[('1.76', {'size': 40, 'bold': True, 'color': TEAL}),
      ('  tCO₂e/tcs', {'size': 11, 'color': MUTED})]])
txt(s, gx+Inches(0.1), my+Inches(0.94), gw-Inches(0.2), Inches(0.2),
    [[('cradle-to-gate ', {'size': 8.2, 'color': MUTED}), ('3.03', {'size': 8.6, 'bold': True, 'color': WHITE}),
      ('   ·   FY35 target ', {'size': 8.2, 'color': MUTED}), ('0.99', {'size': 8.6, 'bold': True, 'color': AMBER})]])
# sensitivity strip (real deltas)
sy = my+Inches(1.42)
txt(s, gx+Inches(0.02), sy, gw, Inches(0.18),
    [[('WHICH LEVER MOVES CO₂ MOST  (Δ tCO₂/t)', {'size': 8, 'bold': True, 'color': MUTED})]])
sens = [('scrap +8pp', 0.32, TEAL), ('RE 47→65%', 0.28, AMBER), ('green H₂/bio', 0.15, GREEN)]
sy += Inches(0.22)
for lab, v, cc in sens:
    txt(s, gx+Inches(0.02), sy, Inches(1.05), Inches(0.17), [[(lab, {'size': 8, 'color': WHITE})]])
    blen = Emu(int(Inches(1.35) * (v/0.32)))
    box(s, gx+Inches(1.1), sy+Inches(0.025), blen, Inches(0.11), fill=cc)
    txt(s, gx+Inches(1.12)+blen, sy, Inches(0.55), Inches(0.17),
        [[('−'+f'{v:.2f}', {'size': 8, 'bold': True, 'color': cc})]])
    sy += Inches(0.215)
# export strip
box(s, mx+Inches(0.08), my+mh-Inches(0.30), mw-Inches(0.16), Inches(0.24), fill=PANEL2)
txt(s, mx+Inches(0.16), my+mh-Inches(0.275), mw-Inches(0.3), Inches(0.2),
    [[('Every run exports a per-tonne ', {'size': 8, 'color': MUTED}),
      ('CBAM invoice + DPP/EPD-ready record', {'size': 8, 'bold': True, 'color': AMBER}),
      (' — audit-grade MRV', {'size': 8, 'color': MUTED})]])

# 04 MATRIX
X04 = X03 + W03 + Inches(0.12); W04 = SW - X04 - M
yy = module(s, X04, y2, W04, mid_h, '04', 'COMPETITIVE MATRIX', 'fig 1.3', accent=GREEN)
rows = [('Alloy-chain emissions', '✗', '✗', '✓'),
        ('India grid + captive coal', '✗', '✗', '✓'),
        ('Feasibility guardrails', '✗', '✗', '✓'),
        ('Audited company anchor', '✗', '✗', '✓'),
        ('CBAM €/t + escalator', '✗', '✗', '✓'),
        ('Constrained optimizer', '△', '✗', '✓'),
        ('DPP/EPD export path', '✗', '✗', '✓')]
tb = mktable(s, 8, 4, X04+Inches(0.08), yy+Inches(0.02), W04-Inches(0.16), Inches(2.18))
tb.columns[0].width = Inches(1.40); tb.columns[1].width = Inches(0.74)
tb.columns[2].width = Inches(0.46); tb.columns[3].width = Inches(0.46)
for j,h in enumerate(['capability','Primetals','SSAB','Ours']):
    set_cell(tb.cell(0,j), [[(h, {'size':7.4,'bold':True,'color':MUTED})]], fill=INK,
             align=PP_ALIGN.CENTER if j else PP_ALIGN.LEFT)
for i,(feat,a,b,c) in enumerate(rows, start=1):
    set_cell(tb.cell(i,0), [[(feat, {'size':7.8,'color':WHITE})]], fill=PANEL if i%2 else PANEL2)
    for j,v in enumerate([a,b,c], start=1):
        col = GREEN if v=='✓' else (AMBER if v=='△' else FAINT)
        set_cell(tb.cell(i,j), [[(v, {'size':9,'bold':True,'color':col})]], align=PP_ALIGN.CENTER,
                 fill=RGBColor(0x1C,0x2B,0x26) if j==3 else (PANEL if i%2 else PANEL2))
for r in tb.rows: r.height = Inches(0.268)
txt(s, X04+Inches(0.08), yy+Inches(2.28), W04-Inches(0.16), Inches(0.6),
    [[('“SSAB simplicity × Primetals depth”', {'size': 8.2, 'bold': True, 'color': WHITE})],
     [('— rebuilt for stainless metallurgy and India.', {'size': 8, 'color': MUTED})]], line_spacing=1.0)

# ---- 05 MODEL SPEC (slim) ----
y3 = y2 + mid_h + Inches(0.10)
spec_h = Inches(1.30)
yy = module(s, M, y3, SW-2*M, spec_h, '05', 'EMISSIONS MODEL SPEC', 'ISSF/worldstainless-aligned · dual-output · validated within ~5% of audited data · spec 2.1', accent=BLUE)
txt(s, M+Inches(0.12), yy+Inches(0.015), Inches(8.9), Inches(0.22),
    [[('E(CO₂/t) = ', {'size': 10.5, 'bold': True, 'color': WHITE}),
      ('S1', {'size': 10.5, 'bold': True, 'color': AMBER}),
      ('[fuels · AOD · reductants]  +  ', {'size': 9.5, 'color': MUTED}),
      ('S2', {'size': 10.5, 'bold': True, 'color': TEAL}),
      ('[(1−RE%) · (grid | captive) · kWh]  +  ', {'size': 9.5, 'color': MUTED}),
      ('S3', {'size': 10.5, 'bold': True, 'color': RED}),
      ('[(1−scrap%) · Σ mᵢ·EFᵢ]', {'size': 9.5, 'color': MUTED}),
      ('    s.t. scrap ≤ 80% · Cu/Sn bounds', {'size': 8.2, 'color': FAINT, 'italic': True})]])
arch = [
    ('DATA', BLUE,  '19-file base — CEA v21.0 · BEE PAT · IPCC 2006 · ICDA FeCr LCA · ISSF benchmarks · JSL audited BRSR/CDP/ESG · EU regs', 'feeds →'),
    ('ENGINE', AMBER,'grade-wise charge chemistry (304/316/430/2205) · constrained optimizer · dual ISSF output (recycled-content + EoL credit) · CBAM escalator 2026–30', 'solves →'),
    ('INTERFACE', TEAL,'4 levers · live gauge · baseline-vs-target compare · per-tonne CBAM invoice · DPP/EPD export', ''),
]
ax = M+Inches(0.12); aw = (SW-2*M-Inches(0.24))/3 - Inches(0.10)
ay = yy + Inches(0.30)
for i,(name, cc, body, tail) in enumerate(arch):
    bx_ = ax + i*(aw+Inches(0.15))
    box(s, bx_, ay, aw, Inches(0.52), fill=PANEL2, line=cc, lw=1.1)
    txt(s, bx_+Inches(0.07), ay+Inches(0.035), Inches(0.95), Inches(0.2),
        [[(name, {'size': 8.6, 'bold': True, 'color': cc})]])
    txt(s, bx_+Inches(0.07), ay+Inches(0.20), aw-Inches(0.14), Inches(0.3),
        [[(body, {'size': 7.5, 'color': WHITE})]], line_spacing=0.9)
    if tail:
        txt(s, bx_+aw+Inches(0.005), ay+Inches(0.16), Inches(0.16), Inches(0.2),
            [[('→', {'size': 11, 'bold': True, 'color': LINE})]])

# ---- footer ----
fy = y3 + spec_h + Inches(0.05)
box(s, M, fy, SW-2*M, Inches(0.30), fill=INK, line=LINE, lw=0.75)
txt(s, M+Inches(0.1), fy+Inches(0.045), SW-2*M-Inches(0.2), Inches(0.24),
    [[('RESEARCH BASE  ', {'size': 7.6, 'bold': True, 'color': AMBER}),
      ('19 deep-dive files · 40+ primary sources · locked canonical model  |  ', {'size': 7.4, 'color': WHITE}),
      ('CEA v21.0 · BEE PAT · IPCC 2006 · worldstainless/ISSF · ICDA · EU Regs 2023/956 · 2025/2620-21 · JSL BRSR/CDP/ESG FY22–26 · Goldman · ICRA · CRISIL', {'size': 7.2, 'color': MUTED})]],
    space_after=0)

# =====================================================================
# SLIDE 2
# =====================================================================
s = prs.slides.add_slide(blank); slide_bg(s)
txt(s, M, Inches(0.09), Inches(10.6), Inches(0.60),
    [[('Validated on Jindal’s audited disclosures —', {'size': 16.5, 'bold': True, 'color': WHITE})],
     [('and worth ', {'size': 16.5, 'bold': True, 'color': WHITE}),
      ('₹200–290 crore a year', {'size': 16.5, 'bold': True, 'color': AMBER}),
      (' at the EU border by 2030', {'size': 16.5, 'bold': True, 'color': WHITE})]],
    space_after=0, line_spacing=1.0)
box(s, Inches(10.75), Inches(0.12), Inches(2.3), Inches(0.34), fill=None, line=LINE, lw=1.0)
txt(s, Inches(10.75), Inches(0.155), Inches(2.3), Inches(0.28),
    [[('VALIDATION · FINANCE · ACTION', {'size': 7.6, 'bold': True, 'color': AMBER})]], align=PP_ALIGN.CENTER)
hline(s, M, Inches(0.74), SW-2*M, color=LINE, weight=1.2)

yA = Inches(0.84); A_h = Inches(3.24)
# ---- 06 worked proof ----
W06 = Inches(6.35)
yy = module(s, M, yA, W06, A_h, '06', 'THE CALCULATOR, RUN ON JINDAL’S REALITY', 'disclosed → optimized · tab 3.1', accent=TEAL)
data = [
    ('lever / result', 'FY24 peak', 'FY26 actual', 'FY28–30 optimized', 'source'),
    ('Scrap charge', '~60%', '70.1%', '78%  (cap 80%)', 'BRSR FY26'),
    ('Renewable electricity', '~30%', '47%', '65%', 'ESG Factsheet'),
    ('Green H₂ / Bio-LDO', '—', 'pilot (Hisar)', 'scaled (Jajpur)', 'company PR'),
    ('S1+2 intensity  tCO₂e/tcs', '2.15', '1.76', '1.35–1.45', 'ESG FS / CDP'),
    ('S3 intensity', '1.90', '1.27', '0.95–1.05', 'ESG Factsheet'),
    ('Cradle-to-gate total', '4.05', '3.03', '≈2.30–2.50', 'derived'),
]
tb = mktable(s, len(data), 5, M+Inches(0.1), yy+Inches(0.03), W06-Inches(0.2), Inches(2.1))
tb.columns[0].width = Inches(1.85); tb.columns[1].width = Inches(0.95)
tb.columns[2].width = Inches(1.0);  tb.columns[3].width = Inches(1.32); tb.columns[4].width = Inches(1.03)
for j,h in enumerate(data[0]):
    set_cell(tb.cell(0,j), [[(h, {'size':7.6,'bold':True,'color':MUTED})]], fill=INK,
             align=PP_ALIGN.LEFT if j in (0,4) else PP_ALIGN.CENTER)
for i,row in enumerate(data[1:], start=1):
    kpi = i >= 4
    for j,v in enumerate(row):
        col = WHITE
        if kpi and j==2: col = TEAL
        if kpi and j==3: col = AMBER
        set_cell(tb.cell(i,j), [[(v, {'size':8 if not kpi else 8.8,'bold':kpi and 0<j<4,
                 'color':col if j>0 else WHITE})]],
                 fill=PANEL if i%2 else PANEL2,
                 align=PP_ALIGN.LEFT if j in (0,4) else PP_ALIGN.CENTER)
for r in tb.rows: r.height = Inches(0.29)
txt(s, M+Inches(0.1), yy+Inches(2.22), W06-Inches(0.2), Inches(0.5),
    [[('Δ FY24→FY26:  ', {'size': 8.6, 'bold': True, 'color': WHITE}),
      ('−25.2% total footprint · −18.1% S1+2', {'size': 8.6, 'bold': True, 'color': GREEN}),
      ('  →  glidepath to FY35 target ', {'size': 8.6, 'color': MUTED}),
      ('0.99', {'size': 8.6, 'bold': True, 'color': AMBER}),
      (' (−50% vs FY22)', {'size': 8.6, 'color': MUTED})],
     [('Every recommended lever is one Jindal is already investing in — ₹700 Cr solar · 300 MW hybrid · H₂ scale-up. The tool ranks them.', {'size': 7.8, 'color': FAINT, 'italic': True})]],
    line_spacing=1.0)

# ---- 07 CBAM hero ----
X07 = M + W06 + Inches(0.12); W07 = SW - X07 - M
yy = module(s, X07, yA, W07, A_h, '07', 'THE CBAM VERIFICATION DIVIDEND', '2030 exposure, €/t exported · fig 3.1', accent=AMBER)
bars = [('EU default assigned to India (8.44 t)', 446, RED, '€446'),
        ('India BF-BOF average', 122, RGBColor(0xC9,0x8A,0x4B), '€107–122'),
        ('JSL verified — conservative (1.4 t)', 74, TEAL, '€74'),
        ('JSL verified — CBAM-direct (0.9 t)', 48, GREEN, '€48')]
bby = yy + Inches(0.06)
for i,(lab,v,cc,vl) in enumerate(bars):
    yy2 = bby + i*Inches(0.40)
    txt(s, X07+Inches(0.12), yy2, Inches(2.6), Inches(0.2),
        [[(lab, {'size': 8.4, 'color': WHITE, 'bold': i>=2})]])
    blen = Emu(int(Inches(3.55) * (v/446.0))) + Inches(0.06)
    box(s, X07+Inches(0.12), yy2+Inches(0.17), blen, Inches(0.16), fill=cc)
    txt(s, X07+Inches(0.16)+blen, yy2+Inches(0.135), Inches(0.95), Inches(0.22),
        [[(vl, {'size': 10, 'bold': True, 'color': cc})]])
mech_y = bby + Inches(1.64)
txt(s, X07+Inches(0.12), mech_y, W07-Inches(0.24), Inches(0.2),
    [[('mechanics: default 6.49 base +30% no-data markup · phase-in 2.5%→48.5% · ETS €80→€109  (EU Regs 2025/2620-21)', {'size': 7.5, 'color': FAINT})]])
hline(s, X07+Inches(0.12), mech_y+Inches(0.22), W07-Inches(0.24))
txt(s, X07+Inches(0.12), mech_y+Inches(0.28), W07-Inches(0.24), Inches(0.75),
    [[('₹200–290 Cr / yr', {'size': 25, 'bold': True, 'color': AMBER}),
      ('   (€22–32M)', {'size': 12, 'bold': True, 'color': WHITE})],
     [('€372–398 saved per tonne × 60–80 kt/yr EU export book — earned by filing verified data instead of EU defaults.', {'size': 8.4, 'color': MUTED})],
     [('The calculator IS the MRV instrument that produces the verified number.', {'size': 8.4, 'bold': True, 'color': TEAL})]],
    line_spacing=1.02, space_after=2)

# ---- band B ----
yB = yA + A_h + Inches(0.10); B_h = Inches(2.50)
# 08 validation
W08 = Inches(4.45)
yy = module(s, M, yB, W08, B_h, '08', 'TRIPLE VALIDATION', 'model vs world · fig 3.2', accent=GREEN)
txt(s, M+Inches(0.1), yy+Inches(0.01), Inches(4.2), Inches(0.16),
    [[('tCO₂/t vs scrap% — worldstainless benchmark curve', {'size': 7.2, 'color': FAINT})]])
cx0 = M+Inches(0.5); cy0 = yy+Inches(1.24); chh = Inches(0.88); chw = Inches(3.45)
vline(s, cx0, cy0-chh, chh, color=LINE); hline(s, cx0, cy0, chw, color=LINE)
pts = [(30,6.80),(50,3.70),(75,2.45),(85,1.95)]
maxv = 7.4
prev = None
for scrap,v in pts:
    px = cx0 + Emu(int(chw * (scrap-25)/65.0))
    pyy = cy0 - Emu(int(chh * v/maxv))
    if prev:
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, prev[0], prev[1], px, pyy)
        ln.line.color.rgb = TEAL; ln.line.width = Pt(1.4); ln.shadow.inherit = False
    box(s, px-Inches(0.03), pyy-Inches(0.03), Inches(0.06), Inches(0.06), fill=TEAL)
    txt(s, px+Inches(0.04), pyy-Inches(0.10), Inches(0.42), Inches(0.16),
        [[(f'{v}', {'size': 7.4, 'color': MUTED})]])
    txt(s, px-Inches(0.2), cy0+Inches(0.02), Inches(0.4), Inches(0.15),
        [[(f'{scrap}%', {'size': 7.4, 'color': FAINT})]], align=PP_ALIGN.CENTER)
    prev = (px, pyy)
jx = cx0 + Emu(int(chw * (70-25)/65.0)); jy = cy0 - Emu(int(chh * 3.03/maxv))
dj = s.shapes.add_shape(MSO_SHAPE.DIAMOND, jx-Inches(0.05), jy-Inches(0.05), Inches(0.10), Inches(0.10))
dj.fill.solid(); dj.fill.fore_color.rgb = AMBER; dj.line.color.rgb = WHITE; dj.line.width=Pt(0.9); dj.shadow.inherit=False
txt(s, jx-Inches(0.55), jy+Inches(0.09), Inches(1.2), Inches(0.16),
    [[('▴ JSL 3.03 @ 70%', {'size': 7.8, 'bold': True, 'color': AMBER})]], align=PP_ALIGN.CENTER)
vals = [('V1 audited anchor', 'model predicts 2.8–3.1 · JSL’s audited 3.03 lands inside'),
        ('V2 industry curve', 'JSL point sits on the ISSF benchmark line (chart above)'),
        ('V3 grade physics', 'Ni-free 430 ≈ half the 304 footprint — correctly reproduced')]
vy = cy0 + Inches(0.22)
for lab, det in vals:
    box(s, M+Inches(0.1), vy+Inches(0.015), Inches(0.04), Inches(0.15), fill=GREEN)
    txt(s, M+Inches(0.2), vy, W08-Inches(0.32), Inches(0.2),
        [[(lab+'   ', {'size': 8, 'bold': True, 'color': WHITE}), (det, {'size': 7.8, 'color': MUTED})]],
        line_spacing=0.92)
    vy += Inches(0.225)

# 09 INITIAL RECOMMENDATIONS
X09 = M + W08 + Inches(0.12); W09 = Inches(4.55)
yy = module(s, X09, yB, W09, B_h, '09', 'INITIAL RECOMMENDATIONS', 'R1–R4, priced and owned', accent=AMBER)
recs = [
    ('R1', TEAL,  'OPS',  'Push scrap 70→78% inside the 80% guardrail; deploy sensor-sorting to secure tramp-free feed.'),
    ('R2', AMBER, 'OPS',  'Lift renewables 47→65% via the 300 MW hybrid — captive coal at 1.045 t/MWh is the #2 lever.'),
    ('R3', GREEN, 'CFO',  'File verified MRV data with EU importers — €372–398/t dividend vs defaults; tool generates the filing.'),
    ('R4', BLUE,  'SALES','Ship a carbon certificate with every EU order — CPR GWP is mandatory since Jan 2026; DPP lands ~2028.'),
]
iy = yy + Inches(0.05)
for tag, cc, who, det in recs:
    box(s, X09+Inches(0.1), iy, Inches(0.40), Inches(0.40), fill=INK, line=cc, lw=1.1)
    txt(s, X09+Inches(0.1), iy+Inches(0.09), Inches(0.40), Inches(0.2),
        [[(tag, {'size': 9.5, 'bold': True, 'color': cc})]], align=PP_ALIGN.CENTER)
    txt(s, X09+Inches(0.58), iy-Inches(0.015), W09-Inches(0.75), Inches(0.48),
        [[(who+'  ', {'size': 7.6, 'bold': True, 'color': cc}),
          (det, {'size': 8, 'color': WHITE})]], line_spacing=0.94)
    iy += Inches(0.485)
txt(s, X09+Inches(0.1), iy+Inches(0.01), W09-Inches(0.2), Inches(0.2),
    [[('Combined effect: S1+2 → 1.35–1.45 by FY28-30 · on-track for FY35 −50% target.', {'size': 7.8, 'bold': True, 'color': GREEN})]])

# 10 roadmap
X10 = X09 + W09 + Inches(0.12); W10 = SW - X10 - M
yy = module(s, X10, yB, W10, B_h, '10', 'DEPLOYMENT ROADMAP', 'fig 3.3', accent=BLUE)
years = ['FY26','FY27','FY28','FY29','FY30']
gx0 = X10+Inches(1.06); gw = W10-Inches(1.24); colw = gw/5
for i,yr in enumerate(years):
    txt(s, gx0+colw*i, yy+Inches(0.0), colw, Inches(0.16),
        [[(yr, {'size': 7.2, 'color': FAINT})]], align=PP_ALIGN.CENTER)
    vline(s, gx0+colw*i, yy+Inches(0.18), Inches(1.52), color=LINE2)
tasks = [
    ('Live calculator', 0, 1, TEAL),
    ('Verified CBAM filing', 0, 2, GREEN),
    ('AI scrap sorting', 1, 2, AMBER),
    ('Biochar · slag→SCM', 2, 2, AMBER),
    ('Auto-DPP per heat', 3, 2, BLUE),
]
ty = yy + Inches(0.24)
for name, start, dur, cc in tasks:
    txt(s, X10+Inches(0.08), ty-Inches(0.01), Inches(0.98), Inches(0.28),
        [[(name, {'size': 7.2, 'color': WHITE})]], line_spacing=0.85)
    box(s, gx0+colw*start+Inches(0.02), ty+Inches(0.02), colw*dur-Inches(0.04), Inches(0.12), fill=cc)
    ty += Inches(0.30)
txt(s, X10+Inches(0.08), ty+Inches(0.03), W10-Inches(0.2), Inches(0.32),
    [[('Abatement cost: sorting $30–43 · biochar $29–45 per tCO₂ — every step beats the 2030 CBAM price of €109.', {'size': 7.4, 'color': MUTED, 'italic': True})]], line_spacing=0.92)

# ---- footer ----
fy = yB + B_h + Inches(0.07)
box(s, M, fy, SW-2*M, Inches(0.42), fill=INK, line=LINE, lw=0.75)
txt(s, M+Inches(0.1), fy+Inches(0.04), SW-2*M-Inches(0.2), Inches(0.36),
    [[('EVIDENCE TRAIL  ', {'size': 7.6, 'bold': True, 'color': AMBER}),
      ('every figure traces to a locked canonical model over 19 research files — factors (CEA v21.0 · BEE PAT · IPCC 2006 · ICDA) · methodology (ISSF/worldstainless · ISO 14404) · actuals (JSL BRSR · CDP · ESG FY22–26) · regulation (EU 2023/956 · 2025/2620-21 · CPR 2024/3110 · ESPR 2024/1781) · finance (Goldman · ICRA · CRISIL · GTRI)', {'size': 7.2, 'color': MUTED})],
     [('ACCOMPANYING THIS SUMMARY:  ', {'size': 7.4, 'bold': True, 'color': TEAL}),
      ('live web calculator [ADD LINK]  ·  full sourced research appendix [ADD LINK]', {'size': 7.4, 'color': WHITE})]],
    space_after=1.5)

out = r'C:\Users\Gaurav Agrawal\jindal-steel-case-study\case-study\StainlessCarbon_Round1.pptx'
prs.save(out)
print('saved', out)
