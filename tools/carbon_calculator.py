#!/usr/bin/env python3
"""Teaching calculator for operational electricity emissions only.

All default inputs are hypothetical. This does not estimate a vendor's actual
footprint or a full life-cycle assessment.
"""


def positive_number(prompt: str, *, allow_zero: bool = False) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("请输入数字，例如 0.4 或 1.25。")
            continue
        if value < 0 or (value == 0 and not allow_zero):
            print("请输入大于零的数。" if not allow_zero else "不能输入负数。")
            continue
        return value


def main() -> None:
    print("AI运行用电排放情景计算器（教学示例）")
    print("默认值是假设，不是任何厂商的实测数据。")
    power_kw = positive_number("IT设备平均功率 kW [示例0.4]: ")
    hours = positive_number("运行时间 小时 [示例1]: ")
    pue = positive_number("数据中心PUE [示例1.3]: ")
    factor = positive_number("电力碳强度 kg CO2e/kWh [示例0.5]: ", allow_zero=True)
    tasks = positive_number("任务数量 [示例1000]: ")

    energy_kwh = power_kw * hours * pue
    emissions_kg = energy_kwh * factor
    per_task_kg = emissions_kg / tasks

    print("\n结果（仅为运行阶段用电情景估算）")
    print(f"估算用电量：{energy_kwh:.6f} kWh")
    print(f"估算排放量：{emissions_kg:.6f} kg CO2e")
    print(f"平均每项任务：{per_task_kg:.10f} kg CO2e")
    print("未包含服务器制造、建筑、网络、存储、设备报废等生命周期项目。")
    print("请记录所有输入的来源、年份、地区、单位，以及实测/披露/基准/假设属性。")


if __name__ == "__main__":
    main()
