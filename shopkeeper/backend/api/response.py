from rest_framework.response import Response

def success_response(response):
	response_dict = {}
	response_dict['result'] = True
	response_dict['data'] = response
	return Response(response_dict)