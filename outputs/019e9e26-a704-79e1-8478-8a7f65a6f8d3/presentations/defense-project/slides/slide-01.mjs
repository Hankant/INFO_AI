import { renderSlideByIndex } from "./build-slide.mjs";

export async function slide01(presentation, ctx) {
  return renderSlideByIndex(presentation, ctx, 1);
}
