import { test, expect } from "@jest/globals";

import { SafeCalculator } from "../safe-calculator";
test("should not throw when authorized", () => {
  // TODO: write a test that fails due to the bug in
  const safeCalculator = new SafeCalculator({ authorize: () => false });
  const result = safeCalculator.add(1, 2);
  expect(result).toBe(new Error("Not authorized"));
});
