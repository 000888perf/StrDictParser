
"""
可添加规则的自动字符串解析，返回字典
"""

class StrDictParser:
    '''
    1,函数输入参数包括 1.(帮助信息#非必填) 2.(日志开关#非必填)
    2,parse 实现逻辑
    3,loop_parse 程序入口
    4,add_rule 单个规则添加，参数为1.(规则，必须带-#必填) 2.(字典名称#必填)
    '''

    def __init__(self,help = "未填写",open_log = False):
        self.mode = True   #loop_parse循环标志符号
        self.ll = {}#输出的字典
        self.list = []#输入的列表
        self.dact_add = []#规则
        self.dact_name = []#设置键的名字
        self.help = help  # 帮助数据
        self.open_log = open_log#是否显示日志


    def _parse(self):#解析逻辑
        for i in range(0, len(self.list)):

            self.ll[i] = self.list[i] #先按顺序添加数据

            if self.open_log:#日志
                print("当前解析数据",self.list[i])

            for ii in range(0, len(self.dact_add)):#每个数据都进行循环比对
                if self.list[i] == self.dact_add[ii]:
                    self.ll[self.dact_name[ii]] = self.list[i+1]
                    if self.open_log:
                        print("当前添加数据:",self.ll[self.dact_name[ii]])

            if i >= len(self.list) - 1:
                if self.open_log:
                    print("解析结束")
                self.mode = False
                break


            elif self.list[i] in ('-h', '-help'):
                print(self.help)
                break
        return self.ll

    def add_rule (self,add) -> None :#添加规则
        rule_add =  add.split()
        if self.open_log:
            print("当前输入参数"+str(rule_add))
        if  '-' not in str(rule_add):
            print("格式不正确")
            return None
        else:
            self.dact_add.append(rule_add[0])
            self.dact_name.append(rule_add[1])
            self.ll[rule_add[1]] = None#为了防止读取报错，填入空数据
            if self.open_log:
                print("添加规则为:"+str(rule_add[0])+",名字为:"+str(rule_add[1]),"当前存储参数:"+str(self.ll))

        rule_add = []#清空数据

    def loop_parse (self,input) -> dict:
        out_dict = {}
        while self.mode == True:
            self.list = (input).split()
            try:
                out_dict = self._parse()
            except Exception as e:
                print(e)
        self.__init__()#清除数据
        return out_dict


if __name__ == "__main__":
    a = StrDictParser ("",True)
    a.add_rule ("i i")
    a.add_rule ("-a a")
    a.add_rule("-n name")
    list = "-i 123   456 -n carmen 789 abc"#测试数据
    #main_list = a.loop_parse(input("输入'-h'可获取帮助"))
    main_list = a.loop_parse(list)
    print(main_list)
    print( "a is",main_list['a'])
    print("name is",main_list['name'])
    if main_list['a'] != True:
        print("qaq")















