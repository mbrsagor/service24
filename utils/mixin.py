from django.conf import settings


def base_url():
    url = settings.SITE_URL
    uri = url.replace('/', '')
    return uri


# When issue will tranfered to contractor the body will call tranfer issue view.
def transfer_issue_body(title, budget, property_unit):
    msg = f"Dear contractor,\n\nwe have been transfer issue.\nIssue name: {title}\nIssue price: {budget}\nProperty unit:{property_unit}"
    return msg


def transfer_issue_notify_admin(status, title, budget, property_unit):
    """
    Name: Transfer issue status.
    Desc: When contractor will update their work status will be change from here.
    :params `CONFIRM`, `PROGRESS`, `REJECTED`, `FINISHED`
    """
    msg = f"Dear Admin,\n{status}.\nIssue name: {title}\nIssue price: {budget}\nProperty unit:{property_unit}"
    return msg


# Assign issue crew/worker
def assgin_issue_body(user, title, date, address):
    msg = f"Dear {user}\n\nwe have assign a new issue please check the issuse details below.Issue name: {title}\nIssue date line: {date}\nCustomer address: {address}"
    return msg


# Worker completed issue mail body
def completed_issue_body(user, title, date, address):
    msg = f"Dear {user},\n\nYour issue has been successfully completed! please check the issuse details below.\nIssue name: {title}\nIssue date line: {date}\nCustomer address: {address}"
    return msg




# Date time convator
def time_convartor(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d:%02d:%02d' % (hour, min, sec)

