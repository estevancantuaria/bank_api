from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unauthorized import HttpUnauthorizedError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnauthorizedError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]    
            },
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "InternalServerError",
                "detail": str(error)
            }]
        }
    )