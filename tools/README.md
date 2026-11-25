`carbon_calculator.py` — 读取共享数据中的教学假设，估算运行用电排放。
运行：`python tools/carbon_calculator.py [--assumptions PATH] [--set NAME=VALUE]`。
数据：默认读取 `data/assumptions.csv`；仅作运行阶段情景估算，不是完整生命周期结果。
`unit-convert.py` — 在能量单位或质量单位内换算，不支持跨类别换算。
运行：`python tools/unit-convert.py --value 2.5 --from kWh --to MWh`。
支持：`kWh/MWh/GWh` 与 `g/kg/t`；仅使用 Python 标准库。
