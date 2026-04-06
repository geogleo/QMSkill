---
name: qingming-festival
description: |
  清明节实用工具。用于清明祭扫日期提醒、祭文生成、纸扎设计、习俗查询、诗词引用、追思日记等。
  当用户询问清明节日期、需要生成祭文、查询习俗、或提到"扫墓"、"祭祖"、"清明"等关键词时触发。
---

# 清明节实用工具

提供清明节相关实用功能，帮助用户准备和度过清明节。

## 功能

| 功能 | 命令 | 说明 |
|------|------|------|
| 祭扫提醒 | `remind` | 当年清明日期、前三后四、最佳时段 |
| 祭文生成 | `eulogy <姓名> <关系>` | 个性化祭文，支持祖父/祖母/父亲/母亲/外祖父/外祖母 |
| 纸扎设计 | `paper <物品>` | 现代纸扎设计指南（iPhone/别墅/汽车/飞机/游艇） |
| 习俗查询 | `custom <地区>` | 全国各地清明习俗（福建/广东/江浙/北方/四川/湖南） |
| 诗词引用 | `poem` | 6首经典清明诗词随机展示 |
| 追思日记 | `diary <内容>` | 记录回忆，自动保存 |
| 日记列表 | `diary --list` | 查看所有日记 |
| 实用清单 | `checklist` | 扫墓准备清单 |
| 清单导出 | `checklist --export` | 导出到文件 |

## 使用方法

```bash
# 查看祭扫日期
python scripts/qingming_tool.py remind

# 生成祭文
python scripts/qingming_tool.py eulogy "张爷爷" "祖父"

# 查询习俗
python scripts/qingming_tool.py custom 福建

# 随机诗词
python scripts/qingming_tool.py poem

# 记录日记
python scripts/qingming_tool.py diary "今天去扫墓了..."

# 查看清单
python scripts/qingming_tool.py checklist --export
```

## 注意事项

- 祭祀重在心意，不必攀比
- 注意防火安全，文明祭祀
- 环保祭祀，减少污染
- 尊重各地风俗习惯