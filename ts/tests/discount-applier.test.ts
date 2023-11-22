import { test, describe, it, expect, beforeEach, jest } from "@jest/globals";
import { DiscountApplier, Notifier } from "../discount-applier";
import { User } from "../user";

class MockNotifier implements Notifier {
  notify(user: any, message: string): void {
    // Do nothing in the mock implementation
  }
}

describe("MockNotifier", () => {
  // TODO: write a test that fails due to the bug in

  let discountApplier: DiscountApplier;
  let mockNotifier: Notifier;

  beforeEach(() => {
    mockNotifier = new MockNotifier();
    discountApplier = new DiscountApplier(mockNotifier);
  });

  describe("applyV1", () => {
    it("should notify each user with the correct discount message", () => {
      const discount = 10;
      const users: User[] = [
        { email: "test@sfr.fr", name: "User1" },
        { email: "test2@sfr.fr", name: "User2" },
      ];

      const notifySpy = jest.spyOn(mockNotifier, "notify");

      discountApplier.applyV1(discount, users);

      expect(notifySpy).toHaveBeenCalledTimes(users.length);

      users.forEach((user, index) => {
        const expectedMessage = `You've got a new discount of ${discount}%`;
        expect(notifySpy).toHaveBeenCalledWith(user, expectedMessage);
      });
    });
  });
});
