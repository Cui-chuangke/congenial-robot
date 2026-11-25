#!/usr/bin/env python3
"""Check required fields in a filled Markdown or CSV template."""

import argparse
import csv
import json
import re
from pathlib import Path


def validate(file_path, schema):
    fields = schema["required"]
    if schema["format"] not in ("markdown", "csv"):
        raise ValueError("schema format must be markdown or csv")
    if schema["format"] == "csv":
        with file_path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            rows, headers = list(reader) or [{}], reader.fieldnames or []
        return [(n, f["name"]) for n, row in enumerate(rows, 1) for f in fields
                if f["name"] not in headers or not (row.get(f["name"]) or "").strip()]
    values = {k.strip(): v.strip() for k, v in re.findall(r"(?m)^\s*-\s*([^：]+)：(.*)$",
              file_path.read_text(encoding="utf-8"))}
    return [(n, f["name"]) for n, f in enumerate(fields, 1) if not values.get(f["name"])]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema", type=Path, help="path to the template schema JSON")
    parser.add_argument("file", type=Path, help="path to the filled template")
    args = parser.parse_args()
    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        missing = validate(args.file, schema)
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
        parser.error(f"读取或校验失败：{error}")
    for number, name in missing:
        print(f"第 {number} 项缺：{name}")
    if not missing:
        print("校验通过")


if __name__ == "__main__":
    main()
