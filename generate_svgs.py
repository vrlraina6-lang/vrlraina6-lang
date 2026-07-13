#!/usr/bin/env python3
"""
Premium GitHub Profile README Hero Banner - 3D Edition
Pure SVG with SMIL animations, isometric 3D effects, no JavaScript
"""

def get_theme(mode):
    if mode == "dark":
        return {
            "bg": "#030712",
            "bg2": "#060d1f",
            "panel": "#0F172A",
            "panel2": "#0a1020",
            "border": "rgba(255,255,255,0.08)",
            "border_glow": "rgba(139,92,246,0.4)",
            "text": "#F8FAFC",
            "muted": "#94A3B8",
            "accent1": "#7C3AED",
            "accent2": "#22D3EE",
            "accent3": "#10B981",
            "accent4": "#F59E0B",
            "ascii_c1": "#06B6D4",
            "ascii_c2": "#8B5CF6",
            "ascii_c3": "#22D3EE",
            "glow1": "rgba(34,211,238,0.18)",
            "glow2": "rgba(124,58,237,0.18)",
            "glow3": "rgba(16,185,129,0.12)",
            "cube_face1": "rgba(124,58,237,0.25)",
            "cube_face2": "rgba(34,211,238,0.15)",
            "cube_face3": "rgba(16,185,129,0.10)",
            "cube_stroke": "rgba(139,92,246,0.6)",
            "grid_color": "rgba(139,92,246,0.12)",
            "grid_bright": "rgba(34,211,238,0.25)",
            "particle1": "#22D3EE",
            "particle2": "#8B5CF6",
            "particle3": "#10B981",
            "shadow": "rgba(0,0,0,0.8)",
            "glass_tint": "rgba(15,23,42,0.7)",
            "reflection": "rgba(255,255,255,0.03)",
            "scanline": "rgba(34,211,238,0.06)",
            "extrude": "rgba(124,58,237,0.4)",
            "mode_label": "DARK",
        }
    else:
        return {
            "bg": "#FFFFFF",
            "bg2": "#F1F5F9",
            "panel": "#F8FAFC",
            "panel2": "#EFF3F8",
            "border": "rgba(15,23,42,0.08)",
            "border_glow": "rgba(37,99,235,0.3)",
            "text": "#0F172A",
            "muted": "#475569",
            "accent1": "#2563EB",
            "accent2": "#06B6D4",
            "accent3": "#10B981",
            "accent4": "#D97706",
            "ascii_c1": "#2563EB",
            "ascii_c2": "#06B6D4",
            "ascii_c3": "#0EA5E9",
            "glow1": "rgba(37,99,235,0.10)",
            "glow2": "rgba(6,182,212,0.10)",
            "glow3": "rgba(16,185,129,0.08)",
            "cube_face1": "rgba(37,99,235,0.12)",
            "cube_face2": "rgba(6,182,212,0.10)",
            "cube_face3": "rgba(16,185,129,0.08)",
            "cube_stroke": "rgba(37,99,235,0.4)",
            "grid_color": "rgba(37,99,235,0.06)",
            "grid_bright": "rgba(6,182,212,0.15)",
            "particle1": "#06B6D4",
            "particle2": "#2563EB",
            "particle3": "#10B981",
            "shadow": "rgba(15,23,42,0.15)",
            "glass_tint": "rgba(248,250,252,0.7)",
            "reflection": "rgba(255,255,255,0.6)",
            "scanline": "rgba(37,99,235,0.04)",
            "extrude": "rgba(37,99,235,0.2)",
            "mode_label": "LIGHT",
        }


ascii_lines = [
    "  ________  ____  __   ___  ",
    " /  _____/ /    |/  | /   \\ ",
    "/   \\  ___|   __    |/ /^\\ \\",
    "\\    \\_\\  \\  |  \\   /  ___  \\ ",
    " \\______  /__|   \\__\\_/   \\__/",
    "        \\/  VRLRAINA           ",
    " ----------------------------  ",
    " [ Full Stack  AI  DevOps ]   ",
    " ----------------------------  ",
    "  > React   > Node  > Python  ",
    "  > Docker  > AWS   > TS      ",
    " ----------------------------  ",
    "  * Open Source Contributor   *",
    "  * AI Interface Builder      *",
    " ----------------------------  ",
    "  [ github.com/vrlraina6-lang ]",
]

