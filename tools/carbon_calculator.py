#!/usr/bin/env python3
"""Teaching calculator for operational electricity emissions only."""

import argparse
import csv
from pathlib import Path
import sys


PARAMETER_NAMES = {
    "power_kw": ("power_kw_example",),
    "hours": ("runtime_hours_example", "runtime_hours_exercise"),
    "pue": ("pue_example",),
    "factor": ("electricity_emission_factor_example",),
    "tasks": ("task_count_example",),
}

DEFAULT_PARAMETER_NAMES = {
    "power_kw": "power_kw_example",
    "hours": "runtime_hours_example",
    "pue": "pue_example",
    "factor": "electricity_emission_factor_example",
    "tasks": "task_count_example",
}


def load_assumptions(path: Path) -> dict[str, dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            required_columns = {"id", "name", "value"}
            if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
                raise ValueError(
                    "assumptions CSV must contain id, name, and value columns"
                )

            assumptions = {}
            for line_number, row in enumerate(reader, start=2):
                name = (row.get("name") or "").strip()
                assumption_id = (row.get("id") or "").strip()
                value = (row.get("value") or "").strip()
                if not name or not assumption_id or not value:
                    raise ValueError(
                        f"missing id, name, or value on CSV line {line_number}"
                    )
                if name in assumptions:
                    raise ValueError(f"duplicate assumption name: {name}")
                assumptions[name] = {"id": assumption_id, "value": value}
            return assumptions
    except OSError as error:
        raise ValueError(f"cannot read assumptions file: {path}") from error


def parse_overrides(values: list[str], assumptions: dict[str, dict[str, str]]) -> dict[str, str]:
    overrides = {}
    supported_names = {
        name for parameter_names in PARAMETER_NAMES.values() for name in parameter_names
    }

    for item in values:
        if "=" not in item:
            raise ValueError(f"invalid --set value {item!r}; expected name=value")
        name, value = item.split("=", 1)
        name = name.strip()
        value = value.strip()
        if name not in assumptions:
            raise ValueError(f"unknown assumption name: {name}")
        if name not in supported_names:
            raise ValueError(f"assumption is not a calculator parameter: {name}")
        try:
            float(value)
        except ValueError as error:
            raise ValueError(f"override for {name} must be a number") from error
        overrides[name] = value
    return overrides


def positive_number(value: str, name: str, *, allow_zero: bool = False) -> float:
    try:
        number = float(value)
    except ValueError as error:
        raise ValueError(f"{name} must be a number") from error
    if number < 0 or (number == 0 and not allow_zero):
        requirement = "non-negative" if allow_zero else "greater than zero"
        raise ValueError(f"{name} must be {requirement}")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Estimate operational electricity emissions from teaching assumptions."
    )
    parser.add_argument(
        "--assumptions",
        default="data/assumptions.csv",
        help="path to assumptions.csv (default: data/assumptions.csv)",
    )
    parser.add_argument(
        "--set",
        dest="overrides",
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help="temporarily override an assumption; can be used multiple times",
    )
    args = parser.parse_args()

    try:
        assumptions = load_assumptions(Path(args.assumptions))
        overrides = parse_overrides(args.overrides, assumptions)

        selected_names = DEFAULT_PARAMETER_NAMES.copy()
        for parameter, candidate_names in PARAMETER_NAMES.items():
            for name in candidate_names:
                if name in overrides:
                    selected_names[parameter] = name

        values = {}
        used_ids = []
        for parameter, name in selected_names.items():
            if name not in assumptions:
                raise ValueError(f"missing assumption in CSV: {name}")
            raw_value = overrides.get(name, assumptions[name]["value"])
            values[parameter] = positive_number(
                raw_value,
                name,
                allow_zero=(parameter == "factor"),
            )
            used_ids.append(assumptions[name]["id"])

        power_kw = values["power_kw"]
        hours = values["hours"]
        pue = values["pue"]
        factor = values["factor"]
        tasks = values["tasks"]

        energy_kwh = power_kw * hours * pue
        emissions_kg = energy_kwh * factor
        per_task_kg = emissions_kg / tasks

        print("结果（仅为运行阶段用电情景估算）")
        print(f"估算用电量：{energy_kwh:.6f} kWh")
        print(f"估算排放量：{emissions_kg:.6f} kg CO2e")
        print(f"平均每项任务：{per_task_kg:.10f} kg CO2e")
        print("未包含服务器制造、建筑、网络、存储、设备报废等生命周期项目。")
        print("请记录所有输入的来源、年份、地区、单位，以及实测/披露/基准/假设属性。")
        print(f"used=[{','.join(used_ids)}]")
        return 0
    except ValueError as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
