import logging
from functools import wraps
from django.http.response import JsonResponse

logger = logging.getLogger(__name__)

def patch_jsonresponse_disable_ensure_ascii():
    if getattr(JsonResponse, '_utf8_patched', False):
        # Already patched. Add warning in logs with stack to see what location
        # is trying to patch this a second time.
        logger.warning("JSONResponse UTF8 patch already applied", stack_info=True)
        return

    logger.debug("Patching JSONResponse to disable ensure_ascii")
    orig_init = JsonResponse.__init__

    @wraps(orig_init)
    def utf8_init(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        orig_init(self, *args, json_dumps_params=json_dumps_params, **kwargs)

    JsonResponse.__init__ = utf8_init
    JsonResponse._utf8_patched = True  # to prevent accidental re-patching