from django.conf import settings
from main.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) # получаем сессию пользователя (его корзину)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart: # если нет айди продукта, то добавляем в корзину
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save() # не забываем сохранять корзину нашу

    def save(self):
        self.session.modified = True # говорим фреймворку, что мы сессию поменяли, он заменяет и сохраняет

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart: # если айдишник продукта есть в корзине, то удалем его + сохраняем корзину
            del self.cart[product_id]
            self.save()

    def __iter__(self): # выводит все параметры, которые есть в корзине
        product_ids = (self.cart.keys())
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product # сопоставляем айдишники

        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        '''Удаляет не все куки(сессию), а только те, которые связаны с корзиной'''
        del self.session[settings.CART_SESSION_ID]
        self.save()