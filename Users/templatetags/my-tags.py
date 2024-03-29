from django import template

register = template.Library()


@register.simple_tag
def update_variable(value):
    data = value
    return data


register.filter("update_variable", update_variable)


nums = [False, False, True, False, False]
liked = False
for x in nums:
    if x == True:
        liked = True
print(liked)
