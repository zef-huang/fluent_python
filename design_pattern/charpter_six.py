# coding=utf-8
# 实现策略模式

from abc import ABC, abstractmethod


class Customer():
    def __init__(self, goods_cost):
        self.cost = goods_cost


class Order():
    def __init__(self, total_cost, promotion):
        self.disc = promotion.get_discount()
        self.cost = total_cost

    @property
    def should_pay(self):
        return self.disc * self.cost


class PromotionBase(ABC):
    @abstractmethod
    def get_discount(self):
        pass


class LargeOrderPromo(PromotionBase):
    '''大订单优惠
    '''
    def get_discount(self):
        return 0.7


class VIPPromo(PromotionBase):
    '''VIP 优惠
    '''
    def get_discount(self):
        return 0.9


class TicketPromo(PromotionBase):
    '''优惠券
    '''
    def get_discount(self):
        return 0.5


hzf = Customer(goods_cost=1000)
hzf_order = Order(hzf.cost, VIPPromo())
print(u"原本价格：%s, vip 优惠之后的价格：%s" % (hzf.cost, hzf_order.should_pay))
