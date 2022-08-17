import json
import math
# import requests
MAX_VALUE = 10000

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": NextNPrimesUnderTenThousand(9,3),
            # "location": ip.text.replace("\n", "")
        }),
    }
def NextNPrimesUnderTenThousand(startingnumber, primesToSkip):
    # Mark all numbers as prime
    list_numbers = MAX_VALUE * [True] 

    # 0 and 1 not primes
    list_numbers[0] = list_numbers[1] = False

    square_root = int(math.sqrt(MAX_VALUE))

    for p in range(square_root) :
        if (list_numbers[p] == True) :
            for i in range (p*p, MAX_VALUE, p) : 
                # Cross out non primes by marking them false
                list_numbers[i] = False
    count = 0
    for p in range(startingnumber,len(list_numbers)) :
        if(list_numbers[p] == True) :
           count += 1
           if(count == primesToSkip):
            return p
