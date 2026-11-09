# -*- coding: utf-8 -*-
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(OUT, exist_ok=True)

BLUE, GREEN, ORANGE, PURPLE = '#0052A4', '#00A84D', '#EF7C1C', '#996CAC'
WHITE, LINE, INK, BG = '#FFFFFF', '#D1D5DB', '#1F2937', '#F3F4F6'
GOLD = '#D97706'

def svg(name, body, vb='0 0 160 100'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)

# c01-book.svg (Grade 5 Textbook cover)
svg('c01-book.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<rect x="52" y="16" width="56" height="68" rx="6" fill="{BLUE}"/>'
    f'<rect x="56" y="20" width="48" height="60" rx="3" fill="#003E7E"/>'
    f'<circle cx="80" cy="38" r="10" fill="{GOLD}"/>'
    f'<path d="M80 32 L83 37 L88 38 L84 42 L85 47 L80 44 L75 47 L76 42 L72 38 L77 37 Z" fill="{WHITE}"/>'
    f'<rect x="62" y="54" width="36" height="5" rx="2" fill="{WHITE}"/>'
    f'<rect x="66" y="63" width="28" height="4" rx="2" fill="{GOLD}"/>'
    f'<rect x="52" y="16" width="6" height="68" rx="2" fill="#002B59"/>')

# c02-skills.svg (4 Skills: Book, Pencil, Ear, Chat)
svg('c02-skills.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(44 14)">'
    f'<rect x="0" y="0" width="32" height="32" rx="8" fill="{BLUE}"/>'
    f'<path d="M8 20 C12 18 16 18 20 22 C24 18 28 18 32 20" stroke="{WHITE}" stroke-width="2" fill="none"/>'
    f'<rect x="40" y="0" width="32" height="32" rx="8" fill="{GREEN}"/>'
    f'<path d="M48 24 L64 8 L68 12 L52 28 Z" fill="{WHITE}"/>'
    f'<rect x="0" y="40" width="32" height="32" rx="8" fill="{ORANGE}"/>'
    f'<path d="M12 16 C12 10 20 10 20 16 C20 20 16 22 16 26" stroke="{WHITE}" stroke-width="2.5" fill="none" transform="translate(0 38)"/>'
    f'<rect x="40" y="40" width="32" height="32" rx="8" fill="{PURPLE}"/>'
    f'<path d="M46 50 H66 C68 50 70 52 70 54 V64 C70 66 68 68 66 68 H54 L48 73 V68 H46 C44 68 42 66 42 64 V54 C42 52 44 50 46 50 Z" fill="{WHITE}"/>'
    f'</g>')

# c03-heroes.svg (Role models / Heroic achievement)
svg('c03-heroes.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<circle cx="80" cy="50" r="32" fill="{BLUE}"/>'
    f'<circle cx="80" cy="40" r="11" fill="{WHITE}"/>'
    f'<path d="M60 68 C60 55 70 54 80 54 C90 54 100 55 100 68 Z" fill="{WHITE}"/>'
    f'<circle cx="112" cy="30" r="10" fill="{GOLD}"/>'
    f'<path d="M112 25 L114 29 L118 30 L115 33 L116 37 L112 35 L108 37 L109 33 L106 30 L110 29 Z" fill="{WHITE}"/>')

# c04-poem.svg (Scroll / Poetry / Traditional literature)
svg('c04-poem.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(48 18)">'
    f'<rect x="8" y="6" width="48" height="52" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="14" y="14" width="36" height="3" rx="1" fill="{GREEN}"/>'
    f'<rect x="14" y="21" width="36" height="3" rx="1" fill="{GREEN}"/>'
    f'<rect x="14" y="28" width="28" height="3" rx="1" fill="{GREEN}"/>'
    f'<rect x="14" y="35" width="32" height="3" rx="1" fill="{GREEN}"/>'
    f'<rect x="14" y="42" width="24" height="3" rx="1" fill="{GREEN}"/>'
    f'<path d="M48 38 L62 10 C63 8 66 8 67 10 L64 36 Z" fill="{PURPLE}"/>'
    f'<circle cx="64" cy="42" r="3" fill="{PURPLE}"/>'
    f'</g>')

# c05-topics.svg (10 Lesson Units / Curriculum matrix)
svg('c05-topics.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(38 18)">'
    f'<rect x="0" y="0" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="30" y="0" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="60" y="0" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="0" y="23" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="30" y="23" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="60" y="23" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="0" y="46" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="30" y="46" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="60" y="46" width="24" height="18" rx="4" fill="{GREEN}"/>'
    f'<rect x="30" y="46" width="24" height="18" rx="4" fill="{GOLD}"/>'
    f'<text x="42" y="59" font-family="sans-serif" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">10</text>'
    f'</g>')

