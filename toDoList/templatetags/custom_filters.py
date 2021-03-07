from django import template

register = template.Library()


@register.filter(name='licss', is_safe=True)
def licss(value):
    rgb_tuple = hex_to_rgb(value)
    bgColor = "rgba(%s, %s, %s, 0.3)" % (
        rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
    style = "border-color: %s;background-color: %s;" % (value, bgColor)
    return style


@register.filter(name='typecss', is_safe=True)
def typecss(value):
    rgb_tuple = hex_to_rgb(value)
    return "color:rgb(%s,%s,%s)" % (deepColor(rgb_tuple[0]), deepColor(rgb_tuple[1]), deepColor(rgb_tuple[2]))


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


def deepColor(value):
    value -= 100
    return value if value > 0 else 0
