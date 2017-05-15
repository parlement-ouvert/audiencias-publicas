from django.conf import settings


def analytics(request):
    analytics_id = settings.GOOGLE_ANALYTICS_ID
    olark_id = settings.OLARK_ID
    is_edemocracia = settings.BELONGS_TO_EDEMOCRACIA
    return {'analytics_id': analytics_id, 'olark_id': olark_id,
            'is_edemocracia': is_edemocracia}
