#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";

import { slideData } from "../slides/content.mjs";

const outputPath = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve("E:/Info_AI/outputs/019e9e26-a704-79e1-8478-8a7f65a6f8d3/presentations/defense-project/output/speech_script_en.md");

const lines = [
  "# English Speech Script",
  "",
  "This script follows the 20-slide defense deck and is designed for a concise proposal defense presentation.",
  "",
];

slideData.forEach((slide, index) => {
  lines.push(`## Slide ${String(index + 1).padStart(2, "0")}: ${slide.title}`);
  lines.push("");
  lines.push(slide.notes.trim());
  lines.push("");
});

await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.writeFile(outputPath, `${lines.join("\n")}\n`, "utf8");
console.log(outputPath);