titles = [
    "Full Stack Developer",
    "Frontend Engineer",
    "Open Source Contributor",
    "UI/UX Engineer",
    "AI Enthusiast",
]

skills_row1 = ["React", "Next.js", "Node.js", "TypeScript", "Tailwind"]
skills_row2 = ["Python", "Docker", "Postgres", "AWS", "Git", "Figma"]


def iso_point(x, y, z, ox=210, oy=80, scale=22):
    """Convert 3D isometric coordinates to 2D SVG coordinates"""
    sx = ox + (x - y) * scale * 0.866
    sy = oy + (x + y) * scale * 0.5 - z * scale
    return sx, sy


def cube_faces(cx, cy, cz, size, t):
    """Generate 3D cube SVG paths"""
    s = size
    # 8 corners
    pts = {}
    for dx in [0, 1]:
        for dy in [0, 1]:
            for dz in [0, 1]:
                px, py = iso_point(cx + dx * s, cy + dy * s, cz + dz * s)
                pts[(dx, dy, dz)] = (px, py)

    def p(dx, dy, dz):
        x, y = pts[(dx, dy, dz)]
        return f"{x:.1f},{y:.1f}"

    # Top face
    top = f"M{p(0,0,1)} L{p(1,0,1)} L{p(1,1,1)} L{p(0,1,1)} Z"
    # Left face
    left = f"M{p(0,0,0)} L{p(0,0,1)} L{p(0,1,1)} L{p(0,1,0)} Z"
    # Right face
    right = f"M{p(1,0,0)} L{p(1,0,1)} L{p(1,1,1)} L{p(1,1,0)} Z"
    # Front face
    front = f"M{p(0,1,0)} L{p(0,1,1)} L{p(1,1,1)} L{p(1,1,0)} Z"

    return top, left, right, front


def make_isometric_grid(t):
    lines = []
    # Draw isometric grid lines
    for i in range(0, 9):
        x0, y0 = iso_point(i, 0, 0, 0, 0, 28)
        x1, y1 = iso_point(i, 8, 0, 0, 0, 28)
        lines.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{t["grid_color"]}" stroke-width="1"/>')
        x0, y0 = iso_point(0, i, 0, 0, 0, 28)
        x1, y1 = iso_point(8, i, 0, 0, 0, 28)
        lines.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{t["grid_color"]}" stroke-width="1"/>')
    return "\n    ".join(lines)


def make_cube_svg(cx, cy, cz, size, t, delay=0, dur=8):
    top, left, right, front = cube_faces(cx, cy, cz, size, t)
    return f'''
    <g opacity="0.85">
        <path d="{top}" fill="{t['cube_face1']}" stroke="{t['cube_stroke']}" stroke-width="1.2">
            <animate attributeName="opacity" values="0.6;1;0.6" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
        </path>
        <path d="{left}" fill="{t['cube_face2']}" stroke="{t['cube_stroke']}" stroke-width="1.2">
            <animate attributeName="opacity" values="0.4;0.8;0.4" dur="{dur}s" begin="{delay+0.5}s" repeatCount="indefinite"/>
        </path>
        <path d="{right}" fill="{t['cube_face3']}" stroke="{t['cube_stroke']}" stroke-width="1.2">
            <animate attributeName="opacity" values="0.3;0.7;0.3" dur="{dur}s" begin="{delay+1}s" repeatCount="indefinite"/>
        </path>
    </g>'''


