import os

def get_theme(mode):
    if mode == "dark":
        return {
            "bg": "#030712",
            "panel": "#0F172A",
            "border": "rgba(255,255,255,0.08)",
            "text": "#F8FAFC",
            "muted": "#94A3B8",
            "accent1": "#7C3AED",
            "accent2": "#22D3EE",
            "accent3": "#10B981",
            "ascii_grad1": "#06B6D4",
            "ascii_grad2": "#8B5CF6",
            "glow1": "rgba(34,211,238,0.2)",
            "glow2": "rgba(124,58,237,0.2)",
            "glow3": "rgba(16,185,129,0.2)",
        }
    else:
        return {
            "bg": "#FFFFFF",
            "panel": "#F8FAFC",
            "border": "rgba(15,23,42,0.08)",
            "text": "#0F172A",
            "muted": "#475569",
            "accent1": "#2563EB",
            "accent2": "#06B6D4",
            "accent3": "#10B981",
            "ascii_grad1": "#2563EB",
            "ascii_grad2": "#06B6D4",
            "glow1": "rgba(37,99,235,0.15)",
            "glow2": "rgba(6,182,212,0.15)",
            "glow3": "rgba(16,185,129,0.15)",
        }

ascii_portrait = [
    r"      _,.-------.,_       ",
    r"    ,;~'             '~;, ",
    r"  ,;                     ;,",
    r" ;                         ;",
    r",'                         ',",
    r",;                           ;,",
    r"; ;      .           .      ; ;",
    r"| ;   ______       ______   ; |",
    r"|  `/~\"     ~\" . \"~     \"~\\'  |",
    r"|  ~  ,-~~~^~, | ,~^~~~-,  ~  |",
    r" |   |        }:{        |   | ",
    r" |   l       / | \\       !   | ",
    r" .~  (__,.--\" .^. \"--.,__)  ~. ",
    r" |     ---;' / | \\ `;---     | ",
    r"  \\__.       \\/^\\/       .__/  ",
    r"   V| \\                 / |V   ",
    r"    | |T~\\___!___!___/~T| |    ",
    r"    | |`IIII_I_I_I_IIII'| |    ",
    r"    |  \\,III I I I III,/  |    ",
    r"     \\   `~~~~~~~~~~'    /     ",
    r"       \\   .       .   /       ",
    r"         \\.    ^    ./         ",
    r"           ^~~~^~~~^           "
]

