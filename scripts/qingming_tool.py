#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清明节实用工具
功能：祭扫提醒、祭文生成、纸扎设计、习俗查询、诗词引用、追思日记、实用清单
版本：1.1.0
作者：福建狼
"""

import argparse
import sys
import os
import json
from datetime import datetime, timedelta

# 跨平台编码处理
def setup_encoding():
    """设置跨平台编码"""
    if sys.platform == 'win32':
        import io
        try:
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        except:
            pass

setup_encoding()

# 数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
DIARY_FILE = os.path.join(DATA_DIR, 'diary.json')

# 确保数据目录存在
os.makedirs(DATA_DIR, exist_ok=True)

def get_qingming_date(year):
    """
    获取当年清明节日期
    清明节：太阳到达黄经15度，一般在4月4日或5日
    """
    # 简化计算：2000-2099年间，清明节日期规律
    # 实际应该用天文算法，这里用近似值
    if year % 4 == 0:  # 闰年
        return datetime(year, 4, 4)
    else:
        return datetime(year, 4, 5)

def cmd_remind():
    """祭扫日期提醒"""
    year = datetime.now().year
    qingming = get_qingming_date(year)
    
    # 计算前三后四
    before = qingming - timedelta(days=3)
    after = qingming + timedelta(days=4)
    
    weekday_names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    weekday = weekday_names[qingming.weekday()]
    
    print("=" * 40)
    print(f"📅 {year}年清明节：{qingming.month}月{qingming.day}日（{weekday}）")
    print("=" * 40)
    print()
    print("🕐 建议祭扫时间：")
    print(f"   • 正清明：{qingming.month}月{qingming.day}日")
    print(f"   • 前三后四：{before.month}月{before.day}日 - {after.month}月{after.day}日")
    print(f"   • 最佳时段：上午9点 - 下午3点")
    print()
    print("⚠️  注意事项：")
    print("   • 避开高峰时段，错峰出行")
    print("   • 关注天气预报，备好雨具")
    print("   • 注意防火安全，文明祭祀")
    print("   • 山区道路注意防滑")

def cmd_eulogy(name, relation):
    """生成祭文"""
    year = datetime.now().year
    
    templates = {
        "祖父": f"""维公元{year}年4月5日，孙辈谨以清酌庶馐之奠，致祭于祖父{name}之灵前：

    {name}一生勤劳朴实，待人诚恳，教诲子孙做人要正直善良、脚踏实地。
    音容宛在，德泽长存。孙辈定当铭记教诲，传承家风。

    伏惟尚飨""",
        
        "祖母": f"""维公元{year}年4月5日，孙辈谨以清酌庶馐之奠，致祭于祖母{name}之灵前：

    {name}一生慈爱贤惠，勤俭持家，养育子女，恩重如山。
    慈颜已逝，懿德永存。孙辈定当孝顺长辈，和睦家庭。

    伏惟尚飨""",
        
        "父亲": f"""维公元{year}年4月5日，子女谨以清酌庶馐之奠，致祭于父亲{name}之灵前：

    {name}一生辛劳，为家庭奔波，养育之恩，没齿难忘。
    严父已逝，教诲犹存。子女定当努力工作，照顾好家人。

    伏惟尚飨""",
        
        "母亲": f"""维公元{year}年4月5日，子女谨以清酌庶馐之奠，致祭于母亲{name}之灵前：

    {name}一生慈爱，含辛茹苦养育子女，母爱如山，深似海。
    慈母已逝，恩情永存。子女定当好好生活，不负母恩。

    伏惟尚飨""",
        
        "外祖父": f"""维公元{year}年4月5日，外孙辈谨以清酌庶馐之奠，致祭于外祖父{name}之灵前：

    {name}一生宽厚仁慈，待人真诚，关爱晚辈，恩德难忘。
    音容宛在，风范长存。外孙辈定当铭记教诲，奋发向上。

    伏惟尚飨""",
        
        "外祖母": f"""维公元{year}年4月5日，外孙辈谨以清酌庶馐之奠，致祭于外祖母{name}之灵前：

    {name}一生慈爱善良，勤劳持家，疼爱晚辈，恩重如山。
    慈颜已逝，懿德永存。外孙辈定当孝顺长辈，传承美德。

    伏惟尚飨""",
    }
    
    template = templates.get(relation)
    if template:
        print(template)
    else:
        # 通用模板
        print(f"""维公元{year}年4月5日，谨以清酌庶馐之奠，致祭于{name}之灵前：

    {name}一生勤劳善良，为人正直，深受亲友敬重。
    音容宛在，德泽长存。后人定当铭记教诲，传承家风。

    伏惟尚飨""")
        print(f"\n（提示：支持的关系类型：祖父、祖母、父亲、母亲、外祖父、外祖母）")

def cmd_paper(item):
    """纸扎设计"""
    designs = {
        "iPhone": """📱 纸扎物品：iPhone

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 尺寸：按真实比例缩小（约15cm长）
• 颜色：金色、银色、深空灰可选
• 配件：充电器、耳机、手机壳
• 建议材质：环保纸张或纸板
• 可添加：屏幕贴图（显示全家福）
• 环保提示：使用可降解材料""",
        
        "别墅": """🏠 纸扎物品：豪华别墅

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 尺寸：约30cm高，两层结构
• 颜色：米白色外墙，红色屋顶
• 配件：花园、车库、游泳池
• 建议材质：卡纸、竹签框架
• 可添加：家具内饰、灯光效果
• 环保提示：避免使用塑料装饰""",
        
        "汽车": """🚗 纸扎物品：豪华轿车

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 尺寸：约20cm长
• 颜色：黑色、白色、红色可选
• 配件：车牌（可定制）、车钥匙
• 建议材质：硬纸板、纸质车轮
• 可添加：司机人偶、行李
• 环保提示：使用水性颜料上色""",
        
        "飞机": """✈️ 纸扎物品：私人飞机

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 尺寸：约25cm长
• 颜色：白色机身，金色线条
• 配件：登机梯、行李箱
• 建议材质：卡纸、竹签骨架
• 可添加：舷窗贴图、航空公司标志
• 环保提示：避免使用金属配件""",
        
        "游艇": """🛥️ 纸扎物品：豪华游艇

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 尺寸：约20cm长
• 颜色：白色船身，蓝色线条
• 配件：甲板、遮阳棚、救生圈
• 建议材质：卡纸、泡沫板底座
• 可添加：船名定制、旗帜
• 环保提示：底座使用可降解材料""",
    }
    
    design = designs.get(item)
    if design:
        print(design)
    else:
        print(f"""📦 纸扎物品：{item}

