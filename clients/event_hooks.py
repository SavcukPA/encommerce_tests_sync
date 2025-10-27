from httpx import Request, Response
import logging

logger = logging.getLogger("HTTP_CLIENT")


def log_request_event_hook(request: Request):
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )
