import { test, expect } from "@jest/globals";
import { SafeCalculator } from "../safe-calculator";

test("should not throw when authorized", () => {
  const safeCalculator = new SafeCalculator({ authorize: () => false });
  const action = () => safeCalculator.add(1, 2);
  expect(action).toThrow(new Error("Not authorized"));
});
