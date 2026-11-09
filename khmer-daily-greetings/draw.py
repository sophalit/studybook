# -*- coding: utf-8 -*-
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(OUT, exist_ok=True)

BLUE, GREEN, ORANGE, PURPLE = '#0052A4', '#00A84D', '#EF7C1C', '#996CAC'
WHITE, LINE, INK, BG = '#FFFFFF', '#D1D5DB', '#1F2937', '#F3F4F6'

def svg(name, body, vb='0 0 160 100'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)

# c1-sampeah.svg (Two praying / sampeah hands)
svg('c1-sampeah.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<path d="M72 82 C68 65 62 45 77 18 C79 14 81 14 83 18 C98 45 92 65 88 82 Z" fill="{BLUE}" stroke="{WHITE}" stroke-width="2"/>'
    f'<path d="M80 20 L80 80" stroke="{WHITE}" stroke-width="2" stroke-linecap="round"/>'
    f'<circle cx="80" cy="50" r="14" fill="none" stroke="{WHITE}" stroke-width="2"/>')

# c2-smile.svg (Friendly greeting face)
svg('c2-smile.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<circle cx="80" cy="50" r="32" fill="{BLUE}"/>'
    f'<circle cx="68" cy="42" r="4.5" fill="{WHITE}"/>'
    f'<circle cx="92" cy="42" r="4.5" fill="{WHITE}"/>'
    f'<path d="M66 56 Q80 72 94 56" fill="none" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>')

# c3-thumbsup.svg (Doing well / thumbs up)
svg('c3-thumbsup.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(62 20)">'
    f'<rect x="0" y="24" width="16" height="36" rx="4" fill="{BLUE}"/>'
    f'<path d="M16 32 H36 C42 32 44 48 38 48 C44 48 44 60 36 60 H16 Z" fill="{BLUE}"/>'
    f'<path d="M16 32 L26 12 C29 8 34 10 33 16 L28 32 Z" fill="{BLUE}"/>'
    f'</g>')

# c4-heart.svg (Gratitude / Heart)
svg('c4-heart.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<path d="M80 78 C40 54 44 26 62 26 C72 26 78 34 80 38 C82 34 88 26 98 26 C116 26 120 54 80 78 Z" fill="{GREEN}"/>')

# c5-check.svg (No problem / checkmark)
svg('c5-check.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<circle cx="80" cy="50" r="32" fill="{GREEN}"/>'
    f'<path d="M64 50 L75 62 L96 38" fill="none" stroke="{WHITE}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')

# c6-question.svg (Polite question bubble)
svg('c6-question.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<path d="M40 22 H120 C128 22 134 28 134 36 V62 C134 70 128 76 120 76 H75 L55 88 L58 76 H40 C32 76 26 70 26 62 V36 C26 28 32 22 40 22 Z" fill="{GREEN}"/>'
    f'<text x="80" y="58" font-family="sans-serif" font-size="28" font-weight="bold" fill="{WHITE}" text-anchor="middle">?</text>')

# c7-car.svg (Safe journey / travel)
svg('c7-car.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(35 25)">'
    f'<path d="M10 32 L24 12 H66 L78 32 H86 C88 32 90 34 90 36 V48 H0 V36 C0 34 2 32 4 32 Z" fill="{ORANGE}"/>'
    f'<circle cx="24" cy="48" r="10" fill="{INK}"/>'
    f'<circle cx="24" cy="48" r="4" fill="{WHITE}"/>'
    f'<circle cx="68" cy="48" r="10" fill="{INK}"/>'
    f'<circle cx="68" cy="48" r="4" fill="{WHITE}"/>'
    f'<rect x="28" y="16" width="18" height="12" rx="2" fill="{WHITE}"/>'
    f'<rect x="50" y="16" width="14" height="12" rx="2" fill="{WHITE}"/>'
    f'</g>')

# c8-wave.svg (Waving hand goodbye)
svg('c8-wave.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(60 16)">'
    f'<path d="M12 40 C6 28 20 10 28 20 L28 40" fill="{ORANGE}" stroke="{WHITE}" stroke-width="2"/>'
    f'<path d="M20 40 V14 C20 8 30 8 30 14 V38" fill="{ORANGE}" stroke="{WHITE}" stroke-width="2"/>'
    f'<path d="M30 38 V16 C30 10 40 10 40 16 V40" fill="{ORANGE}" stroke="{WHITE}" stroke-width="2"/>'
    f'<rect x="10" y="38" width="32" height="34" rx="8" fill="{ORANGE}"/>'
    f'</g>')

# explain tiles
svg('x-sampeah.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<path d="M42 82 C38 65 32 45 47 18 C49 14 51 14 53 18 C68 45 62 65 58 82 Z" fill="{BLUE}"/>', vb='0 0 100 100')

svg('x-polite.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{GREEN}"/>'
    f'<path d="M38 50 L46 60 L64 40" fill="none" stroke="{WHITE}" stroke-width="5" stroke-linecap="round"/>', vb='0 0 100 100')

svg('x-respect.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<path d="M50 78 C25 60 25 36 40 36 C47 36 50 42 50 42 C50 42 53 36 60 36 C75 36 75 60 50 78 Z" fill="{PURPLE}"/>', vb='0 0 100 100')

svg('x-smile.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{ORANGE}"/>'
    f'<circle cx="42" cy="44" r="4" fill="{WHITE}"/>'
    f'<circle cx="58" cy="44" r="4" fill="{WHITE}"/>'
    f'<path d="M40 56 Q50 68 60 56" fill="none" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>', vb='0 0 100 100')

print('SVGs drawn successfully.')
