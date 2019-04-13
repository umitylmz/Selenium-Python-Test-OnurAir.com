
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox();


browser.get("https://www.bizimhesap.com");
browser.maximize_window()

browser.implicitly_wait(120)



browser.find_element_by_xpath('/html/body/header/div[1]/nav/div/div[1]/a[1]').click();

browser.find_element_by_xpath('//*[@id="txtUser"]').send_keys('Your User Email');


browser.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('Your Password');

browser.find_element_by_xpath('//*[@id="btnLogin"]/i').click();


a = ['List of Customer IDs'];
for name in a:
        
        print(name)
        browser.find_element_by_xpath('//*[@id="mnuMainCustomer"]/a/span').click();


        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/section/div/div[2]/div[1]/label/input').send_keys(name);



        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/section/div/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/a').click();

        browser.find_element_by_xpath('//*[@id="ngnMainContainer"]/div[2]/button[1]').click();

        browser.find_element_by_xpath('//*[@id="txtDocumentDate"]').click();






        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[2]').click();


        browser.find_element_by_xpath('//*[@id="txtDueDate"]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[5]/td[4]').click();


        browser.find_element_by_xpath('//*[@id="txtDispatchDate"]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();


        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[2]').click();


        time.sleep(2);
        browser.implicitly_wait(50000);

        element = browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]');

      


        if(element.is_displayed() and element.is_enabled()):
                element.click();
                print("firstthref1")

        browser.find_element_by_xpath('//*[@id="ngnMainContainer"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span').click();
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('E1 Element AHBS (E1)', Keys.ENTER);

        time.sleep(2);
        print("first")

       
         

        elementr = browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div[11]/div/div/div[1]/button');

        if(elementr.is_displayed() and elementr.is_enabled()):
                elementr.click();
                print("firstthref3")


        
        elementk = browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]');
        if(elementk.is_displayed() and elementk.is_enabled()):
                elementk.click();
                print("firstthref4")

        t= browser.find_element_by_xpath('//*[@id="txtQuantity"]')

        while(not t.is_displayed()):
              time.sleep(1);
              print("dits")




     
        browser.find_element_by_xpath('//*[@id="btnAddProduct"]').click()
        e = browser.find_element_by_xpath('//*[@id="btnAddProduct"]')

        while( e.is_displayed() ):
              time.sleep(1);
              print("dis1")

        time.sleep(2);


        browser.find_element_by_xpath('//*[@id="select2-ddlProductSearchClassic-container"]').click();

        
        browser.find_element_by_xpath('//*[@id="ngnMainContainer"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span').click();
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('E2 Yazılım Destek Hizmeti (E2)', Keys.ENTER);

        time.sleep(2);
        print("first")

       
         

        elementr = browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div[11]/div/div/div[1]/button');

        if(elementr.is_displayed() and elementr.is_enabled()):
                elementr.click();
                print("firstthref3")


        
        elementk = browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]');
        if(elementk.is_displayed() and elementk.is_enabled()):
                elementk.click();
                print("firstthref4")

        t= browser.find_element_by_xpath('//*[@id="txtQuantity"]')

        while(not t.is_displayed()):
              time.sleep(1);
              print("dits")




     
        browser.find_element_by_xpath('//*[@id="btnAddProduct"]').click()
        e = browser.find_element_by_xpath('//*[@id="btnAddProduct"]')

        while( e.is_displayed() ):
              time.sleep(1);
              print("dis1")




        elementx =browser.find_element_by_xpath('//*[@id="btnSaveInvoiced"]')
        if(elementx.is_displayed() and elementx.is_enabled()):
                elementx.click();
                print("firstthref4")
        

       

        browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]').click();


        


        elementc =  browser.find_element_by_xpath('//*[@id="btnClose"]')

        while(not elementc.is_displayed()):
              elementc =  browser.find_element_by_xpath('//*[@id="btnClose"]')
              time.sleep(1);
              print("dis")

        if(elementc.is_displayed() and elementc.is_enabled()):
                elementc.click();
                print("firstthref")



                
       

        time.sleep(1);
        browser.find_element_by_xpath('//*[@id="divRepeatDocument"]/div[2]/button').click();


        browser.find_element_by_xpath('//*[@id="txtInitialRecurringDate"]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[1]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[5]').click();


        browser.find_element_by_xpath('//*[@id="txtLastRecurringDate"]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/thead/tr[2]/th[3]').click();

        browser.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[7]').click();

        browser.find_element_by_xpath('//*[@id="btnAddRecurringInfo"]').click();

        browser.find_element_by_xpath('//*[@id="btnSave"]').click();
        time.sleep(3);
        browser.find_element_by_xpath('//*[@id="btnCloseNotify"]').click();

        time.sleep(3);
        

      
       
        browser.find_element_by_xpath('//*[@id="lnkMoreSales"]').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[11]/td[1]/img').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[12]/td/div/span/a[1]/strong').click();
        browser.find_element_by_xpath('//*[@id="btnEdit"]').click();
        browser.find_element_by_xpath('//*[@id="btnSaveInvoiced"]').click();
        browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]').click();
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnClose"]').click();
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnCustomer"]').click();



        browser.find_element_by_xpath('//*[@id="lnkMoreSales"]').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[10]/td[1]/img').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[11]/td/div/span/a[1]/strong').click();
        browser.find_element_by_xpath('//*[@id="btnEdit"]').click();
        browser.find_element_by_xpath('//*[@id="btnSaveInvoiced"]').click();
        browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]').click();
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnClose"]').click();
     
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnCustomer"]').click();

        browser.find_element_by_xpath('//*[@id="lnkMoreSales"]').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[9]/td[1]/img').click();
        browser.find_element_by_xpath('/html/body/form/section/div[3]/div[2]/div/div/div/section/div/div/div/table/tbody/tr[10]/td/div/span/a[1]/strong').click();
        browser.find_element_by_xpath('//*[@id="btnEdit"]').click();
        browser.find_element_by_xpath('//*[@id="btnSaveInvoiced"]').click();
        browser.find_element_by_xpath('//*[@id="btnConfirmOldDatedInvoice"]').click();
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnClose"]').click();
        time.sleep(2);
        browser.find_element_by_xpath('//*[@id="btnCustomer"]').click();

      


                      




        


       
