#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: rufeng

from framework.base_page import BasePage

class OrderPage(BasePage):
    # 订单的买家昵称，根据文本定位
    buyernick = 'x=>//span[text()="%s"]%nickname'
    # 打印快递单按钮
    PrintExpress = 'x=>//*[@id="PrintExpressTipsPra"]'
    # 快递单模板，根据模板名称定位
    waybilltemplete = 'x=>//span[text()="顺丰热敏210mm"]'
    # 打印机
    printer = 'x=>//*[@id="modal_4"]/div[1]/div/div/div[3]/form/div[5]/select'
    # 打印按钮
    print = 'x=>//*[@id="modal_4"]/div[2]/a[2]'
    # 确定打印按钮
    yesbutton = 'x=>/html/body/div[10]/div[7]/div/button'
    # 发货按钮
    consignBtn = 'x=>/html/body/div[5]/div[6]/div/div/div/div/div/span[4]/button'
    # 发货合计
    consignment = 'x=>// *[ @ id = "consignModel"]/div[1]'
    # 确定发货按钮
    qdConsign = 'x=>//*[@id="qdConsign"]'
    # 发货结果信息
    consignResult = 'x=>//*[@id="consignResult"]/div[1]'
    # 确定，关掉发货弹框
    confirm_close = 'x=>//*[@id="consignResult"]/div[4]/a'
# ------------------ 添加模板 -----------------------
    # 添加模板按钮
    add_templete = 'x=>//*[@id="addping_div"]/div[4]/form/ul/li[3]/a/i'
    # 选择物流公司
    Logistics_company = 'x=>//*[@id="select2-imgType_selectVal-container"]'
    # 要添加的模版名称
    templete_name = 'x=>//label[text()="顺丰热敏180mm"]'
    # 运费付款方式
    paytype = 'x=>//label[text()="寄付现结"]'
    # 添加按钮
    add = 'x=>//a[@id="saveWaybillTemplateBtn"]'
    # 添加完成的确定按钮
    button = 'x=>/html/body/div[10]/div[7]/div/button'
    # 关掉添加模板弹窗
    button1 = 'x=>//*[@id="expressSet_os"]/button'

    # 关掉添加模板弹窗
    def template_close(self):
        self.click(self.button1)

    # 点击添加完成的确定按钮
    def click_button(self):
        self.click(self.button)

    # 点击添加按钮
    def click_add(self):
        self.click(self.add)

    # 选择运费付款方式
    def click_paytype(self):
        self.click(self.paytype)

    # 点击要添加的模板
    def click_templete(self):
        self.click(self.templete_name)

    # 点击物流公司下拉框
    def click_Logistics_company(self):
        self.click(self.Logistics_company)

    # 点击添加模板按钮
    def click_add_template(self):
        self.click(self.add_templete)

    # 点击打印订单
    def click_print(self):
        self.click(self.PrintExpress)
    # 选择打印机
    def choose_printer(self,printer):
        self.select_drop_list(self.printer,printer)
    # 点击打印
    def click_print1(self):
        self.click(self.print)
    # 确定打印
    def yes_print(self):
        self.click(self.yesbutton)

    # 点击确认发货
    def click_consignBtn(self):
        self.click(self.consignBtn)
    # 获取发货合计文本
    def get_consignment_info(self):
        consignment_info = self.get_text(self.consignment)
        return consignment_info
    # 点击确定
    def click_qdConsign(self):
        self.click(self.qdConsign)
    # 获取发货结果信息
    def get_consignResult_info(self):
        consignResult_info = self.get_text(self.consignResult)
        return consignResult_info
    # 点击确定，关闭发货弹窗
    def click_confirm_close(self):
        self.click(self.confirm_close)





