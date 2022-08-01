from django.shortcuts import render
from django.db.models import Sum

from .models import Deal


def sellers(request):
    deals = Deal.objects\
        .select_related("lot", "customer", "lot__seller")\
        .values("customer_id",
                "lot__seller_id",
                "customer__lastname",
                "customer__firstname",
                "lot__seller__lastname",
                "lot__seller__firstname")\
        .annotate(dsum=Sum('price'))

    result = {deal["lot__seller_id"]: {
        "seller": f"{deal['lot__seller__lastname']} {deal['lot__seller__firstname']}",
        "customers": {},
    } for deal in deals}

    for deal in deals:
        seller_id = deal["lot__seller_id"]
        new_customer = {
            deal["customer_id"]: {
                "customer": f"{deal['customer__lastname']} {deal['customer__firstname']}",
                "summa": deal["dsum"],
            }
        }
        result[seller_id]["customers"].update(new_customer)

    print(result)
    context = {
        "deals": deals
    }
    # print(deals.query)
    return render(request, 'flowers/sellers.html', context)
