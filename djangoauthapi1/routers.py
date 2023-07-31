from rest_framework import routers
from products.views import ProductViewset
router = routers.SimpleRouter()
router.register('products',ProductViewset)