import sys

def app(environ, start_response):
    """Simplest possible application object"""
    data = environ['QUERY_STRING']
    res = ''
    for i in data.split('&'):
        res += '%s\n' % i
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([res])