# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_PATH = Path(
    r"E:\Info_AI\主Agent\文章项目\03_AIA责任归因\Paper3_RQ_Theory_Map_AI_Responsibility_Structure_Concise_2026-07-05.png"
)

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FALLBACK_FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FALLBACK_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"

TITLE = "Paper 3 RQ-Theory Map: Concise Version"
SUBTITLE = "Short table for PPT use; detailed explanations can be added orally"
FOOTER = (
    "Concise presentation version. Designed to foreground gap and research push, "
    "not to replace the full working memo."
)

COLUMNS = [
    ("Theory Line", 300),
    ("Representative Literature", 260),
    ("What Existing Research Shows", 420),
    ("Key Gap", 420),
    ("How Our RQ Pushes Further", 420),
]

ROWS = [
    [
        "1. Classic accountability foundations",
        "Tetlock (1985); Lerner & Tetlock (1999); Hall, Frink & Buckley; Aleksovska et al.",
        "Defines accountability as answerability, evaluation, and possible consequences. Distinguishes external accountability from felt accountability.",
        "Mostly human-human or human-organization settings. Says little about concrete AI-system design features.",
        "RQ2: Do AI-system responsibility designs change felt accountability, decisional ownership, and responsibility attribution?",
    ],
    [
        "2. Algorithm reliance / aversion",
        "Dietvorst et al.; Logg et al.; Bigman & Gray; Gogoll & Uhl",
        "Explains when people trust, adopt, reject, or resent algorithmic advice.",
        "Strong on trust and reliance. Weak on responsibility structure.",
        "RQ1: Does AI support itself change escalation behavior? Then shift from reliance to responsibility design.",
    ],
    [
        "3. AI delegation / machine responsibility",
        "Kirchkamp & Strobel; Chevrier & Teixeira; Kobis et al.; Huholt & Szech",
        "Shows that AI participation can redistribute responsibility, lower moral cost, and shift blame.",
        "Usually treats AI involvement as a coarse treatment. Rarely distinguishes system-level responsibility mechanisms.",
        "RQ3: Are behavioral effects aligned with changes in felt accountability, decisional ownership, and attribution?",
    ],
    [
        "4. Human-AI blame / responsibility attribution",
        "Tsumura & Yamada; Arnestad et al.; Elish; meaningful human control literature",
        "Explains how blame is redistributed across user, AI agent, and provider after failure.",
        "Mostly ex post blame allocation. Much less on ex ante risk choice.",
        "RQ3 / RQ4: Do responsibility mechanisms shape behavior before outcomes occur?",
    ],
    [
        "5. High-risk strategic decision / escalation",
        "Fearon; Powell; Kahneman & Tversky; Loewenstein et al.; Hawk-Dove / Chicken",
        "Explains escalation via payoffs, beliefs, commitment, misperception, loss aversion, and emotion.",
        "Usually treats responsibility cost as exogenous. Rarely asks how AI reshapes that expectation.",
        "Overall RQ: How does AI-system responsibility design reshape responsibility perceptions and, in turn, escalation behavior?",
    ],
]


def load_font_pair(size_regular, size_bold):
    try:
        regular = ImageFont.truetype(FONT_PATH, size_regular)
        bold = ImageFont.truetype(FONT_BOLD_PATH, size_bold)
        return regular, bold
    except Exception:
        regular = ImageFont.truetype(FALLBACK_FONT_PATH, size_regular)
        bold = ImageFont.truetype(FALLBACK_BOLD_PATH, size_bold)
        return regular, bold


def wrap_text(draw, text, font, max_width):
    lines = []
    for para in str(text).split("\n"):
        para = para.strip()
        if not para:
            lines.append("")
            continue
        words = para.split(" ")
        current = ""
        for word in words:
            test = word if not current else current + " " + word
            if draw.textbbox((0, 0), test, font=font)[2] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines or [""]


def main():
    body_font, body_bold = load_font_pair(22, 24)
    small_font, _ = load_font_pair(17, 17)
    header_font, header_bold = load_font_pair(24, 26)
    title_font, title_bold = load_font_pair(38, 40)

    padding_x = 14
    padding_y = 13
    line_gap = 6
    margin = 28
    title_h = 98
    footer_h = 52

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)

    body_line_h = draw.textbbox((0, 0), "Ag", font=body_font)[3]
    header_h = draw.textbbox((0, 0), "Header", font=header_bold)[3] + 2 * padding_y

    row_heights = []
    for row in ROWS:
        max_h = 0
        for (_, width), cell in zip(COLUMNS, row):
            lines = wrap_text(draw, cell, body_font, width - 2 * padding_x)
            h = len(lines) * body_line_h + max(0, len(lines) - 1) * line_gap + 2 * padding_y
            max_h = max(max_h, h)
        row_heights.append(max_h)

    content_w = sum(w for _, w in COLUMNS)
    img_w = content_w + margin * 2
    img_h = margin + title_h + header_h + sum(row_heights) + footer_h + margin

    img = Image.new("RGB", (img_w, img_h), "#f7f4ee")
    d = ImageDraw.Draw(img)

    d.text((margin, margin), TITLE, fill="#17202a", font=title_bold)
    d.text((margin, margin + 48), SUBTITLE, fill="#55606e", font=small_font)

    y = margin + title_h
    header_bg = "#25364a"
    header_fg = "#ffffff"
    grid = "#8f99a3"
    row_bg1 = "#fffdf8"
    row_bg2 = "#f3efe7"
    text_color = "#1e252b"

    cur_x = margin
    for header, width in COLUMNS:
        d.rectangle([cur_x, y, cur_x + width, y + header_h], fill=header_bg, outline=grid, width=2)
        bbox = d.textbbox((0, 0), header, font=header_bold)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        d.text((cur_x + (width - tw) / 2, y + (header_h - th) / 2 - 1), header, fill=header_fg, font=header_bold)
        cur_x += width

    y += header_h
    for idx, (row, rh) in enumerate(zip(ROWS, row_heights), start=1):
        bg = row_bg1 if idx % 2 == 1 else row_bg2
        cur_x = margin
        for ((_, width), cell) in zip(COLUMNS, row):
            d.rectangle([cur_x, y, cur_x + width, y + rh], fill=bg, outline=grid, width=2)
            lines = wrap_text(d, cell, body_font, width - 2 * padding_x)
            text_y = y + padding_y
            for line in lines:
                d.text((cur_x + padding_x, text_y), line, fill=text_color, font=body_font)
                text_y += body_line_h + line_gap
            cur_x += width
        y += rh

    footer_y = img_h - margin - footer_h + 8
    d.line((margin, footer_y - 10, img_w - margin, footer_y - 10), fill="#c9c1b3", width=2)
    d.text((margin, footer_y), FOOTER, fill="#5f6670", font=small_font)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
