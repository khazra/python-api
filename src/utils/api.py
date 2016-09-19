from flask import jsonify, make_response


def response(**kwargs):
    return make_response(jsonify({
        'status': kwargs.get('status'),
        'message': kwargs.get('message'),
        'data': kwargs.get('data') or {}
    }), kwargs.get('status'))
