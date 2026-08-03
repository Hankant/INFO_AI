# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_PATH = (
    Path(r"E:\Info_AI")
    / "主Agent"
    / "文章项目"
    / "03_AIA责任归因"
    / "Paper3_Experimental_Logic_RQ_Manipulation_Map_2026-07-06.png"
)

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FALLBACK_FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FALLBACK_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"

TITLE = "Paper 3 Experimental Logic: RQ -> Manipulation -> Comparison"
SUBTITLE = "Current operational version for PPT use; based on Human-only / AI-baseline / AI-confirm / AI-disclosure"
FOOTER = (
    "Working design map. Note: the broader draft also discusses AI role proximity; the current experiment operationalizes "
    "responsibility design mainly through confirm and disclosure."
)

COLUMNS = [
    ("RQ / Working H", 260),
    ("Experimental Operation", 380),
    ("Key Comparison", 290),
    ("What the Manipulation Changes", 360),
    ("Main Readout", 310),
    ("What It Identifies", 390),
]

ROWS = [
    [
        "RQ1 / H1\nAI support effect",
        "Add a fixed-format AI analysis panel before choice. No action recommendation and no forced confirmation.",
        "Human-only vs AI-baseline",
        "Introduces AI support and a shared-decision setting without changing the formal game.",
        "Escalation choice, mutual escalation, responsibility measures",
        "Whether AI support per se shifts high-risk strategic choice and responsibility perception.",
    ],
    [
        "RQ2 / H2-H3\nConfirm effect",
        'Keep the same AI analysis as baseline, but require a click-through acknowledgment: "I have reviewed the AI analysis."',
        "AI-baseline vs AI-confirm",
        "Raises process ownership, active release, and explicit human passage through the AI stage.",
        "Decisional ownership, felt accountability, escalation",
        "Whether confirm re-anchors final agency in the human, rather than merely adding friction.",
    ],
    [
        "RQ3 / H4\nDisclosure effect",
        "Keep the same AI analysis as baseline, then require post-round self-disclosure of AI use and its influence on the decision.",
        "AI-baseline vs AI-disclosure",
        "Raises visibility, traceability, disclosure obligation, and explicit labeling of AI involvement.",
        "Felt accountability, responsibility sharing, escalation",
        "Whether making AI use explicit strengthens answerability or instead normalizes shared responsibility.",
    ],
    [
        "RQ4 / H5\nMechanism alignment",
        "Compare confirm-centered and disclosure-centered AI systems inside the same Hawk-Dove environment.",
        "AI-confirm vs AI-disclosure\nplus treatment -> mechanism -> behavior",
        "Contrasts ownership-oriented vs visibility-oriented accountability architecture.",
        "Escalation, ownership, felt accountability, attribution pattern",
        "Whether behavior changes line up with responsibility mechanisms, or whether competing mechanisms dominate.",
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
    body_font, _ = load_font_pair(20, 22)
    small_font, _ = load_font_pair(16, 16)
    _, header_bold = load_font_pair(21, 23)
    _, title_bold = load_font_pair(35, 37)

    padding_x = 14
    padding_y = 12
    line_gap = 6
    margin = 32
    title_h = 106
    footer_h = 72

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)

    body_bbox = draw.textbbox((0, 0), "Ag", font=body_font)
    body_line_h = body_bbox[3] - body_bbox[1]
    header_bbox = draw.textbbox((0, 0), "Header", font=header_bold)
    header_h = (header_bbox[3] - header_bbox[1]) + 2 * padding_y

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
    footer_lines = wrap_text(d, FOOTER, small_font, img_w - 2 * margin)
    text_y = footer_y
    for line in footer_lines:
        d.text((margin, text_y), line, fill="#5f6670", font=small_font)
        text_y += body_line_h

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
