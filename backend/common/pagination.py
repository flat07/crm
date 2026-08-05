# backend/common/pagination.py

from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100
    page_query_param = "page"


# {
#     "count": 143,
#     "next": "http://localhost:8000/api/companies/?page=2",
#     "previous": null,
#     "results": [
#         {
#             "id": 1,
#             "name": "ABC Ltd"
#         },
#         {
#             "id": 2,
#             "name": "XYZ Ltd"
#         }
#     ]
# }