设计要点：
━━━━━━━━━━━━━━━━━━━━
• 根据实际物品比例缩小制作（建议1:10或1:20）
• 使用环保纸张材料（卡纸、瓦楞纸）
• 可添加个性化元素（姓名、照片）
• 注意防火安全，远离易燃物
• 祭祀后妥善处理，保护环境

💡 常见纸扎物品：iPhone、别墅、汽车、飞机、游艇、家具、电器""")

def cmd_custom(region):
    """习俗查询"""
    customs = {
        "福建": """🎋 福建清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 清理墓地杂草，修整坟头
   • 供奉三牲（鸡、鱼、肉）、水果、糕点
   • 烧纸钱、放鞭炮（部分地区已禁止）

🥟 特色食品
   • 清明粿：艾草制成的糯米团，有甜（豆沙）咸（萝卜丝）两种
   • 润饼菜：春卷皮包裹各种蔬菜

🌿 传统活动
   • 踏青：全家出游赏花，感受春意
   • 插柳：门前插柳枝，据说可以辟邪
   • 禁火：部分地区保留清明禁火习俗""",
        
        "广东": """🎋 广东清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 拜山：家族集体上山扫墓，场面隆重
   • 烧猪：必备祭品，象征红皮赤壮、家族兴旺
   • 供奉：水果、糕点、茶水、酒水

🥟 特色食品
   • 艾粄：艾草制成的糕点，有祛湿功效
   • 发糕：象征发财高升

🌿 传统活动
   • 插柳戴柳：男女都戴柳枝编成的圈
   • 放风筝：清明时节放风筝祈福
   • 踏青：春游赏花""",
        
        "江浙": """🎋 江浙清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 扫墓：清理墓地，供奉青团、糕点
   • 上坟：家族成员集体前往，气氛庄重

🥟 特色食品
   • 青团：艾草汁和糯米粉制成，包豆沙或肉松
   • 清明螺：清明时节螺蛳最肥美
   • 香椿炒蛋：时令蔬菜

🌿 传统活动
   • 踏青：游春赏花，称为"踏青"
   • 荡秋千：古代清明习俗
   • 植树：清明前后植树成活率最高
   • 放风筝：剪断线象征放走晦气""",
        
        "北方": """🎋 北方清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 扫墓：清理墓地，供奉鲜花、水果
   • 上坟：烧纸钱、磕头祭拜

🥟 特色食品
   • 冷食：部分地区保留寒食节吃冷食习惯
   • 馓子：油炸面食，香脆可口
   • 鸡蛋：象征圆满

🌿 传统活动
   • 踏青：春游赏花，称为"踏青"或"春游"
   • 插柳：门前插柳枝，或戴柳枝
   • 放风筝：清明放风筝，剪断线象征放走晦气
   • 荡秋千：古代宫廷游戏""",
        
        "四川": """🎋 四川清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 上坟：清理墓地，供奉祭品
   • 烧纸：烧纸钱、纸衣、纸鞋

