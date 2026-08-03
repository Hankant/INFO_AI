# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_PATH = Path(
    r"E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\文献批判靶子_自动化偏差与信息校准_2026-07-05.png"
)

FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"

TITLE = "第一篇可用文献批判靶子：自动化偏差、搜索减少与信息校准"
SUBTITLE = (
    "工作备忘录：用于 literature review / gap / PPT 中的 "
    "existing work -> traditional view -> gap"
)
FOOTER = (
    "注：这是项目内工作备忘录，不替代正式共享文献库入库流程。"
    "完整链接与扩展说明保存在同目录 Markdown 版本。"
)

COLUMNS = [
    ("序号", 90),
    ("靶子文献", 420),
    ("领域/情境", 170),
    ("核心靶子观点", 700),
    ("它的问题", 420),
    ("你的批判切口", 560),
]

ROWS = [
    [
        "1",
        "Sutton, Arnold, & Holt\n《An extension of the theory of technology dominance》",
        "管理、审计、专业决策、AI 决策辅助",
        "TTD/TTD2 认为智能系统会改变专业判断中的 reliance 结构，并可能带来"
        "短期判断偏误、长期 deskilling 与职业知识退化。该文把 TTD2 明确扩展到 "
        "accounting、auditing、finance、medicine、law 等专业场景。",
        "其风险叙事容易滑向“人类被技术主宰后减少独立思考/信息搜索，所以决策恶化”。",
        "可批判它仍偏宏观：技术主宰不只是人少搜索，而是 AI 改写了人能看到、"
        "能比较、能质疑的信息结构。",
    ],
    [
        "2",
        "Seow, P.-S. (2011)\n《The effects of decision aid structural restrictiveness on decision-making outcomes》",
        "审计、内部控制、计算机化 decision aid",
        "结构限制性强的 decision aid 会迫使用户按系统给定流程行动；实验发现，"
        "限制性越强，用户越难识别系统没有提示的项目。",
        "这篇非常接近你的观点，但它仍主要把问题归为 decision aid design restrictiveness，"
        "而不是 AI 摘要的信息代表性。",
        "可作为桥梁文献：坏决策不是因为搜索少，而是因为系统把“未提示信息”"
        "从用户视野中结构性排除了。",
    ],
    [
        "3",
        "Lyell & Coiera (2017)\n《Automation bias and verification complexity: a systematic review》",
        "医疗、人因工程、临床决策支持系统",
        "Automation bias 被定义为对决策支持系统过度依赖，从而降低 information seeking "
        "和 information processing 的 vigilance。",
        "该综述把 verification complexity 作为重要机制，但容易把“是否充分核验”"
        "理解为用户行为强度问题。",
        "你的反驳是：核验复杂度本身并不决定决策质量，关键是核验路径是否包含"
        "诊断性证据、反例证据和代表性信息。",
    ],
    [
        "4",
        "Hondrich & Ruschemeier (2023)\n《Addressing Automation Bias Through Verifiability》",
        "算法治理、human-in-the-loop、法律合规",
        "该文把 verification behavior 视为缓解 automation bias 的关键变量，并提出 "
        "verifiability 是 meaningful human involvement 的最低必要条件。",
        "它把“可验证性”制度化了，但仍可能默认：只要人能验证、愿意验证、"
        "验证足够多，就能改善监督质量。",
        "可批判：meaningful human oversight 的核心不是形式上的可验证，而是 AI 输出"
        "是否为人类保留了足够代表性、冲突性和可反驳的信息。",
    ],
    [
        "5",
        "Kupfer et al. (2023)\n《Check the box! How to deal with automation bias in AI-based personnel selection》",
        "AI 人力资源筛选、简历摘要、AI dashboard",
        "研究发现 verification intensity indicators 与客观决策质量正相关；较低点击数、"
        "页面访问和停留时间意味着更高 automation bias 和更差决策质量。",
        "这是最直接的“少搜索 = 坏决策”靶子。实验通过降低数据聚合度、提示系统错误等方式"
        "提升核验强度，但没有充分控制 AI 摘要的信息代表性。",
        "你的核心批判可以集中在这里：提高搜索量只是补救手段；真正的因果机制是 "
        "AI 摘要是否遗漏了关键反例、少数派信息、边缘但高诊断性线索。",
    ],
]


