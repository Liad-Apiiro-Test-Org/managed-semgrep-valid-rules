import logging

logger = logging.getLogger(__name__)


def report(request):
    name = request.args.get("name")
    logger.info("received %s", name)
    print(name)
