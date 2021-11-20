import logging

from pandas.core.frame import DataFrame

logger = logging.getLogger(__name__)


class BaseCollecter:

    def check_raw_data(self, data):
        print(type(data))
        print(len(data))

    def check_data(self, data):
        print("check data ----------------------------------")
        self.check_raw_data(data)
        # print(dir(data))
        # print(data)

    def check_df(self, data: DataFrame):
        print("check data ----------------------------------")
        self.check_raw_data(data)
        # print(dir(data))
        print(data.keys())
        # print(data)

    pass
