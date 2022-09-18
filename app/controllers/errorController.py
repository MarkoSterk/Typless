from flask import (jsonify, make_response, render_template, request, Response)
from werkzeug.exceptions import HTTPException

"""
Error handling controllers.

AppError <- controller for raising/returning predictable app errors

catchError <- catches unexpected/breaking errors and returns error message.

error_response <- sends response if any kind of error is encountered 
                    (seperates between API and public routes)
"""

##function for raising exceptions when needed.
def AppError(msg: str, statusCode: int, error: str = 'Error') -> Response:
    response = jsonify({
        'status': error,
        'message': msg,
        'code': statusCode
        })
    response = make_response(response)
    return response, statusCode


##try-except "watcher" function
def catchError():
  '''
  Catches all expected and unexpected errors in the app.
  '''
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         return f(*args,**kwargs)
      except Exception as e:
        return error_response(e)
    return applicator
  return decorate


def error_response(e: Exception) -> Response:
    if isinstance(e, HTTPException):
      if request.path.startswith('/api/'):
          ##return JSON response if request was made to the API endpoints
          return AppError(e.description, e.code, 'error')
      return render_template('public/error.html', error=e)
    
    e = {'name': 'Internal server error', 'description': 'Something went wrong', 'code': 500}
    if request.path.startswith('/api/'):
      return AppError(e['description'], e['code'], 'error')
    return render_template('public/error.html', error=e)
