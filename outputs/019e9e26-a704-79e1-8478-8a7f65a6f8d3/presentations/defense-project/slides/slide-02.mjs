import { renderSlideByIndex } from "./build-slide.mjs";

export async function slide02(presentation, ctx) {
  return renderSlideByIndex(presentation, ctx, 2);
}