🥟 特色食品
   • 欢喜团：糯米制成的球形糕点
   • 清明粑：艾草和糯米制成
   • 凉粉：清明时节吃凉粉清火

🌿 传统活动
   • 踏青：春游赏花
   • 采清明菜：采摘艾草、荠菜等野菜
   • 戴柳：男女戴柳枝""",
        
        "湖南": """🎋 湖南清明习俗

━━━━━━━━━━━━━━━━━━━━
🍃 扫墓祭祖
   • 挂青：在坟头挂上白纸剪成的长条
   • 扫墓：清理墓地，供奉三牲

🥟 特色食品
   • 青团：艾草糯米团子
   • 蒿子粑粑：蒿草和糯米制成
   • 艾叶鸡蛋：艾叶煮鸡蛋

🌿 传统活动
   • 踏青：春游
   • 插柳：门前插柳
   • 放风筝""",
    }
    
    custom = customs.get(region)
    if custom:
        print(custom)
    else:
        print(f"暂不支持该地区，显示北方习俗：\n")
        print(customs["北方"])
        print(f"\n💡 支持地区：福建、广东、江浙、北方、四川、湖南")

def cmd_poem():
    """诗词引用"""
    import random
    
    poems = [
        {
            "title": "清明",
            "author": "唐·杜牧",
            "content": """清明时节雨纷纷，
路上行人欲断魂。
借问酒家何处有？
牧童遥指杏花村。""",
            "note": "最经典的清明诗，写尽游子思乡之情"
        },
        {
            "title": "寒食",
            "author": "唐·韩翃",
            "content": """春城无处不飞花，
寒食东风御柳斜。
日暮汉宫传蜡烛，
轻烟散入五侯家。""",
            "note": "寒食节与清明相近，写宫廷赐火习俗"
        },
        {
            "title": "清明夜",
            "author": "唐·白居易",
            "content": """好风胧月清明夜，
碧砌红轩刺史家。
独绕回廊行复歇，
遥听弦管暗看花。""",
            "note": "写清明夜的闲适与淡淡愁绪"
        },
        {
            "title": "清明口号",
            "author": "钱钟书",
            "content": """清明时节雨昏沉，
名唤清明滥到今。
也似重阳无实际，
满城风雨是重阴。""",
            "note": "现代讽刺诗，点出节日形式化的问题"
        },
        {
            "title": "苏堤清明即事",
            "author": "宋·吴惟信",
            "content": """梨花风起正清明，
游子寻春半出城。
日暮笙歌收拾去，
万株杨柳属流莺。""",
            "note": "写清明踏青的热闹景象"
        },
        {
            "title": "破阵子·春景",
            "author": "宋·晏殊",
            "content": """燕子来时新社，梨花落后清明。
池上碧苔三四点，叶底黄鹂一两声。
日长飞絮轻。

巧笑东邻女伴，采桑径里逢迎。
疑怪昨宵春梦好，元是今朝斗草赢。
笑从双脸生。""",
            "note": "写清明时节少女斗草的欢乐"
        },
    ]
    
    poem = random.choice(poems)
    print(f"《{poem['title']}》")
    print(f"{poem['author']}")
    print()
    print(poem['content'])
    print()
    print(f"💡 {poem['note']}")

def cmd_diary(content=None, list_all=False):
    """追思日记"""
    if list_all:
        # 列出所有日记
        if os.path.exists(DIARY_FILE):
            with open(DIARY_FILE, 'r', encoding='utf-8') as f:
                diaries = json.load(f)
            
            if not diaries:
                print("暂无日记记录")
                return
            
            print(f"📚 共有 {len(diaries)} 篇日记\n")
            for i, entry in enumerate(diaries[-10:], 1):  # 显示最近10篇
                print(f"{i}. {entry['date']} {entry['time']}")
                preview = entry['content'][:30] + "..." if len(entry['content']) > 30 else entry['content']
                print(f"   {preview}\n")
        else:
            print("暂无日记记录")
        return
    
    if content:
        # 保存日记
        timestamp = datetime.now()
        entry = {
            "date": timestamp.strftime("%Y-%m-%d"),
            "time": timestamp.strftime("%H:%M"),
            "content": content,
            "timestamp": timestamp.isoformat()
        }
        
        # 读取现有日记
        diaries = []
        if os.path.exists(DIARY_FILE):
            with open(DIARY_FILE, 'r', encoding='utf-8') as f:
                diaries = json.load(f)
        
        # 添加新日记
        diaries.append(entry)
        
        # 保存
        with open(DIARY_FILE, 'w', encoding='utf-8') as f:
            json.dump(diaries, f, ensure_ascii=False, indent=2)
        
        print("=" * 40)
        print("【追思日记】")
        print(f"时间：{entry['date']} {entry['time']}")
        print("=" * 40)
        print()
        print(content)
        print()
        print("——铭记于心，传承于行")
        print(f"\n✅ 已保存到日记本（共{len(diaries)}篇）")
    else:
        # 显示模板
        print("【追思日记模板】")
        print()
        print("今天我想对____说：")
        print()
        print("记得您曾经____，")
        print("那时候____，")
        print("您教会了我____。")
        print()
        print("现在我也____，")
        print("我会继续努力____，")
        print("不辜负您的期望。")
        print()
        print("愿您在另一个世界安好。")
        print()
        print("💡 使用：qingming_tool.py diary \"您的日记内容\"")

def cmd_checklist(export=False):
    """实用清单"""
    checklist = """【扫墓准备清单】

