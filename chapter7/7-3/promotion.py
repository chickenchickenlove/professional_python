# promotion.py
promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


def fidelity(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.qunaity >= 20:
            discount += item.total() * .1
    return discount


def large_order(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) > 10:
        return order.total * .07
    return 0


def best_promo(order):
    """최대로 할인받을 금액을 반환한다.
    """
    return max(promo(order) for promo in promos)