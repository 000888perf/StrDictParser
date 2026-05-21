
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

    def __init__(self,open_log = False,help = "未填写"):
        self.ll = {}#输出的字典
        self.list = []#输入的列表
        self.ll_rule ={}
        self.dact_add = []#规则
        self.dact_name = []#设置键的名字
        self.help = help  # 帮助数据
        self.str_Status = None#是否为空字符串
        print(self.help)
        self.open_log = open_log#是否显示日志

    # 判断返回字符串是否为空
    def ptint_str_Status(self):

        print(self.str_Status)

    # 解析逻辑
    def _parse(self):

        for i in range(0, len(self.list)):
            self.ll[i] = self.list[i] #先按顺序添加数据

            if self.open_log:#日志
                print("当前解析数据",self.list[i])

            for ii in range(0, len(self.dact_add)):#每个数据都进行循环比对
                if self.list[i] == self.dact_add[ii]:
                    self.ll[self.dact_name[ii]] = self.list[i+1]
                    if self.open_log:
                        print("当前添加数据:",self.ll[self.dact_name[ii]])


            if i+1 >= len(self.list) :
                if self.open_log:
                    print("解析结束")
                return self.ll
        return self.ll

        # 添加规则
    def add_rule (self,add) -> None :

        rule_add =  add.split()
        if self.open_log:
            print("当前输入参数"+str(rule_add))
        if  '-' not in str(rule_add):
            print("格式不正确")
            return None
        else:
            self.dact_add.append(rule_add[0])
            self.dact_name.append(rule_add[1])
            self.ll_rule[rule_add[1]] = None#为了防止读取报错，填入空数据
            if self.open_log:
                print("添加规则为:"+str(rule_add[0])+",名字为:"+str(rule_add[1]),"当前存储参数:"+str(self.ll))

        rule_add = []#清空数据

    def Start(self):

        out_dict = {}

        while not self.str_Status:
            str = input("输入'-h'可获得帮助")
            self.loop_parse(str)
        return out_dict

    def loop_parse (self,input)  :
        out_dict = {}
        self.str_Status = None
        self.ll = self.ll_rule.copy()#先把规则复制到字典里，避免重置后数据清空了
        self.list = (input).split()#用空格分割数据
        try:
            if input == "":
                out_dict = self.ll
                self.mode = False
                self.str_Status = None
                if self.open_log:
                    print("字符串为空")
            elif str in ('-h', '-help'):
                print(self.help)
                self.str_Status = None
            else:
                out_dict = self._parse()
        except Exception as e:
            print(e)

        self.mode = True
        self.ll = {}#清空输出的字典
        self.list = []#清空输入的列表
        return out_dict


if __name__ == "__main__":
    a = StrDictParser (True)
    a.add_rule ("i i")
    a.add_rule ("-a a")
    a.add_rule("-n name")

    a.Start()


    #list = "-i 123   456 -n carmen 789 abc"#测试数据
    main_list = a.loop_parse(input("输入'-h'可获取帮助"))
    #main_list = a.loop_parse(list)
    print(main_list)
    print( "a is",main_list['a'])
    print("name is",main_list['name'])
    print(type(main_list['a']))
    if main_list['a'] == None:
        print("qaq")