🌸 祭品
   □ 鲜花（菊花、百合、康乃馨）
   □ 水果（苹果、橘子、香蕉）
   □ 糕点（蛋糕、饼干、传统点心）
   □ 酒水（白酒、红酒或茶水）
   □ 香烛纸钱

🛠️ 工具
   □ 扫帚、抹布（清理墓地）
   □ 打火机/火柴
   □ 垃圾袋（带走垃圾）
   □ 水桶（打水清洗）
   □ 手套

🚗 出行
   □ 查看天气预报
   □ 规划路线（避开拥堵）
   □ 准备现金（部分墓地只收现金）
   □ 充电宝

⚠️  安全
   □ 确认防火安全
   □ 烧纸后在旁确认熄灭
   □ 带走所有垃圾
   □ 看管好小孩
   □ 注意山路安全

📱 其他
   □ 手机充满电
   □ 拍照留念
   □ 记录家族故事

━━━━━━━━━━━━━━━━━━━━
💡 提示：
• 提前一天准备祭品，避免临时匆忙
• 穿舒适的运动鞋，墓地多在山上
• 带上纸巾和湿巾
• 尊重他人，保持安静
"""
    
    print(checklist)
    
    if export:
        # 导出到文件
        export_file = os.path.join(DATA_DIR, 'checklist.txt')
        with open(export_file, 'w', encoding='utf-8') as f:
            f.write(checklist)
        print(f"✅ 清单已导出到：{export_file}")

def main():
    parser = argparse.ArgumentParser(
        description="清明节实用工具 v1.1.0 - 祭扫提醒、祭文生成、习俗查询等",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python qingming_tool.py remind           # 查看祭扫日期
  python qingming_tool.py eulogy 张三 祖父  # 生成祭文
  python qingming_tool.py poem             # 随机显示诗词
  python qingming_tool.py checklist        # 显示准备清单
  python qingming_tool.py diary "今天..."   # 记录追思日记
  python qingming_tool.py diary --list     # 查看所有日记
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # remind
    subparsers.add_parser("remind", help="祭扫日期提醒")
    
    # eulogy
    eulogy_parser = subparsers.add_parser("eulogy", help="生成祭文")
    eulogy_parser.add_argument("name", help="先人姓名")
    eulogy_parser.add_argument("relation", help="关系（祖父/祖母/父亲/母亲/外祖父/外祖母）")
    
    # paper
    paper_parser = subparsers.add_parser("paper", help="纸扎设计")
    paper_parser.add_argument("item", help="物品名称（iPhone/别墅/汽车/飞机/游艇）")
    
    # custom
    custom_parser = subparsers.add_parser("custom", help="习俗查询")
    custom_parser.add_argument("region", help="地区（福建/广东/江浙/北方/四川/湖南）")
    
    # poem
    subparsers.add_parser("poem", help="诗词引用")
    
    # diary
    diary_parser = subparsers.add_parser("diary", help="追思日记")
    diary_parser.add_argument("content", nargs="?", help="日记内容")
    diary_parser.add_argument("--list", "-l", action="store_true", help="列出所有日记")
    
    # checklist
    checklist_parser = subparsers.add_parser("checklist", help="实用清单")
    checklist_parser.add_argument("--export", "-e", action="store_true", help="导出到文件")
    
    args = parser.parse_args()
    
    if args.command == "remind":
        cmd_remind()
    elif args.command == "eulogy":
        cmd_eulogy(args.name, args.relation)
    elif args.command == "paper":
        cmd_paper(args.item)
    elif args.command == "custom":
        cmd_custom(args.region)
    elif args.command == "poem":
        cmd_poem()
    elif args.command == "diary":
        if args.list:
            cmd_diary(list_all=True)
        else:
            cmd_diary(args.content)
    elif args.command == "checklist":
        cmd_checklist(args.export)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