def load_fonts():
    try:
        return {
            "title": ImageFont.truetype(FONT_BOLD_PATH, 42),
            "header": ImageFont.truetype(FONT_BOLD_PATH, 24),
            "body": ImageFont.truetype(FONT_PATH, 22),
            "small": ImageFont.truetype(FONT_PATH, 18),
        }
    except Exception:
        default = ImageFont.load_default()
        return {"title": default, "header": default, "body": default, "small": default}


def wrap_text(draw, text, font, max_width):
    paragraphs = str(text).split("\n")
    lines = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            lines.append("")
            continue
        current = ""
        for ch in para:
            test = current + ch
            if draw.textbbox((0, 0), test, font=font)[2] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines or [""]


def main():
    fonts = load_fonts()
    padding_x = 18
    padding_y = 14
    line_gap = 8
    margin = 40
    title_h = 120
    footer_h = 70

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)

    body_line_bbox = draw.textbbox((0, 0), "测", font=fonts["body"])
    body_line_h = body_line_bbox[3] - body_line_bbox[1]

    header_bbox = draw.textbbox((0, 0), "表头", font=fonts["header"])
    header_h = (header_bbox[3] - header_bbox[1]) + 2 * padding_y

    row_heights = []
    for row in ROWS:
        max_h = 0
        for (_, width), cell in zip(COLUMNS, row):
            lines = wrap_text(draw, cell, fonts["body"], width - 2 * padding_x)
            h = len(lines) * body_line_h + max(0, len(lines) - 1) * line_gap + 2 * padding_y
            max_h = max(max_h, h)
        row_heights.append(max_h)

    content_w = sum(w for _, w in COLUMNS)
    img_w = content_w + margin * 2
    img_h = margin + title_h + header_h + sum(row_heights) + footer_h + margin

    img = Image.new("RGB", (img_w, img_h), "#f7f4ee")
    d = ImageDraw.Draw(img)

    d.text((margin, margin), TITLE, fill="#17202a", font=fonts["title"])
    d.text((margin, margin + 58), SUBTITLE, fill="#55606e", font=fonts["small"])

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
        bbox = d.textbbox((0, 0), header, font=fonts["header"])
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        d.text((cur_x + (width - tw) / 2, y + (header_h - th) / 2 - 1), header, fill=header_fg, font=fonts["header"])
        cur_x += width

    y += header_h

    for idx, (row, rh) in enumerate(zip(ROWS, row_heights), start=1):
        bg = row_bg1 if idx % 2 == 1 else row_bg2
        cur_x = margin
        for col_idx, ((_, width), cell) in enumerate(zip(COLUMNS, row)):
            d.rectangle([cur_x, y, cur_x + width, y + rh], fill=bg, outline=grid, width=2)
            if col_idx == 0:
                bbox = d.textbbox((0, 0), cell, font=fonts["header"])
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                d.text((cur_x + (width - tw) / 2, y + (rh - th) / 2 - 2), cell, fill=accent, font=fonts["header"])
            else:
                lines = wrap_text(d, cell, fonts["body"], width - 2 * padding_x)
                text_y = y + padding_y
                for line in lines:
                    d.text((cur_x + padding_x, text_y), line, fill=text_color, font=fonts["body"])
                    text_y += body_line_h + line_gap
            cur_x += width
        y += rh

    footer_y = img_h - margin - footer_h + 12
    d.line((margin, footer_y - 14, img_w - margin, footer_y - 14), fill="#c9c1b3", width=2)
    d.text((margin, footer_y), FOOTER, fill="#5f6670", font=fonts["small"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
