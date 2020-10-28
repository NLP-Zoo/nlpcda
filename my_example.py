from nlpcda import EquivalentChar


if __name__ == "__main__":
    ts = '''今天是2020年3月8日11:40，天气晴朗，天气很不错。'''
    rs = EquivalentChar(create_num=3, change_rate=0.5)
    res = rs.replace(ts)
    print('等价字替换>>>>>>')
    for s in res:
        print(s)