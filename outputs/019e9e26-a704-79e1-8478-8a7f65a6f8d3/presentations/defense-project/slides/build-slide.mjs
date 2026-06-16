import { slideData } from "./content.mjs";
import {
  addArrow,
  addBulletList,
  addCard,
  addFooter,
  addKeyValue,
  addKicker,
  addSmallNote,
  addSubtitle,
  addTag,
  addTitle,
  baseSlide,
  inkForSlide,
  line,
  mutedForSlide,
  panelFill,
  panelLine,
  theme,
} from "./theme.mjs";

function standardSlide(presentation, ctx, data, page, options = {}) {
  const slide = baseSlide(presentation, ctx, options);
  addKicker(slide, ctx, data.kicker);
  addTitle(slide, ctx, data.title, { width: options.titleWidth ?? 760, size: options.titleSize ?? 34 });
  if (data.subtitle) {
    addSubtitle(slide, ctx, data.subtitle, { width: options.subtitleWidth ?? 760 });
  }
  addFooter(slide, ctx, data.sources, page);
  return slide;
}

function renderCover(presentation, ctx, data, page) {
  const slide = baseSlide(presentation, ctx, { dark: true });
  addKicker(slide, ctx, data.kicker, { color: theme.colors.gold, textColor: theme.colors.gold });
  addTitle(slide, ctx, data.title, {
    left: 96,
    top: 118,
    width: 640,
    height: 140,
    size: 38,
    color: theme.colors.white,
  });
  addSubtitle(slide, ctx, data.subtitle, {
    left: 96,
    top: 260,
    width: 620,
    height: 80,
    size: 20,
    color: "#D8DDE7",
  });
  ctx.addText(slide, {
    text: data.meta,
    left: 96,
    top: 384,
    width: 300,
    height: 30,
    fontSize: 16,
    bold: true,
    color: theme.colors.gold,
    face: theme.fonts.body,
  });

  const boxA = addCard(slide, ctx, {
    left: 800,
    top: 118,
    width: 320,
    height: 110,
    fill: "#273654",
    border: "#435071",
    accent: theme.colors.gold,
    label: "OLD ORDER",
    title: "Evidence",
    body: "People search first, interpret later.",
    bodySize: 15,
  });
  const boxB = addCard(slide, ctx, {
    left: 860,
    top: 268,
    width: 320,
    height: 110,
    fill: "#273654",
    border: "#435071",
    accent: theme.colors.gold,
    label: "NEW ORDER",
    title: "AI answer",
    body: "Interpretation appears before verification.",
    bodySize: 15,
  });
  const boxC = addCard(slide, ctx, {
    left: 800,
    top: 418,
    width: 320,
    height: 110,
    fill: "#273654",
    border: "#435071",
    accent: theme.colors.gold,
    label: "QUESTION",
    title: "What changes next?",
    body: "Search, ownership, and updating may all move.",
    bodySize: 15,
  });
  addArrow(slide, boxA, boxB, { color: theme.colors.gold, kind: "elbow", fromSide: "bottom", toSide: "top" });
  addArrow(slide, boxB, boxC, { color: theme.colors.gold, kind: "elbow", fromSide: "bottom", toSide: "top" });
  addFooter(slide, ctx, data.sources, page);
  return slide;
}

function renderThesis(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 700 });
  addBulletList(slide, ctx, data.bullets, {
    left: 96,
    top: 258,
    width: 560,
    gap: 82,
    fontSize: 23,
    rowHeight: 58,
  });
  addCard(slide, ctx, {
    left: 760,
    top: 228,
    width: 360,
    height: 276,
    label: "CORE CLAIM",
    title: data.railTitle,
    body: "",
  });
  data.railItems.forEach((item, index) => {
    addTag(slide, ctx, item, {
      left: 810,
      top: 290 + index * 62,
      width: 260,
      height: 42,
      fill: index === 0 ? theme.colors.accentSoft : index === 1 ? theme.colors.stone : "#E6E0D4",
    });
  });
  addSmallNote(
    slide,
    ctx,
    "The project studies how answer-first systems reshape search thresholds, subjective ownership, and response to later counterevidence.",
    { left: 96, top: 576, width: 1020, size: 16 },
  );
  return slide;
}

