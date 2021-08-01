def status(http_code):
    http_code_def = {
        403 : 'Unauthorised',
        400 : 'Client Error',
        401 : 'Missing Authorisation',
        429 : 'Too Many Requests',
        500 : 'Unknown Server Error',
        502 : 'Cannot Connect to Data Source',
        503 : 'Server Rebooting',
        200 : 'Success',
        204 : 'No Data',
    }
    return http_code_def[http_code]
if __name__ == '__main__':
    print('status.py contains information about HTTP Status Codes.')