import { describe, it, expect, beforeEach, jest } from "@jest/globals";
import { MailSender } from "../mail-sender";

class MockRequest {}

class MockHttpClient {
  post(baseUrl: string, request: Object): any {}
}

describe("MailSender", () => {
  let mailSender: MailSender;
  let mockHttpClient: MockHttpClient;

  beforeEach(() => {
    mockHttpClient = new MockHttpClient();
    mailSender = new MailSender(mockHttpClient);
  });

  describe("sendV1", () => {
    it("should create and send a SendMailRequest with the correct parameters", () => {
      const user = { name: "John Doe", email: "john.doe@example.com" };
      const message = "Test message";

      const postSpy = jest.spyOn(mockHttpClient, "post");

      mailSender.sendV1(user, message);

      expect(postSpy).toHaveBeenCalledWith(
        mailSender.baseUrl,
        expect.objectContaining({
          recipient: user.email,
          subject: "New notification",
          body: message,
        })
      );
    });
  });
});
