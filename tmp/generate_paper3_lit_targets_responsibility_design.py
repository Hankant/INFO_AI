# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_PATH = (
    Path(r"E:\Info_AI")
    / "主Agent"
    / "文章项目"
    / "03_AIA责任归因"
    / "Paper3_Literature_Targets_AI_Responsibility_Design_2026-07-06.png"
)

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FALLBACK_FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FALLBACK_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"

TITLE = "Paper 3 Literature Targets: Responsibility Design, Accountability, and Strategic Risk"
SUBTITLE = "Working critique table for literature review / gap / PPT pages on AI responsibility structure"
FOOTER = (
    "Internal working memo. Designed to foreground target claims, their limits, and the paper's critical push."
)

COLUMNS = [
    ("No.", 80),
    ("Target Paper", 360),
    ("Domain / Context", 190),
    ("Core Target Claim", 520),
    ("Problem in That Claim", 410),
    ("Your Critical Angle", 520),
]

ROWS = [
    [
        "1",
        'Shrestha, Ben-Menahem, & von Krogh (2019)\n"Organizational decision-making structures in the age of AI"',
        "Management, organizational design, AI-assisted decisions",
        "AI can be embedded through different organizational decision structures, from delegation to sequential or aggregated human-AI judgment.",
        "Great on where AI sits in the workflow, but says little about whether those placements reshape felt responsibility or risky strategic choice.",
        "Treat AI position as more than workflow design. It is also a responsibility-architecture variable that may alter ownership, accountability, and escalation.",
    ],
    [
        "2",
        'Yin, Ngiam, Tan, & Teo (2025)\n"Designing AI-based work processes"',
        "Diagnostic work processes, AI advice timing",
        "When AI advice enters the process materially changes calibration and performance; ex post advice may perform best.",
        "Frames process design mainly as an accuracy and calibration question, not as a responsibility design question.",
        "Push the timing logic toward accountability: when AI enters the process may shift not only performance, but also who feels responsible for the final act.",
    ],
    [
        "3",
        'Kirchkamp & Strobel (2019)\n"Sharing responsibility with a machine"',
        "Behavioral economics, human-machine joint decisions",
        "Machine co-decision can trigger responsibility sharing and alter guilt or responsibility perceptions.",
        "Establishes machine participation as a coarse treatment, but does not unpack concrete AI-system interventions inside the decision process.",
        "The next step is not just machine present vs absent. It is to compare system-level responsibility designs such as confirm, disclosure, or approval gates.",
    ],
    [
        "4",
        'Chevrier & Teixeira (2024)\n"Algorithm delegation and responsibility"',
        "Algorithm delegation, blame shifting, moral choice",
        "Delegating to algorithms can shift blame among user, algorithm, and programmer.",
        "Focuses on delegation and attribution, but says less about whether those shifts change risky strategic behavior before outcomes occur.",
        "Move from ex post blame redistribution to ex ante behavior: do altered responsibility structures make escalation more likely?",
    ],
    [
        "5",
        'Hall, Frink, & Buckley (2017)\n"An accountability account"',
        "Organizational behavior, felt accountability",
        "Felt accountability depends on expectations of being observed, evaluated, and having to justify one's actions.",
        "Strong on accountability theory, but largely outside AI-assisted system design and human-AI responsibility architecture.",
        "Translate classic accountability into concrete AI interventions: who confirms, who discloses, what is logged, and what users must explain.",
    ],
    [
        "6",
        'Coeckelbergh (2020)\n"AI, Responsibility Attribution, and Explainability"',
        "AI responsibility attribution, explainability, governance",
        "AI complicates responsibility attribution and makes explainability central to justifying who should answer for outcomes.",
        "Mostly normative or attributional, and often post hoc. It leaves open how responsibility design affects live risky choice under AI support.",
        "The gap is not only who gets blamed after failure, but whether responsibility architecture changes behavior before failure occurs.",
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
    paragraphs = str(text).split("\n")
    lines = []
    for para in paragraphs:
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
    body_font, body_bold = load_font_pair(20, 22)
    small_font, _ = load_font_pair(16, 16)
    _, header_bold = load_font_pair(22, 24)
    _, title_bold = load_font_pair(36, 38)

    padding_x = 16
    padding_y = 12
    line_gap = 6
    margin = 34
    title_h = 110
    footer_h = 64

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)

    body_line_h = draw.textbbox((0, 0), "Ag", font=body_font)[3] - draw.textbbox((0, 0), "Ag", font=body_font)[1]
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
    d.text((margin, margin + 52), SUBTITLE, fill="#55606e", font=small_font)

    y = margin + title_h
    header_bg = "#25364a"
    header_fg = "#ffffff"
    grid = "#8f99a3"
    row_bg1 = "#fffdf8"
    row_bg2 = "#f3efe7"
    text_color = "#1e252b"
    accent = "#6c3d10"

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
        for col_idx, ((_, width), cell) in enumerate(zip(COLUMNS, row)):
            d.rectangle([cur_x, y, cur_x + width, y + rh], fill=bg, outline=grid, width=2)
            if col_idx == 0:
                bbox = d.textbbox((0, 0), cell, font=header_bold)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                d.text((cur_x + (width - tw) / 2, y + (rh - th) / 2 - 2), cell, fill=accent, font=header_bold)
            else:
                lines = wrap_text(d, cell, body_font, width - 2 * padding_x)
                text_y = y + padding_y
                for line in lines:
                    d.text((cur_x + padding_x, text_y), line, fill=text_color, font=body_font)
                    text_y += body_line_h + line_gap
            cur_x += width
        y += rh

    footer_y = img_h - margin - footer_h + 10
    d.line((margin, footer_y - 12, img_w - margin, footer_y - 12), fill="#c9c1b3", width=2)
    d.text((margin, footer_y), FOOTER, fill="#5f6670", font=small_font)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
