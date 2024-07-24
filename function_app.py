import logging
import uuid
import sys
import time
import jwt
import os
import base64
import json
import math
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_qlikcloud_jwt_token")
def http_trigger_qlikcloud_jwt_token(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        private_key = base64.b64decode(os.environ['private_key'])
        issuer = os.environ['issuer']
        kid = os.environ['kid']

        new_GUID = str(uuid.uuid4())
        def create_JWT(private_key, GUID):
            sub = 'ANON\\' + GUID
            name = 'Anonymous'
            email = GUID + '@example.com'
            current_time = math.trunc(time.time())
            not_before = round(current_time - 5 * 60)  # account for clock skew
            expir = round(current_time + 5 * 60)
            groups = ['anonymous']

            claim = {
                "sub": sub,
                "subType": "user",
                "name": name,
                "email": email,
                "email_verified": True,
                'iss': issuer,
                'iat': current_time,
                'nbf': not_before,
                'exp': expir,
                'jti': str(uuid.uuid4()),
                'aud': 'qlik.api/login/jwt-session',
                'groups': groups
            }

            token = jwt.encode(claim, private_key,
                               algorithm='RS256',
                               headers={'alg': 'RS256',
                                        'kid': kid,
                                        'typ': 'JWT'}
                               )

            return token

        response = create_JWT(private_key, new_GUID)

    except Exception as e:
        response = str(e)

    return func.HttpResponse(
        json.dumps({
            "body": response
        }),
        mimetype="application/json",
        status_code=200
    )