# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb, .py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import datetime 


# + {"code_folding": []}
def create_date_list(datestart = None,dateend = None): 
    # 创建日期辅助表，返回为list
    
    if datestart is None: 
        datestart = '2016-01-01' 
    if dateend is None: 
        dateend = datetime.datetime.now().strftime('%Y-%m-%d') 
    
    # 转为日期格式 
    datestart=datetime.datetime.strptime(datestart,'%Y-%m-%d') 
    dateend=datetime.datetime.strptime(dateend,'%Y-%m-%d') 
    date_list = [] 
    date_list.append(datestart.strftime('%Y-%m-%d')) 
    while datestart<dateend: 
        # 日期叠加一天 
        datestart+=datetime.timedelta(days=+1) 
        # 日期转字符串存入列表 
        date_list.append(datestart.strftime('%Y-%m-%d')) 
    
    #print(date_list)
    return date_list


# -

date_list = create_date_list('2019-03-04', '2019-05-04')
type(date_list)