function renderSequence(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page);
  ctx.addText(slide, {
    text: data.leftTitle,
    left: 120,
    top: 220,
    width: 280,
    height: 32,
    fontSize: 20,
    bold: true,
    color: theme.colors.accent,
    face: theme.fonts.body,
  });
  ctx.addText(slide, {
    text: data.rightTitle,
    left: 690,
    top: 220,
    width: 320,
    height: 32,
    fontSize: 20,
    bold: true,
    color: theme.colors.accent,
    face: theme.fonts.body,
  });

  const leftBoxes = data.leftNodes.map((item, index) =>
    addCard(slide, ctx, {
      left: 120,
      top: 268 + index * 92,
      width: 320,
      height: 66,
      title: item,
      titleSize: 22,
      body: "",
      fill: panelFill(slide),
      border: panelLine(slide),
    }),
  );
  const rightBoxes = data.rightNodes.map((item, index) =>
    addCard(slide, ctx, {
      left: 690,
      top: 268 + index * 92,
      width: 360,
      height: 66,
      title: item,
      titleSize: 22,
      body: "",
      fill: panelFill(slide),
      border: panelLine(slide),
    }),
  );

  addArrow(slide, leftBoxes[0], leftBoxes[1], { color: theme.colors.sage, kind: "elbow", fromSide: "bottom", toSide: "top" });
  addArrow(slide, leftBoxes[1], leftBoxes[2], { color: theme.colors.sage, kind: "elbow", fromSide: "bottom", toSide: "top" });
  addArrow(slide, rightBoxes[0], rightBoxes[1], { color: theme.colors.accent, kind: "elbow", fromSide: "bottom", toSide: "top" });
  addArrow(slide, rightBoxes[1], rightBoxes[2], { color: theme.colors.accent, kind: "elbow", fromSide: "bottom", toSide: "top" });

  addCard(slide, ctx, {
    left: 442,
    top: 322,
    width: 182,
    height: 120,
    label: "SHIFT",
    title: "From evidence-led to answer-led judgment",
    titleSize: 18,
    body: "",
    fill: "#EFE5D9",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });

  addSmallNote(slide, ctx, data.claim, { top: 590, width: 1060, size: 16 });
  return slide;
}

function renderLiterature(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 860 });
  data.columns.forEach((column, index) => {
    const left = 96 + index * 364;
    addCard(slide, ctx, {
      left,
      top: 238,
      width: 330,
      height: 342,
      label: `STREAM ${index + 1}`,
      title: column.title,
      body: "",
    });
    addBulletList(slide, ctx, column.items, {
      left: left + 20,
      top: 314,
      width: 260,
      gap: 72,
      fontSize: 17,
      rowHeight: 56,
    });
    ctx.addText(slide, {
      text: column.refs,
      left: left + 20,
      top: 526,
      width: 286,
      height: 44,
      fontSize: 12,
      color: theme.colors.muted,
      face: theme.fonts.body,
    });
  });
  return slide;
}

function renderGap(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page);
  addCard(slide, ctx, {
    left: 96,
    top: 246,
    width: 460,
    height: 288,
    label: "PRIOR WORK",
    title: data.leftTitle,
    body: "",
  });
  addCard(slide, ctx, {
    left: 620,
    top: 246,
    width: 460,
    height: 288,
    label: "THIS PROJECT",
    title: data.rightTitle,
    body: "",
  });
  addBulletList(slide, ctx, data.leftItems, {
    left: 118,
    top: 326,
    width: 390,
    gap: 66,
    fontSize: 18,
    rowHeight: 50,
    bulletColor: theme.colors.sage,
  });
  addBulletList(slide, ctx, data.rightItems, {
    left: 642,
    top: 326,
    width: 390,
    gap: 66,
    fontSize: 18,
    rowHeight: 50,
  });
  addCard(slide, ctx, {
    left: 96,
    top: 566,
    width: 984,
    height: 82,
    label: "ONE-LINE POSITIONING",
    title: data.bottomClaim,
    titleSize: 21,
    body: "",
    fill: "#EEE5D8",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });
  return slide;
}

