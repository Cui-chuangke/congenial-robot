# 03｜Python零基础：从复制运行到自己改

本页目标不是让你背语法，而是让你看到：代码如何把输入数字变成可复算的结果。先运行仓库里的 `tools/carbon_calculator.py`，再做下面练习。

## 练习一：不用安装库的最小计算

将下面代码复制到一个名为 `first_calc.py` 的文件：

```python
power_kw = 0.4
hours = 1.0
pue = 1.3
grid_factor = 0.5

energy_kwh = power_kw * hours * pue
emissions_kg = energy_kwh * grid_factor

print(f"用电量：{energy_kwh:.3f} kWh")
print(f"运行排放估算：{emissions_kg:.3f} kg CO2e")
```

运行方式：

- Windows：在终端进入文件所在目录，运行 `python first_calc.py`；如果不行，试 `py first_calc.py`。
- macOS/Linux：运行 `python3 first_calc.py`。

若输出用电量0.520 kWh和排放0.260 kg CO2e，说明这段程序运行成功。数字是假设示例，不是实际服务数据。

## 代码逐行讲解

- `power_kw = 0.4`：把0.4这个数存进名为`power_kw`的变量；变量名提示单位是千瓦。
- `*`：乘法。
- `energy_kwh = ...`：计算用电量，并保存结果。
- `print(...)`：把结果显示在屏幕。
- `:.3f`：显示三位小数，不改变计算本身。

## 练习二：把运行时间改成半小时

把 `hours = 1.0` 改成 `hours = 0.5`。重新运行。结果应减半。若没有减半，检查是否改错了文件或运行了旧文件。

## 练习三：多算几张图片

添加：

```python
image_count = 1000
emissions_per_image_kg = emissions_kg / image_count
print(f"平均每张图片：{emissions_per_image_kg:.8f} kg CO2e")
```

这只是把当前情景结果平均分摊到图片数量，并不代表每张图片都真实消耗完全相同的能量。

## 遇到报错先检查

1. 文件名是否真的是`first_calc.py`，而不是`first_calc.py.txt`？
2. 终端当前目录是否包含该文件？
3. 冒号、括号、引号是否成对？
4. 变量名大小写是否一致？`hours`和`Hours`不同。
5. 是否安装了Python？运行`python --version`或`python3 --version`检查。

## 什么时候学Pandas？

当你手里有多行数据（例如不同年份和地区的电力碳强度），再学Pandas。它能读CSV、筛选行、合并表格、计算汇总。官方起步教程：

- Python教程：https://docs.python.org/3/tutorial/
- pandas入门：https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
