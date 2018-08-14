#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng
import time

from framework.base_page import BasePage


class Ordercreate(BasePage):
    createOrderBtn = 'x=>//*[@id="createOrderBtn"]'     # 新建订单按钮
    receiverName = 'x=>//*[@id="createOrderTPL"]/form/div[1]/div[2]/div/div[1]/div[2]/div[1]/input'    # 收件人姓名
    receiverPhone = 'name=>receiverPhone'    # 收件人电话
    receiverMobile = 'name=>receiverMobile'     # 收件人手机
    province = 'name=>province'     # 收件人省份
    city = 'name=>city'    # 收件人城市
    district = 'name=>district'    # 收件人区
    receiverAddress = 'x=>//*[@id="address"]'    # 收件人详细地址
    codAmount = 'name=>codAmount'    # 代收货款金额
    sellerMessage = 'name=>sellerMessage'   # 卖家备注
    goodsNo = 'name=>goodsNo'      # 商品编码
    goodsName = 'x=>//*[@id="goodsInfoBody"]/tr/td[3]/input'     # 商品标题
    goodsProps = 'name=>goodsProps'    # 销售属性
    quantity = 'name=>quantity'     # 商品数量
    price = 'name=>price'    # 商品单价
    confirmCreateOrder = 'name=>confirmCreateOrder'  # 确定新建按钮
    createSuccess = 'x=>/html/body/div[8]/h2'  # 新建成功提示
    confirm = 'x=>/html/body/div[8]/div[7]/div/button'   # 确定，关掉新建成功提示

    # 点击手工新建按钮
    def click_createOrderBtn(self):
        self.click(self.createOrderBtn)
    # 输入收件人姓名
    def type_receiverName(self,text):
        self.type(self.receiverName,text)
    def type_receiverPhone(self,text):
        self.type(self.receiverPhone,text)
    def type_receiverMobile(self,text):
        self.type(self.receiverMobile,text)
    def type_province(self,text):
        self.type(self.province,text)
    def type_city(self,text):
        self.type(self.city,text)
    def type_district(self,text):
        self.type(self.district,text)
    def type_receiverAddress(self,text):
        self.type(self.receiverAddress,text)
    def type_codAmount(self,text):
        self.type(self.codAmount,text)
    def type_sellerMessage(self,text):
        self.type(self.sellerMessage,text)
    def type_goodsNo(self,text):
        self.type(self.goodsNo,text)
    def type_goodsName(self,text):
        self.type(self.goodsName,text)
    def type_goodsProps(self,text):
        self.type(self.goodsProps,text)
    def type_quantity(self,text):
        self.type(self.quantity,text)
    def type_price(self,text):
        self.type(self.price,text)
    def click_confirmCreateOrder(self):
        self.click(self.confirmCreateOrder)
    def get_tips(self):
        tips = self.get_text(self.createSuccess)
        return tips
    def click_confirm(self):
        self.click(self.confirm)

    def skin01_order_create(self,ordermsg):
        # 初始化订单新建页面
        # ordercreatepage = Ordercreate(self.driver)
        time.sleep(3)
        # 切换frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        self.click_createOrderBtn()
        time.sleep(3)
        self.type_receiverName(ordermsg[0])
        self.type_receiverMobile(ordermsg[1])
        self.type_province(ordermsg[2])
        self.type_city(ordermsg[3])
        self.type_district(ordermsg[4])
        self.type_receiverAddress(ordermsg[5])
        self.driver.find_element_by_xpath('//*[@id="createOrderTPL"]/form/div[1]/div[3]/ul/li[2]/a').click()
        self.type_goodsName(ordermsg[6])
        self.click_confirmCreateOrder()
        tips = self.get_tips()
        try:
            assert u"新建订单成功" in tips
            print('Assertion test pass.')
        except Exception as e:
            print('Assertion test fail.', format(e))
        time.sleep(1)
        self.click_confirm()
        time.sleep(1)










