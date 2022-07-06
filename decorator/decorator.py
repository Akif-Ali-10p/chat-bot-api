from route.route import *
from functools import wraps
from constant.constant import SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorated (*args, **kwargs):
        token=request.headers.get('token1') 
        print(token)
        if not token:
            return jsonify({'message':'Token is missing'}),403
        try:
            # data=jwt.decode(token,app.config['SECRET_KEY'])
            print(SECRET_KEY)
            data=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
        except (jwt.DecodeError, jwt.InvalidTokenError) as e:
            print(e)
            return jsonify({'message':'Token is invalid'}),403
        return f(*args,**kwargs)

    return decorated