# c06-pencil.svg (Exercises and practices)
svg('c06-pencil.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(42 20)">'
    f'<rect x="0" y="0" width="46" height="60" rx="5" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="8" y1="14" x2="38" y2="14" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="8" y1="24" x2="38" y2="24" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="8" y1="34" x2="38" y2="34" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="8" y1="44" x2="30" y2="44" stroke="{LINE}" stroke-width="2"/>'
    f'<g transform="translate(38 12) rotate(30)">'
    f'<rect x="0" y="0" width="8" height="34" rx="2" fill="{GREEN}"/>'
    f'<polygon points="0,34 8,34 4,42" fill="{GOLD}"/>'
    f'<polygon points="3,39 5,39 4,42" fill="{INK}"/>'
    f'</g>'
    f'</g>')

# c07-test.svg (Reading Assessment Test)
svg('c07-test.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(48 14)">'
    f'<rect x="0" y="8" width="54" height="64" rx="6" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="18" y="2" width="18" height="10" rx="3" fill="{INK}"/>'
    f'<path d="M12 26 L18 32 L30 20" stroke="{ORANGE}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    f'<path d="M12 42 L18 48 L30 36" stroke="{ORANGE}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    f'<path d="M12 58 L18 64 L30 52" stroke="{ORANGE}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    f'<line x1="36" y1="26" x2="48" y2="26" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="36" y1="42" x2="48" y2="42" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="36" y1="58" x2="48" y2="58" stroke="{LINE}" stroke-width="2"/>'
    f'</g>')

# c08-dictionary.svg (Glossary / Dictionary book)
svg('c08-dictionary.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(36 18)">'
    f'<path d="M44 54 C34 48 20 48 4 52 V12 C20 8 34 8 44 14 Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M44 54 C54 48 68 48 84 52 V12 C68 8 54 8 44 14 Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M44 14 V54" stroke="{ORANGE}" stroke-width="3"/>'
    f'<line x1="12" y1="20" x2="36" y2="20" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="12" y1="28" x2="36" y2="28" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="12" y1="36" x2="28" y2="36" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="52" y1="20" x2="76" y2="20" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="52" y1="28" x2="76" y2="28" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="52" y1="36" x2="68" y2="36" stroke="{LINE}" stroke-width="2"/>'
    f'</g>')

# c09-success.svg (Academic success & graduation)
svg('c09-success.svg',
    f'<rect width="160" height="100" rx="12" fill="{BG}"/>'
    f'<g transform="translate(45 16)">'
    f'<polygon points="35,16 70,28 35,40 0,28" fill="{ORANGE}"/>'
    f'<path d="M14 36 V52 C14 58 35 64 35 64 C35 64 56 58 56 52 V36" fill="{GOLD}"/>'
    f'<path d="M60 28 L66 44 L63 56" stroke="{GOLD}" stroke-width="2.5" fill="none"/>'
    f'<circle cx="63" cy="58" r="3" fill="{GOLD}"/>'
    f'<circle cx="10" cy="18" r="4" fill="{GOLD}"/>'
    f'<circle cx="62" cy="14" r="3" fill="{GOLD}"/>'
    f'</g>')

# Explain tiles
svg('x-skills.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{BLUE}"/>'
    f'<rect x="36" y="36" width="12" height="12" rx="2" fill="{WHITE}"/>'
    f'<rect x="52" y="36" width="12" height="12" rx="2" fill="{GOLD}"/>'
    f'<rect x="36" y="52" width="12" height="12" rx="2" fill="{GOLD}"/>'
    f'<rect x="52" y="52" width="12" height="12" rx="2" fill="{WHITE}"/>', vb='0 0 100 100')

svg('x-heroes.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{GREEN}"/>'
    f'<circle cx="50" cy="42" r="9" fill="{WHITE}"/>'
    f'<path d="M34 66 C34 54 42 53 50 53 C58 53 66 54 66 66 Z" fill="{WHITE}"/>', vb='0 0 100 100')

svg('x-literature.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{PURPLE}"/>'
    f'<path d="M32 40 C38 34 46 34 50 38 C54 34 62 34 68 40 V62 C62 58 54 58 50 62 C46 58 38 58 32 62 Z" fill="{WHITE}"/>', vb='0 0 100 100')

svg('x-glossary.svg',
    f'<circle cx="50" cy="50" r="48" fill="{BG}"/>'
    f'<circle cx="50" cy="50" r="32" fill="{ORANGE}"/>'
    f'<path d="M36 34 H64 V66 H36 Z" fill="{WHITE}" rx="2"/>'
    f'<line x1="42" y1="42" x2="58" y2="42" stroke="{ORANGE}" stroke-width="2.5"/>'
    f'<line x1="42" y1="50" x2="58" y2="50" stroke="{ORANGE}" stroke-width="2.5"/>'
    f'<line x1="42" y1="58" x2="52" y2="58" stroke="{ORANGE}" stroke-width="2.5"/>', vb='0 0 100 100')

print('Grade 5 SVGs drawn successfully.')
