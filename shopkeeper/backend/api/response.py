from rest_framework.response import Response

def SuccessResponse(response):
	response_dict = {}
	response_dict['result'] = True
	response_dict['data'] = response
	return Response(response_dict)

def UnauthorizedResponse():
	response_dict = {}
	response_dict['status'] = 'unauthorized'
	return Response(response_dict)

def ErrorResponse(message):
	response_dict = {}
	response_dict['status'] = 'error'
	response_dict['message'] = message
	return Response(response_dict)

def UpdateAppResponse(message):
	response_dict = {}
	response_dict['update'] = message
	return Response(response_dict)