def generate_svg(mode):
    t = get_theme(mode)
    
    # Render ASCII
    ascii_html = ""
    for i, line in enumerate(ascii_portrait):
        # Escape for XML
        line_esc = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")
        # Replace spaces with non-breaking spaces for preserving layout in svg text
        line_esc = line_esc.replace(" ", "&#160;")
        y_pos = i * 16 + 20
        ascii_html += f'<text x="20" y="{y_pos}" font-family="monospace" font-size="14" fill="url(#ascii_gradient)">{line_esc}</text>\n'

    pills = [
        "React", "Next.js", "Node.js", "TypeScript", 
        "Tailwind", "Python", "Docker", "Postgres", 
        "AWS", "Git", "Figma"
    ]
    
    # Calculate pill layout
    pill_html = ""
    pill_x = 0
    pill_y = 0
    max_w = 600
    for i, pill in enumerate(pills):
        width = len(pill) * 9 + 40
        if pill_x + width > max_w:
            pill_x = 0
            pill_y += 45
            
        pill_html += f'''
        <g class="pill" transform="translate({pill_x}, {pill_y})" style="opacity: 0">
            <rect x="0" y="0" width="{width}" height="32" rx="16" fill="{t['panel']}" stroke="{t['border']}" stroke-width="1"/>
            <text x="{width/2}" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="{t['muted']}" font-weight="500" text-anchor="middle">{pill}</text>
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{3.5 + i*0.1}s" fill="freeze" />
        </g>
        '''
        pill_x += width + 12

    titles = ["Frontend Engineer", "Full Stack Developer", "Open Source Contributor", "UI Engineer", "AI Enthusiast"]
    typing_html = ""
    total_time = 0
    char_width = 11.5
    for i, title in enumerate(titles):
        duration = len(title) * 0.1
        delay = total_time
        typing_html += f'''
        <text x="0" y="0" font-family="monospace" font-size="20" font-weight="600" fill="url(#accent_gradient)" opacity="0">
            {title}
            <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0; {0.05/(duration+1+0.05)}; {(duration+1)/(duration+1+0.05)}; {(duration+1+0.05)/(duration+1+0.05)}; 1" dur="{duration+1+0.05}s" begin="{delay}s" repeatCount="indefinite" />
            <animate attributeName="clip-path" values="url(#clip-0);url(#clip-{len(title)})" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
        </text>
        '''
        # Actually standard SMIL doesn't let us easily chain them in a single repeating block cleanly without a long timeline.
        # Let's use a single text block and animate clip-path for typing.
        # Wait, if we just want one string to type, it's easier. The prompt asks for multiple strings.
        # Let's build a timeline for multiple strings.
    
    # We need a proper continuous timeline for typing.
    timeline_duration = sum(len(title)*0.1 + 1.5 for title in titles)
    typing_html = ""
    curr_time = 0
    for i, title in enumerate(titles):
        title_time = len(title) * 0.1
        start_pct = curr_time / timeline_duration
        full_pct = (curr_time + title_time) / timeline_duration
        hold_pct = (curr_time + title_time + 1.2) / timeline_duration
        end_pct = (curr_time + title_time + 1.5) / timeline_duration
        
        # Clip path animation for this text
        typing_html += f'''
        <g opacity="0">
            <text x="0" y="0" font-family="monospace" font-size="20" font-weight="600" fill="url(#accent_gradient)">{title}</text>
            <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;{max(0.001, start_pct)};{hold_pct};{end_pct};1" dur="{timeline_duration}s" repeatCount="indefinite" />
            <animate attributeName="clip-path" values="url(#clip-type-0);url(#clip-type-{len(title)})" keyTimes="0;1" dur="{title_time}s" begin="{curr_time}s" repeatCount="indefinite" />
            <!-- Note: SMIL is tricky with animating clip-path inside an opacity animation if they don't share the same duration. 
                 Alternative: just use clip-path on the text itself, animating rect width. -->
        </g>
        '''
        curr_time += title_time + 1.5
        
    # Better Typing Animation:
    # We create a single clip path that resizes, and we animate the text content? No, SVG doesn't animate text content.
    # We will just show/hide each text, and animate its clip-path.
    typing_blocks = ""
    curr_t = 0
    for i, title in enumerate(titles):
        t_len = len(title) * 0.1
        t_hold = 1.5
        t_out = 0.2
        t_total = t_len + t_hold + t_out
        
        # A rect that covers the text to reveal it (clip-path is tricky to animate across browsers). 
        # Better: use a solid rect that uncovers the text by shrinking, but background is gradient so it doesn't work well.
        # Let's stick to `<clipPath>` and animate `<rect width="...">` inside it.
        # But we need one clip path per text, or we just animate a `<rect>` in one clip path and use it for all.
        typing_blocks += f'''
        <g>
            <!-- Show only during its time window -->
            <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0; {curr_t/timeline_duration}; {(curr_t+t_len+t_hold-0.1)/timeline_duration}; {(curr_t+t_total)/timeline_duration}; 1" dur="{timeline_duration}s" repeatCount="indefinite" />
            
            <clipPath id="typing-clip-{i}">
                <rect x="0" y="-20" width="0" height="30">
                    <animate attributeName="width" values="0;{len(title)*13};{len(title)*13}" keyTimes="0; {t_len/(t_len+t_hold+t_out)}; 1" dur="{t_len+t_hold+t_out}s" begin="{curr_t}s" repeatCount="indefinite" />
                </rect>
            </clipPath>
            
            <text x="0" y="0" font-family="monospace" font-size="20" font-weight="600" fill="url(#accent_gradient)" clip-path="url(#typing-clip-{i})">{title}</text>
        </g>
        '''
        curr_t += t_total

    svg_content = f'''<svg width="1180" height="610" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            * {{
                font-family: system-ui, -apple-system, sans-serif;
            }}
            
            .ascii {{
                font-family: monospace;
            }}
            
            .pill {{
                transition: all 0.3s ease;
                cursor: pointer;
            }}
            
            .pill:hover rect {{
                stroke: {t['accent1']};
                fill: rgba(124, 58, 237, 0.1);
                filter: drop-shadow(0 0 8px {t['accent1']});
                transform: scale(1.05) translateX(-2.5%) translateY(-2.5%);
            }}
            .pill:hover text {{
                fill: {t['accent1']};
            }}

            .social-icon {{
                transition: all 0.3s ease;
                cursor: pointer;
            }}
            .social-icon:hover {{
                transform: translateY(-3px);
                filter: drop-shadow(0 0 10px {t['accent2']});
            }}
            .social-icon:hover path {{
                fill: {t['accent2']};
            }}

            @keyframes float {{
                0% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-10px); }}
                100% {{ transform: translateY(0px); }}
            }}
            
            .floating {{
                animation: float 6s ease-in-out infinite;
            }}
            
            @keyframes pulse-glow {{
                0% {{ opacity: 0.5; transform: scale(1); }}
                50% {{ opacity: 0.8; transform: scale(1.05); }}
                100% {{ opacity: 0.5; transform: scale(1); }}
            }}
            
            .glow-bg {{
                animation: pulse-glow 8s ease-in-out infinite alternate;
            }}
            
            @keyframes scanline {{
                0% {{ transform: translateY(-100%); }}
                100% {{ transform: translateY(610px); }}
            }}
            
            .scanline {{
                animation: scanline 4s linear infinite;
            }}
            
            @keyframes shimmer {{
                0% {{ stop-color: rgba(255,255,255,0.05); }}
                50% {{ stop-color: rgba(255,255,255,0.2); }}
                100% {{ stop-color: rgba(255,255,255,0.05); }}
            }}
        </style>
        
        <linearGradient id="accent_gradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{t['accent1']}">
                <animate attributeName="stop-color" values="{t['accent1']};{t['accent2']};{t['accent1']}" dur="4s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{t['accent2']}">
                <animate attributeName="stop-color" values="{t['accent2']};{t['accent3']};{t['accent2']}" dur="4s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{t['accent3']}">
                <animate attributeName="stop-color" values="{t['accent3']};{t['accent1']};{t['accent3']}" dur="4s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="ascii_gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{t['ascii_grad1']}">
                <animate attributeName="stop-color" values="{t['ascii_grad1']};{t['ascii_grad2']};{t['ascii_grad1']}" dur="5s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{t['ascii_grad2']}">
                <animate attributeName="stop-color" values="{t['ascii_grad2']};{t['ascii_grad1']};{t['ascii_grad2']}" dur="5s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <radialGradient id="glow_blue" cx="30%" cy="30%" r="50%">
            <stop offset="0%" stop-color="{t['glow1']}" />
            <stop offset="100%" stop-color="transparent" />
        </radialGradient>
        
        <radialGradient id="glow_purple" cx="70%" cy="70%" r="50%">
            <stop offset="0%" stop-color="{t['glow2']}" />
            <stop offset="100%" stop-color="transparent" />
        </radialGradient>
        
        <radialGradient id="glow_emerald" cx="50%" cy="100%" r="50%">
            <stop offset="0%" stop-color="{t['glow3']}" />
            <stop offset="100%" stop-color="transparent" />
        </radialGradient>
        
        <filter id="blur_bg" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="40" />
        </filter>
        
        <filter id="glass_blur">
            <feGaussianBlur stdDeviation="10" />
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.8"/>
            </feComponentTransfer>
        </filter>
        
        <clipPath id="left_panel_clip">
            <rect width="420" height="570" rx="24" />
        </clipPath>
        
        <clipPath id="right_panel_clip">
            <rect width="700" height="570" rx="24" />
        </clipPath>

        <clipPath id="ascii_reveal">
            <rect x="0" y="0" width="420" height="0">
                <animate attributeName="height" values="0; 570" dur="2s" fill="freeze" />
            </rect>
        </clipPath>
    </defs>

    <!-- Main Background -->
    <rect width="1180" height="610" rx="32" fill="{t['bg']}" />
    
    <!-- Ambient Glows -->
    <rect class="glow-bg" x="0" y="0" width="1180" height="610" fill="url(#glow_blue)" filter="url(#blur_bg)" />
    <rect class="glow-bg" x="0" y="0" width="1180" height="610" fill="url(#glow_purple)" filter="url(#blur_bg)" style="animation-delay: -2s;" />
    <rect class="glow-bg" x="0" y="0" width="1180" height="610" fill="url(#glow_emerald)" filter="url(#blur_bg)" style="animation-delay: -4s;" />
    
    <!-- Particles (Stars) -->
    <g opacity="0.4">
        <!-- Let's put a few particles -->
        <circle cx="100" cy="100" r="1.5" fill="#fff"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="3s" repeatCount="indefinite" /></circle>
        <circle cx="300" cy="400" r="2" fill="#fff"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="4s" repeatCount="indefinite" /></circle>
        <circle cx="800" cy="150" r="1" fill="#fff"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="2.5s" repeatCount="indefinite" /></circle>
        <circle cx="1050" cy="500" r="2.5" fill="#fff"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="5s" repeatCount="indefinite" /></circle>
        <circle cx="600" cy="550" r="1.5" fill="#fff"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="3.5s" repeatCount="indefinite" /></circle>
    </g>

    <!-- Left Panel (ASCII Portrait) 38% approx = 420px out of 1140 total available width -->
    <g transform="translate(20, 20)">
        <!-- Glass Background -->
        <rect width="420" height="570" rx="24" fill="{t['panel']}" fill-opacity="0.6" stroke="{t['border']}" stroke-width="1.5" style="backdrop-filter: blur(20px);" />
        
        <!-- Border Shimmer -->
        <rect width="420" height="570" rx="24" fill="none" stroke="url(#accent_gradient)" stroke-width="1.5" opacity="0.3">
            <animate attributeName="opacity" values="0.1; 0.5; 0.1" dur="4s" repeatCount="indefinite" />
        </rect>

        <g clip-path="url(#left_panel_clip)">
            <!-- ASCII Art Container -->
            <g class="floating ascii" transform="translate(40, 80)" clip-path="url(#ascii_reveal)">
                {ascii_html}
            </g>

            <!-- Scanline -->
            <rect class="scanline" x="0" y="0" width="420" height="4" fill="url(#accent_gradient)" opacity="0.3" filter="url(#glass_blur)" />
            <rect class="scanline" x="0" y="4" width="420" height="20" fill="url(#accent_gradient)" opacity="0.05" />
            
            <!-- Terminal Dots -->
            <g transform="translate(20, 20)">
                <circle cx="6" cy="6" r="6" fill="#EF4444" opacity="0.8" />
                <circle cx="28" cy="6" r="6" fill="#EAB308" opacity="0.8" />
                <circle cx="50" cy="6" r="6" fill="#22C55E" opacity="0.8" />
            </g>
        </g>
    </g>

    <!-- Right Panel (Terminal Info) -->
    <g transform="translate(460, 20)">
        <!-- Glass Background -->
        <rect width="700" height="570" rx="24" fill="{t['panel']}" fill-opacity="0.6" stroke="{t['border']}" stroke-width="1.5" style="backdrop-filter: blur(20px);" />
        
        <!-- Inner Content -->
        <g transform="translate(50, 60)">
            
            <!-- Greeting -->
            <text x="0" y="0" font-size="28" font-weight="500" fill="{t['text']}" opacity="0">
                Hi 👋
                <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.5s" fill="freeze" />
                <animate attributeName="y" values="10;0" dur="0.5s" begin="0.5s" fill="freeze" />
            </text>
            
            <text x="0" y="45" font-size="48" font-weight="700" fill="{t['text']}" opacity="0">
                I'm <tspan fill="url(#accent_gradient)">Developer</tspan>
                <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1s" fill="freeze" />
                <animate attributeName="y" values="55;45" dur="0.5s" begin="1s" fill="freeze" />
            </text>

            <!-- Animated Typing Text -->
            <g transform="translate(0, 95)" class="ascii">
                <text x="0" y="0" font-size="20" font-weight="600" fill="{t['muted']}">>_</text>
                <g transform="translate(30, 0)">
                    {typing_blocks}
                    <!-- Blinking Cursor -->
                    <rect x="0" y="-18" width="10" height="22" fill="{t['accent1']}">
                        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                        <animate attributeName="x" values="0; 280; 0" dur="{timeline_duration}s" repeatCount="indefinite" />
                        <!-- Actually animating cursor X synchronously with clip path is tough in pure SMIL across multiple strings. 
                             Better approach: static cursor that blinks next to a <tspan> block that appears? 
                             Or let's just make the cursor stay at the end of the line, wait we can't if length varies.
                             Let's just put the cursor fixed at a spot, or no cursor but a blinking underscore _ 
                        -->
                    </rect>
                </g>
            </g>

            <!-- Info Lines -->
            <g transform="translate(0, 160)" font-size="16" font-weight="500" fill="{t['muted']}">
                <!-- Location -->
                <g opacity="0">
                    <text x="0" y="0" fill="{t['accent1']}">📍</text>
                    <text x="30" y="0">Based in San Francisco, CA</text>
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="2s" fill="freeze" />
                </g>
                
                <!-- Education -->
                <g opacity="0">
                    <text x="0" y="35" fill="{t['accent2']}">🎓</text>
                    <text x="30" y="35">B.S. in Computer Science</text>
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.3s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="2.3s" fill="freeze" />
                </g>
                
                <!-- Focus -->
                <g opacity="0">
                    <text x="0" y="70" fill="{t['accent3']}">🚀</text>
                    <text x="30" y="70">Building next-gen AI interfaces</text>
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.6s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="2.6s" fill="freeze" />
                </g>
                
                <!-- Portfolio -->
                <g opacity="0">
                    <text x="0" y="105" fill="{t['accent1']}">🔗</text>
                    <text x="30" y="105">developer.portfolio.com</text>
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.9s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="2.9s" fill="freeze" />
                </g>
                
                <!-- Email -->
                <g opacity="0">
                    <text x="0" y="140" fill="{t['accent2']}">✉️</text>
                    <text x="30" y="140">hello@developer.com</text>
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="3.2s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="3.2s" fill="freeze" />
                </g>
            </g>

            <!-- Skills Section -->
            <g transform="translate(0, 360)">
                <text x="0" y="-15" font-size="14" font-weight="600" fill="{t['text']}" letter-spacing="1" opacity="0">
                    TECH STACK
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="3.5s" fill="freeze" />
                </text>
                
                <g>
                    {pill_html}
                </g>
            </g>

            <!-- Social Icons -->
            <g transform="translate(0, 480)">
                <g class="social-icon" transform="translate(0, 0)" opacity="0">
                    <!-- GitHub -->
                    <rect width="40" height="40" rx="10" fill="{t['panel']}" stroke="{t['border']}" />
                    <path d="M20 10C14.477 10 10 14.477 10 20C10 24.418 12.865 28.166 16.839 29.486C17.339 29.578 17.521 29.269 17.521 29.011C17.521 28.779 17.512 28.156 17.507 27.319C14.726 27.923 14.139 25.979 14.139 25.979C13.684 24.823 13.029 24.515 13.029 24.515C12.122 23.896 13.097 23.908 13.097 23.908C14.1 23.979 14.627 24.938 14.627 24.938C15.518 26.465 16.962 26.024 17.539 25.766C17.629 25.112 17.893 24.671 18.185 24.42C15.965 24.168 13.633 23.31 13.633 19.479C13.633 18.388 14.023 17.494 14.664 16.804C14.561 16.552 14.216 15.533 14.762 14.16C14.762 14.16 15.603 13.89 17.5 15.174C18.299 14.951 19.151 14.84 20 14.836C20.849 14.84 21.701 14.951 22.502 15.174C24.397 13.89 25.236 14.16 25.236 14.16C25.784 15.533 25.439 16.552 25.337 16.804C25.979 17.494 26.366 18.388 26.366 19.479C26.366 23.322 24.032 24.164 21.803 24.412C22.169 24.728 22.501 25.352 22.501 26.313C22.501 27.691 22.489 28.804 22.489 29.011C22.489 29.273 22.668 29.584 23.176 29.485C27.147 28.163 30 24.417 30 20C30 14.477 25.523 10 20 10Z" fill="{t['text']}" />
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="4.5s" fill="freeze" />
                    <animate attributeName="transform" values="translate(0, 10); translate(0, 0)" dur="0.5s" begin="4.5s" fill="freeze" />
                </g>
                
                <g class="social-icon" transform="translate(60, 0)" opacity="0">
                    <!-- LinkedIn -->
                    <rect width="40" height="40" rx="10" fill="{t['panel']}" stroke="{t['border']}" />
                    <path d="M14.625 15.3567C14.625 16.4831 13.6841 17.396 12.5255 17.396C11.3664 17.396 10.426 16.4831 10.426 15.3567C10.426 14.23 11.3664 13.3176 12.5255 13.3176C13.6841 13.3176 14.625 14.23 14.625 15.3567ZM10.5513 28.5H14.5027V18.6657H10.5513V28.5ZM21.3655 18.4239C19.2619 18.4239 18.2831 19.5786 17.7551 20.4497V18.6657H13.8037C13.8565 19.7801 13.8037 28.5 13.8037 28.5H17.7551V23.0039C17.7551 22.7099 17.7763 22.4158 17.8631 22.2057C18.1002 21.6171 18.6534 21.008 19.5752 21.008C20.7831 21.008 21.2586 21.9272 21.2586 23.2778V28.5H25.2104V22.9198C25.2104 19.927 23.6309 18.4239 21.3655 18.4239Z" fill="{t['text']}" />
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="4.7s" fill="freeze" />
                    <animate attributeName="transform" values="translate(60, 10); translate(60, 0)" dur="0.5s" begin="4.7s" fill="freeze" />
                </g>

                <g class="social-icon" transform="translate(120, 0)" opacity="0">
                    <!-- Twitter / X -->
                    <rect width="40" height="40" rx="10" fill="{t['panel']}" stroke="{t['border']}" />
                    <path d="M22.46 12.9102H25.28L19.12 19.9402L26.36 29.5002H20.69L16.25 23.6902L11.16 29.5002H8.34L14.92 21.9802L8 12.9102H13.83L17.84 18.2102L22.46 12.9102ZM21.46 27.8102H23.02L12.81 14.5002H11.15L21.46 27.8102Z" fill="{t['text']}" />
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="4.9s" fill="freeze" />
                    <animate attributeName="transform" values="translate(120, 10); translate(120, 0)" dur="0.5s" begin="4.9s" fill="freeze" />
                </g>
                
                <g class="social-icon" transform="translate(180, 0)" opacity="0">
                    <!-- Website/Portfolio -->
                    <rect width="40" height="40" rx="10" fill="{t['panel']}" stroke="{t['border']}" />
                    <path d="M20 11C15.0294 11 11 15.0294 11 20C11 24.9706 15.0294 29 20 29C24.9706 29 29 24.9706 29 20C29 15.0294 24.9706 11 20 11ZM12.83 20C12.83 18.8 13.12 17.67 13.62 16.66L17.26 20.3C17.18 20.57 17.12 20.87 17.12 21.18C17.12 22.77 18.41 24.06 20 24.06C20.31 24.06 20.61 24 20.88 23.92L24.52 27.56C23.23 28.47 21.67 29 20 29C15.0294 29 11 24.9706 11 20ZM27.17 20C27.17 21.2 26.88 22.33 26.38 23.34L22.74 19.7C22.82 19.43 22.88 19.13 22.88 18.82C22.88 17.23 21.59 15.94 20 15.94C19.69 15.94 19.39 16 19.12 16.08L15.48 12.44C16.77 11.53 18.33 11 20 11C24.9706 11 29 15.0294 29 20Z" fill="{t['text']}" />
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="5.1s" fill="freeze" />
                    <animate attributeName="transform" values="translate(180, 10); translate(180, 0)" dur="0.5s" begin="5.1s" fill="freeze" />
                </g>
            </g>
        </g>
    </g>
</svg>'''
    return svg_content

if __name__ == "__main__":
    dark_svg = generate_svg("dark")
    light_svg = generate_svg("light")
    
    with open("C:\\Users\\user\\.gemini\\antigravity\\scratch\\github-banner\\dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    with open("C:\\Users\\user\\.gemini\\antigravity\\scratch\\github-banner\\light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
    
    print("SVGs generated successfully.")
