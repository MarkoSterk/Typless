from flask import (jsonify, make_response, render_template, request)
from werkzeug.exceptions import HTTPException

"""
Error handling controllers.

AppError <- controller for raising/returning predictable app errors

handle_error: overrides the default error responses for all exception codes.
"""

##function for raising exceptions when needed.
def AppError(msg, statusCode: int, error: str = 'Error'):
    response = jsonify({
        'status': error,
        'message': msg,
        'code': statusCode
        })
    response = make_response(response)
    return response, statusCode

##try-except "watcher" function
def catchError():
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         return f(*args,**kwargs)
      except Exception as e:
        if isinstance(e, HTTPException):
            return AppError(e.description, e.code, 'error')
        return AppError('Something went wrong', 500, 'error')
    return applicator
  return decorate


def route_not_found(e):
    if request.path.startswith('/api/'):
        ##return JSON response
        return AppError(e.description, e.code, 'error')
    return render_template('public/error.html', error=e)
