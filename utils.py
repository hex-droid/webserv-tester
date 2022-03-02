import socket
import config
from http.client import HTTPResponse

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

def	send_request(request_header):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((config.SERVER_ADDR, config.SERVER_PORT))
	s.send(request_header.encode())

	http_response = HTTPResponse(s)
	http_response.begin()

	return http_response

def	pretty_print(test_number, cond):
	if cond:print("{}{}{}{}{}OK{}".format(color.BLUE, test_number, color.END, ' '*(60 - len(test_number)),color.GREEN, color.END))
	else:print("{}{}{}KO{}".format(color.BLUE, test_number, color.END, ' '*(60 - len(test_number)),color.RED, color.END))