def make_orbiting_rings(cx, cy, t):
    return f'''
    <!-- Orbiting ring 1 - horizontal -->
    <ellipse cx="{cx}" cy="{cy}" rx="110" ry="35" fill="none"
             stroke="url(#ring_grad)" stroke-width="1.5" opacity="0.5"
             transform="rotate(-20 {cx} {cy})">
        <animateTransform attributeName="transform" type="rotate"
            values="-20 {cx} {cy}; 340 {cx} {cy}; -20 {cx} {cy}"
            dur="12s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.3;0.7;0.3" dur="6s" repeatCount="indefinite"/>
    </ellipse>
    <!-- Orbiting ring 2 - tilted -->
    <ellipse cx="{cx}" cy="{cy}" rx="90" ry="28" fill="none"
             stroke="url(#ring_grad2)" stroke-width="1" opacity="0.4"
             transform="rotate(60 {cx} {cy})">
        <animateTransform attributeName="transform" type="rotate"
            values="60 {cx} {cy}; 420 {cx} {cy}; 60 {cx} {cy}"
            dur="9s" repeatCount="indefinite"/>
    </ellipse>
    <!-- Orbiting ring 3 - vertical-ish -->
    <ellipse cx="{cx}" cy="{cy}" rx="70" ry="22" fill="none"
             stroke="url(#accent_grad)" stroke-width="0.8" opacity="0.3"
             transform="rotate(-70 {cx} {cy})">
        <animateTransform attributeName="transform" type="rotate"
            values="-70 {cx} {cy}; 290 {cx} {cy}; -70 {cx} {cy}"
            dur="15s" repeatCount="indefinite"/>
    </ellipse>

    <!-- Particle on ring 1 -->
    <circle r="4" fill="{t['accent2']}" opacity="0.9" filter="url(#glow_sm)">
        <animateMotion dur="12s" repeatCount="indefinite">
            <mpath href="#ring_path1"/>
        </animateMotion>
    </circle>
    <!-- Particle on ring 2 -->
    <circle r="3" fill="{t['accent1']}" opacity="0.8" filter="url(#glow_sm)">
        <animateMotion dur="9s" repeatCount="indefinite" begin="-3s">
            <mpath href="#ring_path2"/>
        </animateMotion>
    </circle>
    <!-- Particle on ring 3 -->
    <circle r="2.5" fill="{t['accent3']}" opacity="0.8" filter="url(#glow_sm)">
        <animateMotion dur="15s" repeatCount="indefinite" begin="-7s">
            <mpath href="#ring_path3"/>
        </animateMotion>
    </circle>'''


