# Есть площадка для продавцом цветами.
# Задача: написать модели, которые позволят:
# 1) Делить юзеров на продавцов и покупателей(продавцы не могут быть покупателями)
# 2) Создавать продавцам лоты с информацией о виде цветка(ромашка/тюльпан и т.п.),
#    его оттенка(перечень оттенков ограничен и известен заранее), количестве товара этого вида, цене за один товар
# 3) Продавец может выбирать: отображать выбранный лот покупателям или нет
# 4) Покупатели могу оставлять отзывы на лоты и продавца
# 5) Отслеживать сделки
#
# В конце написать скрипт, который будет возвращать информацию в виде списка
# продавцов с перечнем покупателей, которые делали покупку у этого продавца и общей суммой покупок


from django.db import models


# Продавец
class Seller(models.Model):
    lastname = models.CharField("Фамилия", max_length=50, null=False)
    firstname = models.CharField("Имя", max_length=50, null=False)

    def __str__(self):
        return f"{self.lastname} {self.firstname}"


# Покупатель
class Customer(models.Model):
    lastname = models.CharField("Фамилия", max_length=50, null=False)
    firstname = models.CharField("Имя", max_length=50, null=False)

    def __str__(self):
        return f"{self.lastname} {self.firstname}"


# Цветок
class Flower(models.Model):
    name = models.CharField("Название", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


# Оттенок
class Shade(models.Model):
    name = models.CharField("Название", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


# Лот
class Lot(models.Model):
    seller = models.ForeignKey(
        "Seller",
        on_delete=models.PROTECT,
        verbose_name="Продавец",
        related_name="seller_lot",
    )
    flower = models.ForeignKey(
        "Flower",
        on_delete=models.PROTECT,
        verbose_name="Цветок",
        related_name="flower_lot",
    )
    shade = models.ForeignKey(
        "Shade",
        on_delete=models.PROTECT,
        verbose_name="Оттенок",
        related_name="flower_shade_lot",
    )
    price = models.IntegerField(verbose_name="Цена за единицу", default=0)
    count = models.IntegerField(verbose_name="Количество единиц", default=0)
    is_hidden = models.BooleanField(verbose_name="Скрыть лот", default=False)

    def __str__(self):
        return f"{self.seller} - {self.flower} {self.shade}"


# Отзыв на лот
class LotReview(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        verbose_name="Покупатель",
        related_name="customer_lot_review",
    )
    lot = models.ForeignKey(
        "Lot",
        on_delete=models.PROTECT,
        verbose_name="Лот",
        related_name="lot_review",
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.customer} о {self.lot}"


# Отзыв на продавца
class SellerReview(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        verbose_name="Покупатель",
        related_name="customer_seller_review",
    )
    seller = models.ForeignKey(
        "Seller",
        on_delete=models.PROTECT,
        verbose_name="Продавец",
        related_name="seller_review",
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.customer} о {self.seller}"


# Сделка
class Deal(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        verbose_name="Покупатель",
        related_name="customer_deal",
    )
    lot = models.ForeignKey(
        "Lot",
        on_delete=models.PROTECT,
        verbose_name="Лот",
        related_name="lot_deal",
    )
    price = models.IntegerField(verbose_name="Цена сделки", default=0)
    count = models.IntegerField(verbose_name="Количество единиц", default=0)

    def __str__(self):
        return f"{self.customer} - {self.lot}"
