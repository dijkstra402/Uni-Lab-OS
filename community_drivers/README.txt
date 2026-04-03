============================================================
Build Agent 集成报告
============================================================
task_id     : fbeffe4c
GitHub 仓库  : https://github.com/pklaus/universal_usbtmc
成功纳管     : 1 个驱动
失败         : 1 个驱动
UNILAB_ROOT : /Users/sml/work/test/Unilab_副本/Uni-Lab-OS

============================================================
【成功纳管的仪器驱动】
============================================================

▶ Instrument  [通用设备]
  仪器名称   : A backend for python-vxi11
  型号       : vxi11
  GitHub 源码 : https://github.com/pklaus/universal_usbtmc/blob/master/universal_usbtmc/backends/python_vxi11.py
  驱动文件   : /Users/sml/work/test/Unilab_副本/Uni-Lab-OS/unilabos/devices/generic/vxi11_instrument.py
  注册表     : /Users/sml/work/test/Unilab_副本/Uni-Lab-OS/unilabos/registry/devices/generic.yaml
  启动配置   : /Users/sml/work/test/Unilab_副本/Uni-Lab-OS/unilabos/test/_build_agent_test_instrument.json
  启动命令   : cd '/Users/sml/work/test/Unilab_副本/Uni-Lab-OS' && source ~/miniforge3/etc/profile.d/mamba.sh && mamba activate unilab && unilab -g unilabos/test/_build_agent_test_instrument.json --backend simple --skip_env_check --ak "$UNILAB_AK" --sk "$UNILAB_SK" --addr "$UNILAB_ADDR" --disable_browser

============================================================
【失败驱动摘要】
============================================================

✗ Instrument
  源文件 : universal_usbtmc/instrument.py
  原因   : 导入验证失败: Traceback (most recent call last):

============================================================
说明
============================================================
- driver.py     : 生成的驱动文件，可手工修 bug / 调整依赖
- registry.yaml : 注册表，可手工改参数 schema / 默认值
- startup.json  : 启动配置，可手工改连接地址/端口/串口参数
- registry_yaml 是多设备共存文件，修改时注意不要破坏其它条目