def generate_svg(mode):
    t = get_theme(mode)

    # Build ASCII lines SVG
    ascii_svg = ""
    for i, line in enumerate(ascii_lines):
        escaped = (line.replace("&", "&amp;").replace("<", "&lt;")
                      .replace(">", "&gt;").replace('"', "&quot;"))
        y = 20 + i * 26
        delay = 0.3 + i * 0.1
        ascii_svg += f'''
        <text x="10" y="{y}" font-family="monospace" font-size="13.5" font-weight="500"
              fill="url(#ascii_grad)" letter-spacing="0.5" opacity="0">
            {escaped}
            <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{delay}s" fill="freeze"/>
        </text>'''

    # Skills pills row 1
    pills1 = ""
    x = 0
    for i, skill in enumerate(skills_row1):
        w = len(skill) * 9 + 36
        delay = 3.5 + i * 0.12
        pills1 += f'''
        <g opacity="0" transform="translate({x},0)">
            <rect x="0" y="0" width="{w}" height="30" rx="15"
                  fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" opacity="0.6"/>
            <text x="{w/2}" y="20" font-family="system-ui,sans-serif" font-size="13"
                  fill="{t['accent2']}" font-weight="600" text-anchor="middle">{skill}</text>
            <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{delay}s" fill="freeze"/>
        </g>'''
        x += w + 10

    # Skills pills row 2
    pills2 = ""
    x = 0
    for i, skill in enumerate(skills_row2):
        w = len(skill) * 9 + 36
        delay = 4.2 + i * 0.12
        pills2 += f'''
        <g opacity="0" transform="translate({x},0)">
            <rect x="0" y="0" width="{w}" height="30" rx="15"
                  fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" opacity="0.6"/>
            <text x="{w/2}" y="20" font-family="system-ui,sans-serif" font-size="13"
                  fill="{t['accent3']}" font-weight="600" text-anchor="middle">{skill}</text>
            <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{delay}s" fill="freeze"/>
        </g>'''
        x += w + 10

    # Typing animation — multiple title blocks
    timeline = sum(len(tt) * 0.08 + 1.8 for tt in titles)
    typing_blocks = ""
    cur = 0
    for i, title in enumerate(titles):
        t_len = len(title) * 0.08
        t_hold = 1.5
        t_out  = 0.3
        total  = t_len + t_hold + t_out
        s0 = cur / timeline
        s1 = (cur + t_len) / timeline
        s2 = (cur + t_len + t_hold) / timeline
        s3 = (cur + total) / timeline
        max_w = len(title) * 14
        typing_blocks += f'''
        <g opacity="0">
            <clipPath id="tc{i}">
                <rect x="0" y="-22" width="0" height="28">
                    <animate attributeName="width" from="0" to="{max_w}" dur="{t_len}s"
                        begin="{cur}s" fill="freeze" repeatCount="1"/>
                    <animate attributeName="width" from="{max_w}" to="{max_w}" dur="{t_hold}s"
                        begin="{cur+t_len}s" fill="freeze" repeatCount="1"/>
                    <animate attributeName="width" from="{max_w}" to="0" dur="{t_out}s"
                        begin="{cur+t_len+t_hold}s" fill="freeze" repeatCount="1"/>
                </rect>
            </clipPath>
            <text x="0" y="0" font-family="monospace" font-size="19" font-weight="700"
                  fill="url(#accent_grad)" clip-path="url(#tc{i})">{title}</text>
            <animate attributeName="opacity" values="0;1;1;0;0"
                keyTimes="0;{max(0.001,s0):.4f};{s2:.4f};{s3:.4f};1"
                dur="{timeline:.1f}s" repeatCount="indefinite"/>
        </g>'''
        cur += total

    # Info items
    info = [
        ("📍", t["accent1"], "San Francisco, CA"),
        ("🎓", t["accent2"], "B.S. in Computer Science"),
        ("🚀", t["accent3"], "Building next-gen AI interfaces"),
        ("🔗", t["accent1"], "github.com/vrlraina6-lang"),
        ("✉️", t["accent2"], "hello@vrlraina.dev"),
    ]
    info_svg = ""
    for i, (icon, color, text) in enumerate(info):
        delay = 2.2 + i * 0.3
        y = i * 38
        info_svg += f'''
        <g opacity="0" transform="translate(0,{y})">
            <text x="0" y="0" font-size="16">{icon}</text>
            <text x="32" y="0" font-family="system-ui,sans-serif" font-size="15"
                  font-weight="500" fill="{t['muted']}">{text}</text>
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze"/>
            <animateTransform attributeName="transform" type="translate"
                values="0,{y+8};0,{y}" dur="0.5s" begin="{delay}s" fill="freeze"/>
        </g>'''

    # 3D Cubes isometric
    cubes_svg = make_cube_svg(0, 0, 0, 1.8, t, 0, 6)
    cubes_svg += make_cube_svg(2.5, 0, 0, 1.2, t, 0.5, 7)
    cubes_svg += make_cube_svg(0, 2.5, 0, 1.0, t, 1.0, 5)
    cubes_svg += make_cube_svg(2.5, 2.5, 0, 1.5, t, 1.5, 8)
    cubes_svg += make_cube_svg(1.2, 1.2, 1.8, 1.0, t, 0.8, 9)

    # Orbiting rings center
    rings_svg = make_orbiting_rings(210, 285, t)

    # Particles background
    particles = ""
    pdata = [
        (120, 80, 2, t["particle1"], "3.2s", "0s"),
        (340, 180, 1.5, t["particle2"], "4.1s", "-1s"),
        (80, 400, 2.5, t["particle3"], "5.0s", "-2s"),
        (380, 480, 1.8, t["particle1"], "3.7s", "-0.5s"),
        (200, 540, 1.2, t["particle2"], "4.5s", "-1.5s"),
        (900, 100, 2, t["particle3"], "3.9s", "-0.8s"),
        (1100, 300, 1.5, t["particle1"], "5.2s", "-2.5s"),
        (1050, 550, 2, t["particle2"], "4.0s", "-1.2s"),
        (750, 550, 1.8, t["particle3"], "6.0s", "-3s"),
        (650, 80, 1.2, t["particle1"], "3.5s", "-0.3s"),
    ]
    for px, py, pr, pc, dur, beg in pdata:
        particles += f'''
        <circle cx="{px}" cy="{py}" r="{pr}" fill="{pc}" filter="url(#glow_sm)">
            <animate attributeName="opacity" values="0.1;0.9;0.1" dur="{dur}" begin="{beg}" repeatCount="indefinite"/>
            <animate attributeName="cy" values="{py};{py-15};{py}" dur="{dur}" begin="{beg}" repeatCount="indefinite"/>
        </circle>'''

    svg = f'''<svg width="1180" height="610" viewBox="0 0 1180 610"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">

  <defs>
    <!-- Gradients -->
    <linearGradient id="bg_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['bg']}"/>
      <stop offset="100%" stop-color="{t['bg2']}"/>
    </linearGradient>

    <linearGradient id="accent_grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['accent1']}">
        <animate attributeName="stop-color"
          values="{t['accent1']};{t['accent2']};{t['accent3']};{t['accent1']}"
          dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="{t['accent2']}">
        <animate attributeName="stop-color"
          values="{t['accent2']};{t['accent3']};{t['accent1']};{t['accent2']}"
          dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{t['accent3']}">
        <animate attributeName="stop-color"
          values="{t['accent3']};{t['accent1']};{t['accent2']};{t['accent3']}"
          dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="ascii_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['ascii_c1']}">
        <animate attributeName="stop-color"
          values="{t['ascii_c1']};{t['ascii_c2']};{t['ascii_c3']};{t['ascii_c1']}"
          dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{t['ascii_c2']}">
        <animate attributeName="stop-color"
          values="{t['ascii_c2']};{t['ascii_c3']};{t['ascii_c1']};{t['ascii_c2']}"
          dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="ring_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{t['accent1']}" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="ring_grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['accent3']}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="panel_left_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['panel']}" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="{t['panel2']}" stop-opacity="0.85"/>
    </linearGradient>

    <linearGradient id="panel_right_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['panel']}" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="{t['panel2']}" stop-opacity="0.80"/>
    </linearGradient>

    <linearGradient id="shimmer_grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="transparent"/>
      <stop offset="40%" stop-color="{t['reflection']}">
        <animate attributeName="offset" values="0%;50%;100%" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="transparent"/>
    </linearGradient>

    <linearGradient id="text_extrude" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{t['accent1']}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{t['extrude']}" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="glow_blue" cx="30%" cy="35%" r="45%">
      <stop offset="0%" stop-color="{t['glow1']}"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>
    <radialGradient id="glow_purple" cx="75%" cy="65%" r="45%">
      <stop offset="0%" stop-color="{t['glow2']}"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>
    <radialGradient id="glow_emerald" cx="50%" cy="90%" r="40%">
      <stop offset="0%" stop-color="{t['glow3']}"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>

    <radialGradient id="spot_left" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>
    <radialGradient id="spot_right" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t['accent1']}" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="transparent"/>
    </radialGradient>

    <!-- Filters -->
    <filter id="blur_heavy" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="45"/>
    </filter>
    <filter id="blur_med" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="20"/>
    </filter>
    <filter id="glow_sm" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow_lg" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="drop_shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="{t['shadow']}" flood-opacity="0.6"/>
    </filter>
    <filter id="inner_shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4" result="blur"/>
      <feOffset dx="0" dy="2" result="offsetBlur"/>
      <feComposite in="SourceGraphic" in2="offsetBlur" operator="over"/>
    </filter>

    <!-- Clip Paths -->
    <clipPath id="main_clip">
      <rect width="1180" height="610" rx="28"/>
    </clipPath>
    <clipPath id="left_clip">
      <rect width="420" height="570" rx="20"/>
    </clipPath>
    <clipPath id="right_clip">
      <rect width="720" height="570" rx="20"/>
    </clipPath>
    <clipPath id="ascii_clip">
      <rect x="0" y="0" width="400" height="0">
        <animate attributeName="height" from="0" to="450" dur="2s" fill="freeze"/>
      </rect>
    </clipPath>

    <!-- 3D Ring motion paths -->
    <path id="ring_path1" d="M 100,285 A 110,35 0 1,1 319,285 A 110,35 0 1,1 100,285"
          transform="rotate(-20 210 285)"/>
    <path id="ring_path2" d="M 120,285 A 90,28 0 1,1 299,285 A 90,28 0 1,1 120,285"
          transform="rotate(60 210 285)"/>
    <path id="ring_path3" d="M 140,285 A 70,22 0 1,1 279,285 A 70,22 0 1,1 140,285"
          transform="rotate(-70 210 285)"/>

    <!-- Noise texture pattern -->
    <filter id="noise_filter">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
      <feBlend in="SourceGraphic" mode="overlay" result="blend"/>
      <feComposite in="blend" in2="SourceGraphic" operator="in"/>
    </filter>
  </defs>

  <!-- ═══════════════════════════════════════════════════ -->
  <!--  BACKGROUND                                        -->
  <!-- ═══════════════════════════════════════════════════ -->
  <g clip-path="url(#main_clip)">
    <rect width="1180" height="610" fill="url(#bg_grad)"/>

    <!-- Ambient glow orbs -->
    <ellipse cx="300" cy="200" rx="350" ry="250" fill="url(#glow_blue)" filter="url(#blur_heavy)">
      <animate attributeName="cx" values="300;380;300" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="200;260;200" dur="10s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="900" cy="400" rx="320" ry="220" fill="url(#glow_purple)" filter="url(#blur_heavy)">
      <animate attributeName="cx" values="900;820;900" dur="13s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="400;340;400" dur="13s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="600" cy="550" rx="280" ry="180" fill="url(#glow_emerald)" filter="url(#blur_heavy)">
      <animate attributeName="cx" values="600;680;600" dur="11s" repeatCount="indefinite"/>
    </ellipse>

    <!-- Animated particles -->
    {particles}

    <!-- ══════════════════════════════════════════════════ -->
    <!--  LEFT PANEL — 3D ASCII + Rings                   -->
    <!-- ══════════════════════════════════════════════════ -->
    <g transform="translate(20,20)" filter="url(#drop_shadow)">

      <!-- Panel glass bg -->
      <rect width="420" height="570" rx="20" fill="url(#panel_left_grad)"/>

      <!-- Spot glow inside panel -->
      <rect width="420" height="570" rx="20" fill="url(#spot_left)" opacity="0.8"/>

      <!-- Border -->
      <rect width="420" height="570" rx="20" fill="none"
            stroke="url(#accent_grad)" stroke-width="1.5" opacity="0.25">
        <animate attributeName="opacity" values="0.15;0.5;0.15" dur="4s" repeatCount="indefinite"/>
      </rect>

      <!-- Shimmer overlay -->
      <rect width="420" height="570" rx="20" fill="url(#shimmer_grad)" opacity="0.5"/>

      <!-- Inner content clip -->
      <g clip-path="url(#left_clip)">

        <!-- Scanline sweep -->
        <rect x="0" y="-4" width="420" height="3" fill="{t['accent2']}" opacity="0.25">
          <animate attributeName="y" values="-4;574;-4" dur="5s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.05;0.4;0.05" dur="5s" repeatCount="indefinite"/>
        </rect>

        <!-- 3D Isometric background grid (bottom) -->
        <g transform="translate(15,330)" opacity="0.6">
          {make_isometric_grid(t)}
        </g>

        <!-- 3D Orbiting rings (center visual) -->
        {rings_svg}

        <!-- 3D Floating cubes -->
        <g transform="translate(25,340)">
          {cubes_svg}
        </g>

        <!-- Terminal dots -->
        <circle cx="22" cy="22" r="6" fill="#EF4444" opacity="0.9"/>
        <circle cx="44" cy="22" r="6" fill="#EAB308" opacity="0.9"/>
        <circle cx="66" cy="22" r="6" fill="#22C55E" opacity="0.9"/>
        <text x="88" y="27" font-family="monospace" font-size="11" fill="{t['muted']}"
              opacity="0.6">bash — vrlraina6-lang</text>

        <!-- Divider -->
        <line x1="15" y1="40" x2="405" y2="40" stroke="{t['border']}" stroke-width="1"/>

        <!-- ASCII Art (3D floating effect) -->
        <g clip-path="url(#ascii_clip)">
          <g>
            <animateTransform attributeName="transform" type="translate"
              values="0,0;0,-6;0,0" dur="7s" repeatCount="indefinite"/>
            {ascii_svg}
          </g>
        </g>

        <!-- Blinking cursor after ASCII -->
        <rect x="12" y="430" width="9" height="16" rx="1" fill="{t['accent2']}" opacity="1">
          <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
        </rect>

        <!-- Noise overlay -->
        <rect width="420" height="570" fill="transparent" filter="url(#noise_filter)" opacity="0.04"/>
      </g>
    </g>

    <!-- ══════════════════════════════════════════════════ -->
    <!--  RIGHT PANEL — Terminal Info                     -->
    <!-- ══════════════════════════════════════════════════ -->
    <g transform="translate(460,20)" filter="url(#drop_shadow)">

      <!-- Panel glass bg -->
      <rect width="700" height="570" rx="20" fill="url(#panel_right_grad)"/>

      <!-- Spot glow -->
      <rect width="700" height="570" rx="20" fill="url(#spot_right)" opacity="0.7"/>

      <!-- Border -->
      <rect width="700" height="570" rx="20" fill="none"
            stroke="url(#accent_grad)" stroke-width="1.5" opacity="0.2">
        <animate attributeName="opacity" values="0.1;0.4;0.1" dur="5s" begin="-2s" repeatCount="indefinite"/>
      </rect>

      <!-- Shimmer -->
      <rect width="700" height="570" rx="20" fill="url(#shimmer_grad)" opacity="0.4"/>

      <g clip-path="url(#right_clip)">

        <!-- Scanline -->
        <rect x="0" y="-4" width="700" height="2" fill="{t['accent1']}" opacity="0.15">
          <animate attributeName="y" values="-4;574;-4" dur="7s" begin="-3s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.05;0.25;0.05" dur="7s" begin="-3s" repeatCount="indefinite"/>
        </rect>

        <!-- Terminal dots -->
        <circle cx="22" cy="22" r="6" fill="#EF4444" opacity="0.9"/>
        <circle cx="44" cy="22" r="6" fill="#EAB308" opacity="0.9"/>
        <circle cx="66" cy="22" r="6" fill="#22C55E" opacity="0.9"/>
        <text x="88" y="27" font-family="monospace" font-size="11" fill="{t['muted']}"
              opacity="0.6">profile.tsx — developer</text>

        <!-- Divider -->
        <line x1="15" y1="40" x2="685" y2="40" stroke="{t['border']}" stroke-width="1"/>

        <!-- Content area -->
        <g transform="translate(45,65)">

          <!-- Greeting -->
          <text x="0" y="0" font-family="system-ui,sans-serif" font-size="26"
                font-weight="500" fill="{t['text']}" opacity="0">
            Hi 👋
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.3s" fill="freeze"/>
          </text>

          <!-- 3D Extruded Name -->
          <!-- Shadow/extrude layers -->
          <text x="3" y="60" font-family="system-ui,sans-serif" font-size="52"
                font-weight="800" fill="{t['extrude']}" opacity="0" letter-spacing="-1">
            I'm VRLRAINA
            <animate attributeName="opacity" values="0;0.6" dur="0.5s" begin="0.8s" fill="freeze"/>
          </text>
          <text x="2" y="59" font-family="system-ui,sans-serif" font-size="52"
                font-weight="800" fill="{t['extrude']}" opacity="0" letter-spacing="-1">
            I'm VRLRAINA
            <animate attributeName="opacity" values="0;0.4" dur="0.5s" begin="0.8s" fill="freeze"/>
          </text>
          <!-- Main name with gradient -->
          <text x="0" y="57" font-family="system-ui,sans-serif" font-size="52"
                font-weight="800" fill="url(#accent_grad)" opacity="0"
                letter-spacing="-1" filter="url(#glow_sm)">
            I'm VRLRAINA
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.8s" fill="freeze"/>
          </text>

          <!-- Typing text row -->
          <g transform="translate(0,90)">
            <text x="0" y="0" font-family="monospace" font-size="16"
                  font-weight="500" fill="{t['muted']}" opacity="0">
              &gt;_
              <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.5s" fill="freeze"/>
            </text>
            <g transform="translate(28,0)">
              {typing_blocks}
              <!-- Blinking cursor -->
              <rect x="0" y="-19" width="10" height="22" rx="1" fill="{t['accent1']}">
                <animate attributeName="opacity" values="1;0;1" dur="0.75s" repeatCount="indefinite"/>
              </rect>
            </g>
          </g>

          <!-- Divider line -->
          <line x1="0" y1="122" x2="610" y2="122" stroke="{t['border']}" stroke-width="1" opacity="0">
            <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2s" fill="freeze"/>
          </line>

          <!-- Info items -->
          <g transform="translate(0,140)">
            {info_svg}
          </g>

          <!-- Skills section -->
          <g transform="translate(0,355)">
            <text x="0" y="0" font-family="system-ui,sans-serif" font-size="11"
                  font-weight="700" fill="{t['muted']}" letter-spacing="2" opacity="0">
              TECH STACK
              <animate attributeName="opacity" values="0;1" dur="0.4s" begin="3.3s" fill="freeze"/>
            </text>

            <line x1="90" y1="-4" x2="610" y2="-4" stroke="{t['border']}" stroke-width="1" opacity="0">
              <animate attributeName="opacity" values="0;0.8" dur="0.4s" begin="3.3s" fill="freeze"/>
            </line>

            <g transform="translate(0,14)">
              {pills1}
            </g>
            <g transform="translate(0,54)">
              {pills2}
            </g>
          </g>

          <!-- Social Icons Row -->
          <g transform="translate(0,465)">

            <!-- GitHub -->
            <g opacity="0" filter="url(#glow_sm)">
              <rect x="0" y="0" width="40" height="40" rx="10"
                    fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" stroke-opacity="0.5"/>
              <path transform="translate(8,8)" d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"
                    fill="{t['text']}" opacity="0.85"/>
              <animate attributeName="opacity" values="0;1" dur="0.4s" begin="4.5s" fill="freeze"/>
            </g>

            <!-- LinkedIn -->
            <g transform="translate(55,0)" opacity="0" filter="url(#glow_sm)">
              <rect x="0" y="0" width="40" height="40" rx="10"
                    fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" stroke-opacity="0.5"/>
              <path transform="translate(8,8)" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"
                    fill="{t['accent1']}" opacity="0.9"/>
              <animate attributeName="opacity" values="0;1" dur="0.4s" begin="4.7s" fill="freeze"/>
            </g>

            <!-- Twitter/X -->
            <g transform="translate(110,0)" opacity="0" filter="url(#glow_sm)">
              <rect x="0" y="0" width="40" height="40" rx="10"
                    fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" stroke-opacity="0.5"/>
              <path transform="translate(8,8)" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.748l7.73-8.835L1.254 2.25H8.08l4.259 5.63zm-1.161 17.52h1.833L7.084 4.126H5.117z"
                    fill="{t['text']}" opacity="0.85"/>
              <animate attributeName="opacity" values="0;1" dur="0.4s" begin="4.9s" fill="freeze"/>
            </g>

            <!-- Portfolio -->
            <g transform="translate(165,0)" opacity="0" filter="url(#glow_sm)">
              <rect x="0" y="0" width="40" height="40" rx="10"
                    fill="{t['panel']}" stroke="url(#accent_grad)" stroke-width="1" stroke-opacity="0.5"/>
              <path transform="translate(8,8)" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"
                    fill="{t['accent3']}" opacity="0.9"/>
              <animate attributeName="opacity" values="0;1" dur="0.4s" begin="5.1s" fill="freeze"/>
            </g>

            <!-- Label -->
            <text x="230" y="26" font-family="system-ui,sans-serif" font-size="12"
                  fill="{t['muted']}" font-weight="500" opacity="0">
              @vrlraina6-lang
              <animate attributeName="opacity" values="0;0.7" dur="0.4s" begin="5.3s" fill="freeze"/>
            </text>
          </g>

        </g>

        <!-- Noise overlay -->
        <rect width="700" height="570" fill="transparent" filter="url(#noise_filter)" opacity="0.03"/>
      </g>
    </g>

    <!-- ══════════════════════════════════════════════════ -->
    <!--  OUTER BORDER SHIMMER                            -->
    <!-- ══════════════════════════════════════════════════ -->
    <rect x="1" y="1" width="1178" height="608" rx="27" fill="none"
          stroke="url(#accent_grad)" stroke-width="1.5" opacity="0.15">
      <animate attributeName="opacity" values="0.08;0.3;0.08" dur="6s" repeatCount="indefinite"/>
    </rect>

  </g>
</svg>'''
    return svg


if __name__ == "__main__":
    for mode in ("dark", "light"):
        svg = generate_svg(mode)
        path = f"C:\\Users\\user\\.gemini\\antigravity\\scratch\\github-banner\\{mode}.svg"
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"[OK] {mode}.svg generated ({len(svg)//1024}KB)")
    print("[DONE] All done!")
