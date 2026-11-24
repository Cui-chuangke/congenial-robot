# AI碳足迹 × Python × 计算机视觉：学习工作台

欢迎来到你的学习资料仓库。这里不是一篇替你写好的参赛论文，而是一套可以边学边做、逐步积累自己研究能力的工具箱。内容按主题分开，建议从“从这里开始”顺序使用。

> **竞赛诚信提醒**：第十三届全国大学生能源经济学术创意大赛公开通知写明不得使用生成式人工智能自动生成参赛作品。请把本仓库用于学习、理解概念、练习代码和核查计算；参赛论文的观点、证据判断与最终表达应由你本人/团队完成，并以官网最新规则为准。不要把AI生成的文字直接作为参赛作品。

## 从这里开始

1. 打开 [01｜入门路线](docs/01-start-here.md)：先看这项研究想解决什么，再安排学习顺序。
2. 用 [02｜一步一步做研究](docs/02-research-workbook.md)：把题目缩小成能回答的问题，记录数据和假设。
3. 按 [03｜Python零基础练习](docs/03-python-first-steps.md) 运行第一个小程序。
4. 了解 [04｜AI碳排放计算器](docs/04-carbon-calculator.md)，或在本地打开交互页面 [`docs/tools/carbon-calculator.html`](docs/tools/carbon-calculator.html)。
5. 准备好后进入 [05｜计算机视觉入门](docs/05-computer-vision.md)。
6. 最后使用 [06｜实验室准备](docs/06-lab-preparation.md) 整理公开信息和个人能力证据。

## 可直接使用的工具与模板

- [浏览器碳排放情景计算器](docs/tools/carbon-calculator.html)：纯本地页面，输入是假设值；只估算运行用电排放，不会上传数据，也不代表任何厂商实测结果。
- [Python命令行计算器](tools/carbon_calculator.py)：无需第三方库的示例脚本。
- [来源与数据记录表](templates/source-and-data-log.csv)
- [实验记录模板](templates/experiment-log.md)
- [论文研究问题工作表](templates/research-question.md)
- [导师调研模板](templates/lab-contact.md)

## 来源原则

优先阅读原始标准、官方赛事通知、官方文档和论文原文。第三方网页只用于发现资料，不作为未经核验的最终依据。每条数据都要保存来源、日期、单位、适用地区和是否为估算。

- [赛事官网入口](https://energy.qibebt.ac.cn/eneco/contribution/index.html#/index)
- [Python官方教程](https://docs.python.org/3/tutorial/)
- [PyTorch教程](https://pytorch.org/tutorials/)
- [ITU-T L.1801 AI环境影响指南](https://www.itu.int/ITU-T/recommendations/rec.aspx?rec=L.1801)
- [GHG Protocol](https://ghgprotocol.org/)

## 研究边界声明

“运行设备用电排放”不等于“AI系统完整生命周期碳足迹”。完整研究还可能涉及硬件制造、数据中心建设、冷却、网络、存储、模型训练/推理分配和设备退役。没有数据的项目应写明缺失，不能伪装成已测量。
