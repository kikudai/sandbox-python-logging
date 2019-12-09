import logging
from my_pac.mod01 import Mod01
from my_pac.mod02 import Mod02


# my_package.my_moduleのみに絞ってsys.stderrにlogを出す
# 最初に呼び出しが必要(注釈も参考のこと)。 defaultはlevel=logging.WARNING
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s[%(levelname)-5s][%(name)10s.%(funcName)-10s] %(message)s"
)

logging.getLogger("my_pac.mod01").setLevel(level=logging.INFO)

mod01 = Mod01()
mod01.do()

mod02 = Mod02()
mod02.do()
