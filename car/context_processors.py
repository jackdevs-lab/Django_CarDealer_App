# This file is needed for  passing variable to base.html
from .models import Ads

def ad_processor(request):
    popup_ad = Ads.objects.all()
    return {
        'ad': popup_ad[0] if popup_ad.exists() else None  # Check if the queryset is not empty
    }
