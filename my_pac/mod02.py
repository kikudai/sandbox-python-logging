import logging
# __name__はこのモジュールの名前
logger = logging.getLogger(__name__)


class Mod02():
    def __init__(self):
        pass

    def do(self):
        # do sth
        # おもに問題を診断するときにのみ関心があるような、詳細な情報。
        logger.debug("test")
        # 想定された通りのことが起こったことの確認。
        logger.info("info")


def do():
    # do sth
    logger.debug("Mod02")
