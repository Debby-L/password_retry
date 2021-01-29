#先在城市碼中 設定好密碼 password = a123456
#讓使用者[最多輸入3次密碼]
#不對的話，印出"密碼錯誤! 還有__次機會"
#對的話，印出"登入成功!"
password = 'a123456'
i = 3 #剩餘的機會
while i > 0: #要建立重複輸入的循環，設定條件
    i = i - 1
    pwd = input('請輸入密碼:') #password = input('請輸入密碼:') ，如果宣告為password會取代原先的正確密碼
    if pwd == password:
    	print ('登入成功!')
    	break #逃出迴圏
    else:
    	print ('密碼錯誤!')
    	if i > 0: #當剩餘0次機會時顯示'密碼錯誤'，終止迴圈
    		print ('還有', i ,'次機會')
		


	


    