function renderCards3(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page);
  data.cards.forEach((card, index) => {
    addCard(slide, ctx, {
      left: 96 + index * 344,
      top: 256,
      width: 304,
      height: 324,
      label: card.label,
      title: card.title,
      body: card.body,
      bodySize: 17,
    });
  });
  return slide;
}

function renderRQH(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  addCard(slide, ctx, {
    left: 96,
    top: 240,
    width: 488,
    height: 354,
    label: "RESEARCH QUESTIONS",
    title: "",
    body: "",
  });
  addCard(slide, ctx, {
    left: 626,
    top: 240,
    width: 454,
    height: 354,
    label: "HYPOTHESES",
    title: "",
    body: "",
  });
  addBulletList(slide, ctx, data.researchQuestions, {
    left: 118,
    top: 284,
    width: 436,
    gap: 76,
    fontSize: 16,
    rowHeight: 64,
    numbered: true,
  });
  addBulletList(slide, ctx, data.hypotheses, {
    left: 648,
    top: 286,
    width: 394,
    gap: 92,
    fontSize: 17,
    rowHeight: 70,
  });
  return slide;
}

function renderComparison(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 780 });

  const top = 226;
  const rowHeight = 78;
  const lefts = { label: 96, original: 346, revised: 726 };

  [
    ["DIMENSION", 210],
    ["ORIGINAL DRAFT", 330],
    ["REVISED DRAFT", 354],
  ].forEach(([text, width], index) => {
    const left = index === 0 ? lefts.label : index === 1 ? lefts.original : lefts.revised;
    ctx.addShape(slide, {
      left,
      top,
      width,
      height: 42,
      fill: "#E9DED1",
      line: line("#E9DED1", 0),
    });
    ctx.addText(slide, {
      text,
      left,
      top: top + 6,
      width,
      height: 28,
      fontSize: 13,
      bold: true,
      color: theme.colors.accent,
      face: theme.fonts.body,
      align: "center",
      valign: "middle",
    });
  });

  data.rows.forEach((row, index) => {
    const y = top + 54 + index * rowHeight;
    [210, 330, 354].forEach((width, cellIndex) => {
      const left = cellIndex === 0 ? lefts.label : cellIndex === 1 ? lefts.original : lefts.revised;
      ctx.addShape(slide, {
        left,
        top: y,
        width,
        height: 66,
        fill: cellIndex === 0 ? "#F0E6D8" : panelFill(slide),
        line: line(panelLine(slide), 1),
      });
    });
    ctx.addText(slide, {
      text: row.label,
      left: lefts.label + 12,
      top: y + 8,
      width: 186,
      height: 50,
      fontSize: 15,
      bold: true,
      color: theme.colors.ink,
      face: theme.fonts.body,
      valign: "middle",
    });
    ctx.addText(slide, {
      text: row.original,
      left: lefts.original + 12,
      top: y + 8,
      width: 306,
      height: 54,
      fontSize: 14,
      color: theme.colors.muted,
      face: theme.fonts.body,
    });
    ctx.addText(slide, {
      text: row.revised,
      left: lefts.revised + 12,
      top: y + 8,
      width: 330,
      height: 54,
      fontSize: 14,
      color: theme.colors.ink,
      face: theme.fonts.body,
    });
  });
  return slide;
}

