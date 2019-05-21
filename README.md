# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

#### 编码规范
* PEP8 Python 编码规范,参考文档 https://www.jianshu.com/p/52f4416c267d t6

#### 如何运行
* 安装依赖包`pip install -r requirements.txt`
* 运行所有TestCase `pytest --env=live`, 参数`env`可选择`dev/staging/live`, 默认`dev`
* 运行单个TestCase, 指定文件即可 `pytest --env=staging proj01_botk/test_case/m0100_check_landing_page.py`
* pytest配置文件`pytest.ini`中指定`testcase`文件类型`python_files=m*.py`, 以及Html报告输出目录及文件`--html=report/report.html` 
* pytest参考文档: [https://docs.pytest.org/en/latest/index.html](https://docs.pytest.org/en/latest/index.html)

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact