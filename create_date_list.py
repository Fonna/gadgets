# -*- coding: utf-8 -*-

import datetime


def create_date_list(datestart=None, dateend=None, default_start='2016-01-01'):
    # 创建日期辅助表，返回为list

    try:
        if datestart is None:
            datestart = default_start
        if dateend is None:
            dateend = datetime.datetime.now().strftime('%Y-%m-%d')

        # 转为日期格式
        start_date = datetime.datetime.strptime(datestart, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(dateend, '%Y-%m-%d')

        if start_date > end_date:
            raise ValueError("Start date cannot be later than end date")

        # 使用列表推导式生成日期列表
        date_list = [
            (start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
            for i in range((end_date - start_date).days + 1)
        ]

        return date_list

    except ValueError as e:
        print(f"Invalid date format or logic error: {e}")
        return []

# 测试代码
date_list = create_date_list('2019-03-04', '2019-05-04')
print(type(date_list))
print(date_list)