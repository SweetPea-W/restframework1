from rest_framework import routers
from .views import UserViewSet, EntryViewSet

#modelごとに登録
#下記のように設定した場合、/api/がREST APIへの入り口となっており
#GET /api/users/ でUserの一覧、
#GET /api/entries/でEntryの一覧
#  へとアクセスすることが出来ます。
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
