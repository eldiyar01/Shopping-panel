from django import template


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def sum_costs(query):
    total_cost = 0
    total_dis = 0
    for item in query:
        total_cost += item.cost
        total_dis += item.discount
    total = total_cost - total_dis
    total_day = [total_cost, total_dis, total]
    return total_day


@register.filter
def index(args, i):
    return args[i]

