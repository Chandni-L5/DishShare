# All code is provided via chatgpt

# recipe_post/templatetags/safe_media.py
from django import template

register = template.Library()


@register.filter
def safe_url(image_field):
    """
    Return image_field.url if available; otherwise return empty string.
    Prevents template crashes when the file is missing or storage raises.
    """
    try:
        if image_field:
            return image_field.url
    except Exception:
        pass
    return ""
