from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class Mypagination1(PageNumberPagination):
	page_size=5
	page_query_param='sandesh'
	page_size_query_param='number'
	max_page_size=10
	last_page_strings=('suhas',)

class Mypagination2(LimitOffsetPagination):
	default_limit=15
	limit_query_param='mylimit'
	offset_query_param='myoffset'
	max_limit=20

class Mypagination3(CursorPagination):
	ordering='-esalary'
	page_size=5