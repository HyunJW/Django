import os.path
from django.shortcuts import HttpResponse
from shop.models import Product
from shop import ProductSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

def list(request):
    # 상품목록 - 내림차순
    items = Product.objects.order_by('-product_name')
    # 객체 직렬화
    serializer = ps.ProductSerializer(items, many=True)
    return HttpResponse(simplejson.dumps(serializer.data))

@csrf_exempt
def insert(request):
    if 'img' in request.FILES:
        file = request.FILES['img']
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = '-'
    row = Product(product_name=request.POST['product_name'],
                  description=request.POST['description'],
                  price=request.POST['price'],
                  filename=file_name)
    row.save()