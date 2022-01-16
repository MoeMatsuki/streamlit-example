# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import pickle5


def main():
    # Streamlit が対応している任意のオブジェクトを可視化する (ここでは文字列)
    pklfile_path = "data/202111_catch_tissuepaper/2021-11-14-17-28-07-129_0.pkl"
    with open(pklfile_path, "rb") as fh:
            df =  pickle5.load(fh)
    pr = df.profile_report()

    st_profile_report(pr)


if __name__ == '__main__':
    main()
