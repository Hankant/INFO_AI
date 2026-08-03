# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_PATH = Path(
    r"E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\Literature_Targets_Automation_Bias_and_Information_Calibration_2026-07-05.png"
)

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FALLBACK_FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FALLBACK_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"

TITLE = "Paper 1 Literature Targets: Automation Bias, Reduced Search, and Information Calibration"
SUBTITLE = "Working memo for literature review / gap / PPT pages on existing work -> traditional view -> gap"
FOOTER = (
    "Note: internal project memo only; not a substitute for the formal shared-library workflow. "
    "The editable English Markdown version is saved in the same folder."
)

COLUMNS = [
    ("No.", 80),
    ("Target Paper", 360),
    ("Domain / Context", 170),
    ("Core Target Claim", 690),
    ("Problem in That Claim", 410),
    ("Your Critical Angle", 570),
]

ROWS = [
    [
        "1",
        'Sutton, Arnold, & Holt\n"An extension of the theory of technology dominance"',
        "Management, auditing, professional judgment, AI-assisted decisions",
        "TTD / TTD2 argue that intelligent systems reshape reliance structures in professional judgment "
        "and may lead to short-run judgment bias, long-run deskilling, and erosion of professional knowledge. "
        "The paper explicitly extends TTD2 to accounting, auditing, finance, medicine, and law.",
        "Its risk narrative can slide toward the claim that once humans are dominated by technology, "
        "they search less and think less independently, so decision quality deteriorates.",
        "Critique it as still too macro-level: technology dominance is not just about reduced search; "
        "AI rewrites the information structure users can see, compare, and question.",
    ],
    [
        "2",
        'Seow, P.-S. (2011)\n"The effects of decision aid structural restrictiveness on decision-making outcomes"',
        "Auditing, internal control, computerized decision aids",
        "Highly restrictive decision aids force users to follow system-defined procedures; experimentally, "
        "greater restrictiveness makes users less able to identify issues not prompted by the system.",
        "This is very close to your argument, but it still attributes the problem mainly to decision aid "
        "restrictiveness rather than to the representativeness of AI summaries.",
        'Use it as a bridge paper: bad decisions are not simply caused by less search, but by the structural '
        'exclusion of "unprompted information" from the user\'s field of view.',
    ],
    [
        "3",
        'Lyell & Coiera (2017)\n"Automation bias and verification complexity: a systematic review"',
        "Medicine, human factors, clinical decision support",
        "Automation bias is defined as over-reliance on decision support systems, thereby reducing vigilance "
        "in information seeking and information processing.",
        "The review treats verification complexity as a key mechanism, but this can easily reduce the issue "
        "to the intensity of user verification behavior.",
        "Your response: verification complexity by itself does not determine decision quality; what matters is "
        "whether the verification path contains diagnostic evidence, counterevidence, and representative information.",
    ],
    [
        "4",
        'Hondrich & Ruschemeier (2023)\n"Addressing Automation Bias Through Verifiability"',
        "Algorithmic governance, human-in-the-loop, legal compliance",
        "The paper treats verification behavior as the key variable for mitigating automation bias and proposes "
        "verifiability as a minimum condition for meaningful human involvement.",
        'It institutionalizes "verifiability," but can still implicitly assume that if humans can verify, want '
        "to verify, and verify enough, supervision quality will improve.",
        "Critique: the core of meaningful human oversight is not formal verifiability alone, but whether AI outputs "
        "preserve enough representative, conflicting, and rebuttable information for human judgment.",
    ],
    [
        "5",
        'Kupfer et al. (2023)\n"Check the box! How to deal with automation bias in AI-based personnel selection"',
        "AI personnel screening, resume summaries, AI dashboards",
        "Verification intensity indicators are positively related to objective decision quality; lower clicks, "
        "page visits, and dwell time imply greater automation bias and worse decisions.",
        'This is the clearest "less search = worse decisions" target. The experiment increases verification '
        "intensity by lowering aggregation and warning about system errors, but it does not adequately control "
        "the representativeness of AI summaries.",
        "This is your sharpest critique target: increasing search is only a remedial move; the real causal mechanism "
        "is whether AI summaries omit key counterexamples, minority information, or peripheral yet highly diagnostic cues.",
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
    header_font, header_bold = load_font_pair(22, 24)
    title_font, title_bold = load_font_pair(36, 38)

    padding_x = 16
    padding_y = 12
    line_gap = 6
    margin = 34
    title_h = 108
    footer_h = 62

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)

    body_line_bbox = draw.textbbox((0, 0), "Ag", font=body_font)
    body_line_h = body_line_bbox[3] - body_line_bbox[1]

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
