import logging

logger = logging.getLogger(__name__)


def report(request):
    name = request.args.get("name")
    logger.info("received %s", name)
    print(name)


def report_again(request):
    other = request.args.get("other")
    print(other)
