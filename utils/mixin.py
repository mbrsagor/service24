from django.conf import settings


def base_url():
    url = settings.SITE_URL
    uri = url.replace('/', '')
    return uri


# When issue will transfer to contractor the body will call transfer issue view.
def transfer_issue_body(title, budget, property_unit):
    msg = f"Dear contractor,\n\nwe have been transfer issue.\nIssue name: {title}\nIssue price: {budget}\nProperty unit:{property_unit}"
    return msg


# Date time convert
def time_convertor(seconds):
    minute, sec = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return '%d:%02d:%02d' % (hour, minute, sec)