function renderIdentification(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page);

  data.topLabels.forEach((label, index) => {
    addTag(slide, ctx, label, {
      left: 96 + index * 258,
      top: 238,
      width: 220,
      height: 36,
      fill: index % 2 === 0 ? theme.colors.stone : "#EDE4D7",
    });
  });

  const flowBoxes = data.treatmentLabels.map((label, index) =>
    addCard(slide, ctx, {
      left: 112 + index * 258,
      top: 340,
      width: 192,
      height: 116,
      label: `ARM ${index + 1}`,
      title: label,
      body: "",
      titleSize: 18,
      fill: panelFill(slide),
      border: panelLine(slide),
    }),
  );

  addArrow(slide, flowBoxes[0], flowBoxes[1], { color: theme.colors.sage, fromSide: "right", toSide: "left" });
  addArrow(slide, flowBoxes[1], flowBoxes[2], { color: theme.colors.sage, fromSide: "right", toSide: "left" });
  addArrow(slide, flowBoxes[2], flowBoxes[3], { color: theme.colors.sage, fromSide: "right", toSide: "left" });

  addCard(slide, ctx, {
    left: 168,
    top: 514,
    width: 840,
    height: 88,
    label: "IDENTIFICATION CLAIM",
    title: data.claim,
    titleSize: 19,
    body: "",
    fill: "#EEE5D8",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });
  return slide;
}

function renderStudy1(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 780 });
  addCard(slide, ctx, {
    left: 96,
    top: 242,
    width: 460,
    height: 326,
    label: "TASK FLOW",
    title: "Corporate default-risk judgment",
    body: "",
  });
  addBulletList(slide, ctx, data.steps, {
    left: 118,
    top: 320,
    width: 404,
    gap: 64,
    fontSize: 16,
    rowHeight: 54,
  });

  addCard(slide, ctx, {
    left: 614,
    top: 242,
    width: 466,
    height: 182,
    label: "CONDITIONS",
    title: "",
    body: "",
  });
  data.conditions.forEach((condition, index) => {
    addTag(slide, ctx, condition, {
      left: 638 + (index % 2) * 212,
      top: 292 + Math.floor(index / 2) * 58,
      width: 180,
      height: 38,
      fill: index === 2 ? theme.colors.accentSoft : theme.colors.stone,
    });
  });

  addCard(slide, ctx, {
    left: 614,
    top: 444,
    width: 466,
    height: 124,
    label: "MAIN OUTCOMES",
    title: "",
    body: "",
  });
  data.measures.forEach((measure, index) => {
    addTag(slide, ctx, measure, {
      left: 638 + (index % 2) * 212,
      top: 486 + Math.floor(index / 2) * 38,
      width: 180,
      height: 30,
      size: 11,
      fill: "#EEE5D8",
    });
  });
  return slide;
}

function renderMechanism(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  const boxes = data.nodes.map((node, index) =>
    addCard(slide, ctx, {
      left: 76 + index * 236,
      top: 284,
      width: 192,
      height: 92,
      title: node,
      titleSize: 18,
      body: "",
      fill: index === 0 ? "#F2DED6" : panelFill(slide),
      border: panelLine(slide),
      accent: index === 0 ? theme.colors.accent : theme.colors.sage,
    }),
  );
  boxes.slice(0, -1).forEach((box, index) => {
    addArrow(slide, box, boxes[index + 1], { color: theme.colors.accent, fromSide: "right", toSide: "left" });
  });
  addCard(slide, ctx, {
    left: 96,
    top: 446,
    width: 984,
    height: 144,
    label: "WHAT IS OBSERVED",
    title: "",
    body: "",
  });
  addBulletList(slide, ctx, data.measures, {
    left: 122,
    top: 484,
    width: 900,
    gap: 28,
    fontSize: 15,
    rowHeight: 22,
    bulletColor: theme.colors.sage,
  });
  return slide;
}

