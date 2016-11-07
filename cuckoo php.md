#cuckoo二次开发（PHP格式支持）
##操作步骤
### guest机修改部分
* 安装phpstudy
  >需要运行php文件必然需要php运行环境，包括php，apache，mysql，使用phpstudy最方便快捷
  
* 设置网站服务目录C:\WWW
  >将网站根目录设置成C:\WWW

![pic](http://ww2.sinaimg.cn/mw690/7b924f2dgw1f9jlm3rkhgj20db03jmy5.jpg)

### 代码修复部分
1. 添加php.py文件
  >在**cuckoo/analyzer/windows/modules/packages**目录下添加文件php.py
  
2. 在php.py中添加代码
3. 修改packages.py