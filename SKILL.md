---
name: qingming-festival
description: |
  清明节实用工具。提供祭扫日期提醒、祭文生成、纸扎设计、家谱记录、习俗查询、诗词引用、追思日记等功能。
  帮助用户更好地准备和度过清明节，传承家族记忆。
  版本：1.1.0
metadata:
  openclaw:
    emoji: "🎋"
---

# 清明节实用工具 v1.1.0

> 清明祭祀，心意重于形式。本 skill 提供实用工具，帮助用户更好地准备和度过清明节。

## 功能概览

| 功能 | 说明 | 命令 |
|------|------|------|
| 祭扫提醒 | 当年清明日期、前三后四、最佳时段 | `remind` |
| 祭文生成 | 个性化祭文（支持多种亲属关系） | `eulogy` |
| 纸扎设计 | 现代纸扎物品设计指南 | `paper` |
| 习俗查询 | 全国各地清明习俗 | `custom` |
| 诗词引用 | 6首经典清明诗词随机展示 | `poem` |
| 追思日记 | 记录回忆，自动保存 | `diary` |
| 实用清单 | 扫墓准备清单，可导出 | `checklist` |

## 安装

无需额外依赖，直接运行 Python 脚本即可。

```bash
# 克隆或下载本 skill
cd qingming-festival/scripts

# 查看帮助
python qingming_tool.py --help
```

## 命令详解

### 1. 祭扫提醒

查看当年清明节日期和祭扫建议：

```bash
python qingming_tool.py remind
```

输出示例：
```
📅 2026年清明节：4月5日（周日）

🕐 建议祭扫时间：
   • 正清明：4月5日
   • 前三后四：4月2日 - 4月9日
   • 最佳时段：上午9点 - 下午3点
```

### 2. 生成祭文

根据先人信息生成个性化祭文：

```bash
python qingming_tool.py eulogy "张爷爷" "祖父"
python qingming_tool.py eulogy "李奶奶" "祖母"
python qingming_tool.py eulogy "爸爸" "父亲"
python qingming_tool.py eulogy "妈妈" "母亲"
```

支持的关系类型：
- 祖父、祖母
- 父亲、母亲
- 外祖父、外祖母

### 3. 纸扎设计

获取现代纸扎物品的设计指南：

```bash
python qingming_tool.py paper iPhone
python qingming_tool.py paper 别墅
python qingming_tool.py paper 汽车
python qingming_tool.py paper 飞机
python qingming_tool.py paper 游艇
```

### 4. 习俗查询

查询全国各地清明习俗：

```bash
python qingming_tool.py custom 福建
python qingming_tool.py custom 广东
python qingming_tool.py custom 江浙
python qingming_tool.py custom 北方
python qingming_tool.py custom 四川
python qingming_tool.py custom 湖南
```

### 5. 诗词引用

随机展示清明相关诗词（共6首）：

```bash
python qingming_tool.py poem
```

包含：
- 杜牧《清明》
- 韩翃《寒食》
- 白居易《清明夜》
- 钱钟书《清明口号》
- 吴惟信《苏堤清明即事》
- 晏殊《破阵子·春景》

### 6. 追思日记

记录对先人的回忆和感悟：

```bash
# 记录新日记
python qingming_tool.py diary "今天去扫墓了，想起了爷爷..."

# 查看所有日记
python qingming_tool.py diary --list
```

日记自动保存在 `data/diary.json` 文件中。

### 7. 实用清单

生成扫墓准备清单：

```bash
# 显示清单
python qingming_tool.py checklist

# 导出到文件
python qingming_tool.py checklist --export
```

清单内容包括：
- 🌸 祭品（鲜花、水果、糕点等）
- 🛠️ 工具（扫帚、打火机、垃圾袋等）
- 🚗 出行（天气、路线、现金等）
- ⚠️ 安全（防火、看护、环保等）
- 📱 其他（手机、拍照、记录等）

## 文件结构

```
qingming-festival/
├── SKILL.md              # 本文件
├── scripts/
│   └── qingming_tool.py  # 主程序
└── data/                 # 数据目录（自动创建）
    ├── diary.json        # 日记数据
    └── checklist.txt     # 导出的清单
```

## 跨平台兼容

- ✅ Windows（PowerShell/CMD）
- ✅ macOS（Terminal）
- ✅ Linux（Bash）

自动处理编码问题，中文显示正常。

## 使用示例

**场景1：准备清明扫墓**
```bash
# 查看日期
python qingming_tool.py remind

# 生成清单并导出
python qingming_tool.py checklist --export

# 查询当地习俗
python qingming_tool.py custom 福建
```

**场景2：撰写祭文**
```bash
# 生成祭文
python qingming_tool.py eulogy "爷爷" "祖父"

# 随机诗词
python qingming_tool.py poem
```

**场景3：记录追思**
```bash
# 写日记
python qingming_tool.py diary "今天清明，去看了爷爷..."

# 查看所有日记
python qingming_tool.py diary --list
```

## 注意事项

- 祭祀重在心意，不必攀比
- 注意防火安全，文明祭祀
- 环保祭祀，减少污染
- 尊重各地风俗习惯

## 版本历史

- v1.1.0 (2026-04-04)
  - 增加6首诗词（含钱钟书《清明口号》）
  - 增加更多地区习俗（四川、湖南）
  - 增加日记保存和列表功能
  - 增加清单导出功能
  - 优化跨平台编码兼容性
  - 美化输出格式

- v1.0.0 (2026-04-04)
  - 初始版本
  - 基础功能：提醒、祭文、纸扎、习俗、诗词、日记、清单

## 作者

福建狼

## 开源协议

MIT License
