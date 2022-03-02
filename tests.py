import utils
import config

#	bad request tests 400
def	test_1():
#	invalid request_line 
	http_request = 'GET / hamid HTTP/1.1\r\nHost: {}:{}\r\n\r\n'.format(config.SERVER_ADDR, config.SERVER_PORT)
	http_response = utils.send_request(http_request)

	utils.pretty_print('invalid request_line', http_response.status == 400)

#	multiple header fields with the same field name	duplicated_headers
	http_request = 'GET /youcef HTTP/1.1\r\nHost: {}:{}\r\nHost: {}:{}\r\n\r\n'.format(config.SERVER_ADDR, config.SERVER_PORT, config.SERVER_ADDR, config.SERVER_PORT)
	http_response = utils.send_request(http_request)

	print(http_response.status)
	utils.pretty_print('duplicated_headers', http_response.status == 400)

#	invalid Content-Length	
	http_request = 'GET / HTTP/1.1\r\nHost: localhost8080\r\nContent-Length: -1\r\n\r\n'
	http_response = utils.send_request(http_request)

	utils.pretty_print('invalid Content-Length', http_response.status == 400)

#	payload too large
	http_request = 'GET / HTTP/1.1\r\nHost: localhost8080\r\nContent-Length: 2147483648\r\n\r\n'
	http_response = utils.send_request(http_request)

	utils.pretty_print('playload too large', http_response.status == 413)

#	unsupported protocol 505	>1.1
	http_request = 'GET / HTTP/1.2\r\nHost: localhost8080\r\nContent-Length: 0\r\n\r\n'
	http_response = utils.send_request(http_request)

	utils.pretty_print('protocol greater than http/1.1', http_response.status == 505)