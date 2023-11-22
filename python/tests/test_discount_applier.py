import pytest
from discount_applier import DiscountApplier

def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    discount_applier, discount, users = init()

    discount_applier.apply_v1(discount,users)
    assert discount_applier.notifier.getNotifiedUsers() == users


def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    discount_applier, discount, users = init()

    discount_applier.apply_v2(discount,users)
    assert discount_applier.notifier.getNotifiedUsers() == users

def init():
    discount_applier = DiscountApplier(Notifier())
    discount = 50
    users = ["Bob","Alice","Charlie"]

    return discount_applier, discount, users


class Notifier:
    def __init__(self):
        self.notifiedUsers = []

    def notify(self,user,message):
        self.notifiedUsers.append(user)
        print(user+" "+message)
    
    def getNotifiedUsers(self):
        return self.notifiedUsers