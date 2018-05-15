#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

from framework.base_page import BasePage

class OrderPage(BasePage):
    #订单的买家昵称，根据文本定位
    buyernick = 'x=>//span[text()="%s"]%nickname'
    #打印快递单按钮
    PrintExpress = 'x=>//*[@id="PrintExpressTipsPra"]'
    #快递单模板，根据模板名称定位
    waybilltemplete = 'x=>//span[text()="顺丰热敏210mm"]'
    #打印机
    printer = 'x=>//*[@id="modal_4"]/div[1]/div/div/div[3]/form/div[5]/select'
    #打印按钮
    print = 'x=>//*[@id="modal_4"]/div[2]/a[2]'
    #确定打印按钮
    yesbutton = 'x=>/html/body/div[10]/div[7]/div/button'




    #点击打印订单
    def click_print(self):
        self.click(self.PrintExpress)

    #选择模板
    def choose_templete(self):

        self.click(self.waybilltemplete)
    #选择打印机
    def choose_printer(self,printer):
        self.select_drop_list(self.printer,printer)

    #点击打印
    def click_print1(self):
        self.click(self.print)

    #确定打印
    def yes_print(self):
        self.click(self.yesbutton)



