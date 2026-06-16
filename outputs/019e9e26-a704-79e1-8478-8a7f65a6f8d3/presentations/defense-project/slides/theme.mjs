export const theme = {
  colors: {
    paper: "#F6F1E8",
    panel: "#FFF9F0",
    stone: "#E9DDCB",
    mist: "#D9D1C7",
    ink: "#1D2433",
    muted: "#5F6775",
    accent: "#B45A3C",
    accentSoft: "#E8C6B8",
    sage: "#667561",
    gold: "#C89B4A",
    navy: "#1F2A44",
    white: "#FFFFFF",
  },
  fonts: {
    title: "Georgia",
    body: "Aptos",
    mono: "Aptos Mono",
  },
};

export function line(fill, width = 1, style = "solid") {
  return { style, fill, width };
}

export function baseSlide(presentation, ctx, options = {}) {
  const dark = Boolean(options.dark);
  const slide = presentation.slides.add();
  const bg = dark ? theme.colors.navy : theme.colors.paper;
  const orbA = dark ? "#314062" : "#EDE1D0";
  const orbB = dark ? "#273554" : "#F1E7D9";
  const ink = dark ? theme.colors.white : theme.colors.ink;

  ctx.addShape(slide, {
    left: 0,
    top: 0,
    width: ctx.W,
    height: ctx.H,
    fill: bg,
    line: line(bg, 0),
  });

  ctx.addShape(slide, {
    geometry: "ellipse",
    left: ctx.W - 280,
    top: -120,
    width: 360,
    height: 360,
    fill: orbA,
    line: line(orbA, 0),
  }).sendToBack();

  ctx.addShape(slide, {
    geometry: "ellipse",
    left: -120,
    top: ctx.H - 220,
    width: 300,
    height: 300,
    fill: orbB,
    line: line(orbB, 0),
  }).sendToBack();

  ctx.addShape(slide, {
    left: 58,
    top: 48,
    width: 2,
    height: ctx.H - 96,
    fill: dark ? theme.colors.gold : theme.colors.accentSoft,
    line: line(dark ? theme.colors.gold : theme.colors.accentSoft, 0),
  });

  if (options.band) {
    ctx.addShape(slide, {
      left: 96,
      top: options.band.top ?? 124,
      width: options.band.width ?? 1080,
      height: options.band.height ?? 54,
      fill: dark ? "#273654" : theme.colors.panel,
      line: line(dark ? "#273654" : theme.colors.panel, 0),
    });
  }

  slide.__ink = ink;
  slide.__dark = dark;
  return slide;
}

export function inkForSlide(slide) {
  return slide.__ink || theme.colors.ink;
}

export function mutedForSlide(slide) {
  return slide.__dark ? "#D8DCE6" : theme.colors.muted;
}

export function panelFill(slide) {
  return slide.__dark ? "#283655" : theme.colors.panel;
}

export function panelLine(slide) {
  return slide.__dark ? "#435071" : theme.colors.stone;
}

export function addKicker(slide, ctx, text, options = {}) {
  const left = options.left ?? 96;
  const top = options.top ?? 60;
  const color = options.color ?? (slide.__dark ? theme.colors.gold : theme.colors.accent);
  const textColor = options.textColor ?? color;

  ctx.addShape(slide, {
    left,
    top: top + 9,
    width: 18,
    height: 18,
    fill: color,
    line: line(color, 0),
    name: "kicker-marker",
  });

  ctx.addText(slide, {
    text,
    left: left + 28,
    top,
    width: options.width ?? 260,
    height: 36,
    fontSize: 14,
    bold: true,
    color: textColor,
    face: theme.fonts.body,
    valign: "middle",
    name: "kicker-label",
  });
}

export function addTitle(slide, ctx, title, options = {}) {
  const left = options.left ?? 96;
  const top = options.top ?? 96;
  const width = options.width ?? 720;
  const height = options.height ?? 110;
  const color = options.color ?? inkForSlide(slide);
  const size = options.size ?? 34;

  ctx.addText(slide, {
    text: title,
    left,
    top,
    width,
    height,
    fontSize: size,
    bold: true,
    color,
    face: theme.fonts.title,
    valign: "middle",
  });
}

export function addSubtitle(slide, ctx, text, options = {}) {
  ctx.addText(slide, {
    text,
    left: options.left ?? 96,
    top: options.top ?? 182,
    width: options.width ?? 760,
    height: options.height ?? 56,
    fontSize: options.size ?? 18,
    color: options.color ?? mutedForSlide(slide),
    face: theme.fonts.body,
  });
}

export function addFooter(slide, ctx, text, page) {
  const color = slide.__dark ? "#D7DCE7" : "#7B7F88";
  ctx.addText(slide, {
    text,
    left: 96,
    top: 682,
    width: 930,
    height: 20,
    fontSize: 10,
    color,
    face: theme.fonts.body,
  });
  ctx.addText(slide, {
    text: String(page).padStart(2, "0"),
    left: 1130,
    top: 676,
    width: 60,
    height: 24,
    fontSize: 12,
    bold: true,
    color: slide.__dark ? theme.colors.gold : theme.colors.accent,
    face: theme.fonts.mono,
    align: "right",
  });
}