function renderStudy2(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  data.variants.forEach((variant, index) => {
    addCard(slide, ctx, {
      left: 96 + index * 334,
      top: 258,
      width: 290,
      height: 278,
      label: `CONDITION ${index + 1}`,
      title: variant.title,
      body: variant.body,
      bodySize: 17,
      accent: index === 0 ? theme.colors.accent : index === 1 ? theme.colors.sage : theme.colors.gold,
    });
  });
  addCard(slide, ctx, {
    left: 96,
    top: 574,
    width: 960,
    height: 60,
    label: "EXPECTED COMPARISON",
    title: data.bottomClaim,
    titleSize: 18,
    body: "",
    fill: "#EEE5D8",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });
  return slide;
}

function renderStudy3(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 720 });
  data.topConditions.forEach((condition, index) => {
    addCard(slide, ctx, {
      left: 96 + index * 328,
      top: 256,
      width: 284,
      height: 126,
      label: `PATH ${index + 1}`,
      title: condition,
      body: "",
      titleSize: 18,
      accent: index === 0 ? theme.colors.accent : index === 1 ? theme.colors.sage : theme.colors.gold,
    });
  });
  addCard(slide, ctx, {
    left: 96,
    top: 438,
    width: 984,
    height: 172,
    label: data.formulaTitle,
    title: "",
    body: data.formulaBody,
    bodySize: 18,
    accent: theme.colors.accent,
  });
  return slide;
}

function renderMeasures(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 840 });
  addCard(slide, ctx, {
    left: 96,
    top: 248,
    width: 468,
    height: 300,
    label: "CONTROLLED DGP",
    title: "",
    body: "",
  });
  addCard(slide, ctx, {
    left: 612,
    top: 248,
    width: 468,
    height: 300,
    label: "MAIN OUTCOMES",
    title: "",
    body: "",
  });
  data.leftPairs.forEach(([key, value], index) => addKeyValue(slide, ctx, key, value, { left: 118, top: 292 + index * 58, keyWidth: 130, valueWidth: 300 }));
  data.rightPairs.forEach(([key, value], index) => addKeyValue(slide, ctx, key, value, { left: 634, top: 292 + index * 58, keyWidth: 130, valueWidth: 300 }));
  addCard(slide, ctx, {
    left: 96,
    top: 580,
    width: 984,
    height: 52,
    label: "MODELING CHOICE",
    title: data.bottomClaim,
    titleSize: 16,
    body: "",
    fill: "#EEE5D8",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });
  return slide;
}

function renderContributions(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  data.cards.forEach((card, index) => {
    addCard(slide, ctx, {
      left: 96 + (index % 2) * 496,
      top: 246 + Math.floor(index / 2) * 174,
      width: 428,
      height: 138,
      label: card.label,
      title: card.title,
      body: card.body,
      bodySize: 16,
    });
  });
  return slide;
}

function renderGovernance(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 860 });
  data.tiers.forEach((tier, index) => {
    addCard(slide, ctx, {
      left: 96 + index * 330,
      top: 258,
      width: 286,
      height: 332,
      label: `RISK TIER ${index + 1}`,
      title: tier.title,
      body: "",
      accent: index === 0 ? theme.colors.sage : index === 1 ? theme.colors.gold : theme.colors.accent,
    });
    addBulletList(slide, ctx, tier.items, {
      left: 118 + index * 330,
      top: 342,
      width: 236,
      gap: 72,
      fontSize: 17,
      rowHeight: 58,
      bulletColor: index === 0 ? theme.colors.sage : index === 1 ? theme.colors.gold : theme.colors.accent,
    });
  });
  return slide;
}

function renderStrengths(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 720 });
  data.points.forEach((point, index) => {
    addCard(slide, ctx, {
      left: 96 + (index % 2) * 498,
      top: 246 + Math.floor(index / 2) * 166,
      width: 430,
      height: 130,
      label: `STRENGTH ${index + 1}`,
      title: point,
      titleSize: 18,
      body: "",
      accent: index % 2 === 0 ? theme.colors.accent : theme.colors.sage,
    });
  });
  return slide;
}

