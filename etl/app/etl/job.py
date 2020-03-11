from pyetl import Etl
# from app.config import default
from etl.app.config import default
from etl.app.logger import module_log
log = module_log(__file__)


def task():
    src_tab = "menu"
    # src_update = "SRC_UPDATE_FIELD"
    dst_tab = "menu"
    # dst_unique = "DST_UNIQUE"
    # mapping = {
    #     "ID": "CODE"
    # }
    app = Etl(src_tab, dst_tab,
            #   mapping=mapping,
            #   updte=src_update,
            #   unique=dst_unique
    )
    app.config(default)
    conditions = "pid=0"
    app.run(where=conditions, groupby=None, days=None)


def main():
    task()


if __name__=="__main__":
    main()