export function addBulletList(slide, ctx, items, options = {}) {
  const left = options.left ?? 96;
  const top = options.top ?? 240;
  const width = options.width ?? 480;
  const gap = options.gap ?? 58;
  const bulletColor = options.bulletColor ?? (slide.__dark ? theme.colors.gold : theme.colors.accent);
  const textColor = options.textColor ?? inkForSlide(slide);
  const fontSize = options.fontSize ?? 22;
  const rowHeight = options.rowHeight ?? 48;

  items.forEach((item, index) => {
    const y = top + index * gap;
    ctx.addText(slide, {
      text: options.numbered ? `${index + 1}.` : "-",
      left,
      top: y,
      width: 24,
      height: rowHeight,
      fontSize,
      bold: true,
      color: bulletColor,
      face: theme.fonts.body,
    });
    ctx.addText(slide, {
      text: item,
      left: left + 28,
      top: y - 2,
      width,
      height: rowHeight + 18,
      fontSize,
      color: textColor,
      face: theme.fonts.body,
    });
  });
}

export function addCard(slide, ctx, options = {}) {
  const fill = options.fill ?? panelFill(slide);
  const border = options.border ?? panelLine(slide);
  const titleColor = options.titleColor ?? inkForSlide(slide);
  const bodyColor = options.bodyColor ?? mutedForSlide(slide);
  const accent = options.accent ?? (slide.__dark ? theme.colors.gold : theme.colors.accent);
  const card = ctx.addShape(slide, {
    left: options.left,
    top: options.top,
    width: options.width,
    height: options.height,
    fill,
    line: line(border, 1),
  });

  ctx.addShape(slide, {
    left: options.left,
    top: options.top,
    width: 6,
    height: options.height,
    fill: accent,
    line: line(accent, 0),
  });

  if (options.label) {
    ctx.addText(slide, {
      text: options.label,
      left: options.left + 22,
      top: options.top + 16,
      width: options.width - 44,
      height: 22,
      fontSize: 12,
      bold: true,
      color: accent,
      face: theme.fonts.body,
    });
  }

  if (options.title) {
    ctx.addText(slide, {
      text: options.title,
      left: options.left + 22,
      top: options.top + (options.label ? 34 : 18),
      width: options.width - 44,
      height: options.titleHeight ?? 42,
      fontSize: options.titleSize ?? 20,
      bold: true,
      color: titleColor,
      face: theme.fonts.title,
      valign: "middle",
    });
  }

  if (options.body) {
    ctx.addText(slide, {
      text: options.body,
      left: options.left + 22,
      top: options.bodyTop ?? (options.top + (options.label ? 80 : 64)),
      width: options.width - 44,
      height: options.bodyHeight ?? (options.height - 88),
      fontSize: options.bodySize ?? 16,
      color: bodyColor,
      face: theme.fonts.body,
    });
  }

  return card;
}

export function addTag(slide, ctx, text, options = {}) {
  const fill = options.fill ?? (slide.__dark ? "#304264" : theme.colors.stone);
  const color = options.color ?? inkForSlide(slide);
  ctx.addShape(slide, {
    geometry: "roundRect",
    left: options.left,
    top: options.top,
    width: options.width ?? 170,
    height: options.height ?? 34,
    fill,
    line: line(fill, 0),
  });
  ctx.addText(slide, {
    text,
    left: options.left + 12,
    top: options.top + 3,
    width: (options.width ?? 170) - 24,
    height: (options.height ?? 34) - 6,
    fontSize: options.size ?? 13,
    bold: true,
    color,
    face: theme.fonts.body,
    align: "center",
    valign: "middle",
  });
}

export function addArrow(slide, fromShape, toShape, options = {}) {
  return slide.shapes.connect(fromShape, toShape, {
    kind: options.kind ?? "straight",
    fromSide: options.fromSide ?? "right",
    toSide: options.toSide ?? "left",
    line: {
      style: "solid",
      fill: options.color ?? theme.colors.accent,
      width: options.width ?? 2,
    },
    head: options.head === false ? undefined : { type: "arrow", width: "med", length: "med" },
  });
}

export function addSmallNote(slide, ctx, text, options = {}) {
  ctx.addText(slide, {
    text,
    left: options.left ?? 96,
    top: options.top ?? 620,
    width: options.width ?? 1080,
    height: options.height ?? 44,
    fontSize: options.size ?? 14,
    color: options.color ?? mutedForSlide(slide),
    face: theme.fonts.body,
  });
}

export function addKeyValue(slide, ctx, key, value, options = {}) {
  ctx.addText(slide, {
    text: key,
    left: options.left,
    top: options.top,
    width: options.keyWidth ?? 170,
    height: options.height ?? 28,
    fontSize: options.keySize ?? 14,
    bold: true,
    color: options.keyColor ?? (slide.__dark ? theme.colors.gold : theme.colors.accent),
    face: theme.fonts.body,
  });
  ctx.addText(slide, {
    text: value,
    left: options.left + (options.keyWidth ?? 170),
    top: options.top,
    width: options.valueWidth ?? 360,
    height: options.height ?? 30,
    fontSize: options.valueSize ?? 15,
    color: options.valueColor ?? inkForSlide(slide),
    face: theme.fonts.body,
  });
}