function renderUpdates(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  data.suggestions.forEach((item, index) => {
    addCard(slide, ctx, {
      left: 96,
      top: 216 + index * 84,
      width: 984,
      height: 64,
      label: `UPDATE ${index + 1}`,
      title: item,
      titleSize: 16,
      body: "",
      accent: index === 0 ? theme.colors.accent : index === 1 ? theme.colors.sage : index === 2 ? theme.colors.gold : theme.colors.accent,
    });
  });
  return slide;
}

function renderTakeaways(presentation, ctx, data, page) {
  const slide = standardSlide(presentation, ctx, data, page, { titleWidth: 760 });
  data.takeaways.forEach((item, index) => {
    addCard(slide, ctx, {
      left: 96 + index * 330,
      top: 280,
      width: 282,
      height: 184,
      label: `TAKEAWAY ${index + 1}`,
      title: item,
      titleSize: 20,
      body: "",
      accent: index === 0 ? theme.colors.accent : index === 1 ? theme.colors.sage : theme.colors.gold,
    });
  });
  addCard(slide, ctx, {
    left: 96,
    top: 528,
    width: 984,
    height: 72,
    label: "CLOSING",
    title: data.closing,
    titleSize: 18,
    body: "",
    fill: "#EEE5D8",
    border: theme.colors.stone,
    accent: theme.colors.gold,
  });
  return slide;
}

function renderQa(presentation, ctx, data, page) {
  const slide = baseSlide(presentation, ctx, { dark: true });
  addKicker(slide, ctx, data.kicker, { color: theme.colors.gold, textColor: theme.colors.gold });
  addTitle(slide, ctx, data.title, {
    left: 96,
    top: 164,
    width: 560,
    height: 110,
    size: 42,
    color: theme.colors.white,
  });
  addSubtitle(slide, ctx, "I welcome questions on identification, measurement, and practical governance design.", {
    left: 96,
    top: 286,
    width: 640,
    height: 60,
    size: 20,
    color: "#D7DCE7",
  });
  data.prompts.forEach((prompt, index) => {
    addTag(slide, ctx, prompt, {
      left: 800,
      top: 200 + index * 78,
      width: 300,
      height: 44,
      fill: "#304264",
      color: theme.colors.white,
      size: 14,
    });
  });
  addFooter(slide, ctx, data.sources, page);
  return slide;
}

export async function renderSlideByIndex(presentation, ctx, index) {
  const data = slideData[index - 1];
  if (!data) {
    throw new Error(`No slide data found for slide ${index}.`);
  }

  switch (data.kind) {
    case "cover":
      return renderCover(presentation, ctx, data, index);
    case "thesis":
      return renderThesis(presentation, ctx, data, index);
    case "sequence":
      return renderSequence(presentation, ctx, data, index);
    case "literature":
      return renderLiterature(presentation, ctx, data, index);
    case "gap":
      return renderGap(presentation, ctx, data, index);
    case "cards3":
      return renderCards3(presentation, ctx, data, index);
    case "rqh":
      return renderRQH(presentation, ctx, data, index);
    case "comparison":
      return renderComparison(presentation, ctx, data, index);
    case "identification":
      return renderIdentification(presentation, ctx, data, index);
    case "study1":
      return renderStudy1(presentation, ctx, data, index);
    case "mechanism":
      return renderMechanism(presentation, ctx, data, index);
    case "study2":
      return renderStudy2(presentation, ctx, data, index);
    case "study3":
      return renderStudy3(presentation, ctx, data, index);
    case "measures":
      return renderMeasures(presentation, ctx, data, index);
    case "contributions":
      return renderContributions(presentation, ctx, data, index);
    case "governance":
      return renderGovernance(presentation, ctx, data, index);
    case "strengths":
      return renderStrengths(presentation, ctx, data, index);
    case "updates":
      return renderUpdates(presentation, ctx, data, index);
    case "takeaways":
      return renderTakeaways(presentation, ctx, data, index);
    case "qa":
      return renderQa(presentation, ctx, data, index);
    default:
      throw new Error(`Unsupported slide kind: ${data.kind}`);
  }
}
