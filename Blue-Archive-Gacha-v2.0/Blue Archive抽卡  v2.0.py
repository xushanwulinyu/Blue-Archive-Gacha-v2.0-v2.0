import time
import random

# 1. 提前定义角色列表（示例）
students_rare = ['圣园未花⭐⭐⭐🌈', '桐藤渚⭐⭐⭐🌈']

students_3 =[
    "白子⭐⭐⭐", "星野⭐⭐⭐", "阿露⭐⭐⭐", "日奈⭐⭐⭐",
    "泉⭐⭐⭐", "晴奈⭐⭐⭐", "日富美⭐⭐⭐", "鹤城⭐⭐⭐",
    "花凛⭐⭐⭐", "妮露⭐⭐⭐", "真纪⭐⭐⭐", "响⭐⭐⭐",
    "堇⭐⭐⭐", "纱绫⭐⭐⭐", "瞬⭐⭐⭐", "绿⭐⭐⭐",
    "艾米⭐⭐⭐", "真白⭐⭐⭐", "泉奈⭐⭐⭐", "爱丽丝⭐⭐⭐",
    "切里诺⭐⭐⭐", "柚子⭐⭐⭐", "梓⭐⭐⭐", "小春⭐⭐⭐",
    "日富美（泳装）⭐⭐⭐", "白子（骑行）⭐⭐⭐", "瞬（幼女）⭐⭐⭐", "纱绫（私服）⭐⭐⭐",
    "明日奈（兔女郎）⭐⭐⭐", "夏⭐⭐⭐", "亚子⭐⭐⭐", "切里诺（温泉）⭐⭐⭐",
    "千夏（温泉）⭐⭐⭐", "和香（温泉）⭐⭐⭐", "芹香（正月）⭐⭐⭐", "濑名⭐⭐⭐",
    "千寻⭐⭐⭐", "三森⭐⭐⭐", "忧⭐⭐⭐", "日向⭐⭐⭐",
    "玛丽娜⭐⭐⭐", "咲⭐⭐⭐", "宫子⭐⭐⭐", "美游⭐⭐⭐",
    "枫⭐⭐⭐", "伊吕波⭐⭐⭐", "月咏⭐⭐⭐", "美咲⭐⭐⭐",
    "日和⭐⭐⭐", "亚津子⭐⭐⭐", "野宫（泳装）⭐⭐⭐", "若藻（泳装）⭐⭐⭐",
    "海香⭐⭐⭐", "纱织⭐⭐⭐", "萌绘⭐⭐⭐", "和纱⭐⭐⭐",
    "心奈⭐⭐⭐", "歌原（应援团）⭐⭐⭐", "诺亚⭐⭐⭐", "朱音（兔女郎）⭐⭐⭐",
    "日鞠⭐⭐⭐", "时雨⭐⭐⭐", "结良良⭐⭐⭐", "芹娜（圣诞）⭐⭐⭐",
    "花绘（圣诞）⭐⭐⭐", "美称⭐⭐⭐", "妃咲⭐⭐⭐", "惠⭐⭐⭐",
    "康娜⭐⭐⭐", "樱子⭐⭐⭐", "小雪⭐⭐⭐", "佳代子（正月）⭐⭐⭐",
    "遥香（正月）⭐⭐⭐", "果穗⭐⭐⭐", "时（兔女郎）⭐⭐⭐", "爱丽丝（女仆）⭐⭐⭐",
    "桃井（女仆）⭐⭐⭐", "绿（女仆）⭐⭐⭐", "玲纱⭐⭐⭐", "理美⭐⭐⭐",
    "南⭐⭐⭐", "丽情⭐⭐⭐", "实梨⭐⭐⭐", "宫子（泳装）⭐⭐⭐",
    "咲（泳装）⭐⭐⭐", "白子（泳装）⭐⭐⭐", "三森（泳装）⭐⭐⭐", "梅樱⭐⭐⭐",
    "琴里（应援团）⭐⭐⭐", "晴奈（体操）⭐⭐⭐", "霞⭐⭐⭐", "一花⭐⭐⭐",
    "时雨（温泉）⭐⭐⭐", "缘里⭐⭐⭐", "莲华⭐⭐⭐", "桔梗⭐⭐⭐",
    "艾米（泳装）⭐⭐⭐", "晴（野餐）⭐⭐⭐", "小玉（野餐）⭐⭐⭐", "阿露（礼服）⭐⭐⭐",
    "佳代子（礼服）⭐⭐⭐", "明里（正月）⭐⭐⭐", "椿（导游）⭐⭐⭐", "伊织⭐⭐⭐",
    "芹香（泳装）⭐⭐⭐", "康娜（泳装）⭐⭐⭐", "吹雪（泳装）⭐⭐⭐", "萌绘（泳装）⭐⭐⭐",
    "美咲（泳装）⭐⭐⭐", "巴（旗袍）⭐⭐⭐", "玛丽娜（旗袍）⭐⭐⭐", "皋月⭐⭐⭐",
    "千秋⭐⭐⭐", "优香（睡衣）⭐⭐⭐", "诺亚（睡衣）⭐⭐⭐", "真纪（野餐）⭐⭐⭐",
    "朱莉（打工）⭐⭐⭐", "濑名（私服）⭐⭐⭐", "泉（正月）⭐⭐⭐", "堇（打工）⭐⭐⭐",
    "来伊⭐⭐⭐", "纱织（礼服）⭐⭐⭐", "菲娜（导游）⭐⭐⭐", "名草⭐⭐⭐",
    "妮娅⭐⭐⭐", "夏（乐队）⭐⭐⭐", "缘里（泳装）⭐⭐⭐", "桔梗（泳装）⭐⭐⭐",
    "绘里⭐⭐⭐", "朋江⭐⭐⭐", "美代⭐⭐⭐", "冬⭐⭐⭐",
    "律⭐⭐⭐"
]

students_2 = [
    "芹香⭐⭐", "绫音⭐⭐", "佳代子⭐⭐", "淳子⭐⭐",
    "明里⭐⭐", "枫香⭐⭐", "爱莉⭐⭐", "莲见⭐⭐",
    "朱音⭐⭐", "晴⭐⭐", "歌原⭐⭐", "优香⭐⭐",
    "椿⭐⭐", "千世⭐⭐", "桃井⭐⭐", "野宫⭐⭐",
    "花绘⭐⭐", "静子⭐⭐", "花子⭐", "桐乃⭐⭐",
    "玛丽⭐⭐", "睦月⭐⭐", "红叶⭐⭐", "莲华（泳装）⭐⭐"
]


students_1 = [
        "千夏⭐", "好美⭐", "芹娜⭐", "明日奈⭐",
        "琴里⭐", "菲娜⭐", "鹤城（泳装）⭐", "吹雪⭐",
        "满⭐", "绫音（泳装）⭐", "巴⭐", "静子（泳装）⭐",
        "和香⭐", "遥香⭐", "泉（泳装）⭐", "朱莉⭐",
        "志美子⭐", "铃美⭐", "小玉⭐", "响（应援团）⭐",
        "莲见（体操）⭐", "淳子（正月）⭐", "柚子（女仆）⭐", "美游（泳装）⭐",
        "小春（泳装）⭐", "佐天泪子⭐", "伊吹⭐", "爱莉（乐队）⭐",
        "桐乃（泳装）⭐", "亚津子（泳装）⭐", "美弥（偶像）⭐", "花凛（制服）⭐",
        "青叶⭐", "一花（泳装）⭐"
]


# 2. 全局定义打字函数（只定义一次）
def type_print(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def type11_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def ty_print(text, delay=0.3):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

type_print("😆欢迎sensei前来招募学生🎉（木嘿嘿嘿嘿嘿嘿怨大种来啦👻~~~）")
type11_print("啊~！(=ﾟДﾟ=)❤️ 没说什么...！")
type_print("招募 120青辉石💎（1次）——请输入1")
type_print("招募 1200青辉石💎（10次）——请输入10")
type_print("㊙️限定角色：圣园未花，㊙️限定角色：桐藤渚 招募概率提升！")

# 3. 抽卡函数（单独定义）
def blue_archive_gacha_10pull():
    """模拟蔚蓝档案十连抽，返回抽卡结果和资源消耗"""
    # 概率配置
    lis = [students_rare, students_3]
    lis_weights = [0.007, 0.023]
    selected_high_rarity = random.choices(lis, weights=lis_weights, k=1)[0]
    student_3_rare = random.choice(selected_high_rarity) if selected_high_rarity else None
    student_2 = random.choice(students_2)
    student_1 = random.choice(students_1)

    # 十连抽概率
    rarity_weights = [
        (student_3_rare, 3),
        (student_2, 18.5),
        (student_1, 78.5)
    ]
    rarities = [r[0] for r in rarity_weights]
    weights = [r[1] for r in rarity_weights]

    # 执行十连抽
    pulls = random.choices(rarities, weights=weights, k=10)

    # 保底逻辑：无二次则最后一次替换且无三星(出现了1三星9一星
    if student_2 not in pulls and student_3_rare not in pulls:
        selected_element = random.choice(students_2)
        pulls[-1] = selected_element
        type_print("=== ㊙️蔚蓝档案十连抽结果㊙️===")
        ty_print(f"总抽数：10次")
        ty_print("三星角色：0名")
        ty_print("二星角色：1名")
        ty_print("一星角色：9名")
        for i in range(len(pulls)):
            if pulls[i] in student_2:
                pulls[i] = random.choice(students_2)  # 每个名额随机抽二星角色
            if pulls[i] in student_1:
                pulls[i] = random.choice(students_1)
        # 最终pulls就是替换后的结果
        print(f"{pulls}")
        ty_print("🤣AUV~ +19~ 九蓝一金🤡~")
        return pulls

    else:
        result = {
            "三星": pulls.count(student_3_rare),
            "二星": pulls.count(student_2),
            "一星": pulls.count(student_1)
        }

        two_star_count = result["二星"]
        three_star_count = result["三星"]

        # 输出结果
        type_print("=== ㊙️蔚蓝档案十连抽结果㊙️ ===")
        ty_print(f"总抽数：10次")
        if three_star_count > 0:
            if students_rare in pulls:
                time.sleep(1)
                ty_print("😆😆😆!!")
                time.sleep(1)
                ty_print("🎉出彩啦！🎉 是限定！！")
                for rarity, count in result.items():
                    ty_print(f"{rarity}角色：{count}名")
                for i in range(len(pulls)):
                    if pulls[i] in students_rare:
                        pulls[i] = random.choice(students_rare)
                    if pulls[i] in student_2:
                        pulls[i] = random.choice(students_2)  # 每个名额随机抽二星角色
                    if pulls[i] in student_1:
                        pulls[i] = random.choice(students_1)
                ty_print(f"{pulls}")
                ty_print("阿罗娜要草莓味酸奶！🤤原味也行！！🤤（虽然忘记把彩收起来了...嘿嘿~~）")
            else:
                time.sleep(1)
                ty_print("^+^!!")
                time.sleep(1)
                ty_print("🎉出彩啦！")
                for rarity, count in result.items():
                    ty_print(f"{rarity}角色：{count}名")
                for i in range(len(pulls)):
                    if pulls[i] in students_3:
                        pulls[i] = random.choice(students_3)
                    if pulls[i] in student_2:
                        pulls[i] = random.choice(students_2)  # 每个名额随机抽二星角色
                    if pulls[i] in student_1:
                        pulls[i] = random.choice(students_1)
                ty_print(f"{pulls}")
                ty_print("还不快快奖励阿罗娜~~~~要草莓味酸奶！🤤原味？🤤也行....😉")

         # 判断：只有当二星数量恰好是1个且无三星时，执行命令
        elif two_star_count == 1 and three_star_count == 0:
            def tay_print(text, delay=0.3):

                """带打字效果的打印函数，text是要打印的内容，delay是每个字符的间隔时间"""
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(delay)
                print()  # 打印完换行
            tay_print("三星角色：0名")
            tay_print("二星角色：1名")
            tay_print("一星角色：9名")
            for i in range(len(pulls)):
                if pulls[i] in student_2:
                    pulls[i] = random.choice(students_2)  # 每个名额随机抽二星角色
                if pulls[i] in student_1:
                    pulls[i] = random.choice(students_1)
            print(pulls)

            tay_print("🤣AUV~ +19nie~ 九蓝一金🤡~")
            #无三星
        elif three_star_count == 0:
            for rarity, count in result.items():
                ty_print(f"{rarity}角色：{count}名")
            for i in range(len(pulls)):
                if pulls[i] in students_2:
                    pulls[i] = random.choice(students_2)  # 每个名额随机抽二星角色
                if pulls[i] in students_1:
                    pulls[i] = random.choice(students_1)
            print(f"{pulls}")

    return pulls


# 4. 核心执行函数（带资源扣减）
def execute_command(stone,point):
    try:
        type_print(f"目前青辉石💎：{stone}")
        type_print(f"point🎫：{point}")
        type_print("sensei请开始招募您想要的学生吧！❤️😆")

        a = int(input(":"))
        if a == 1:
            # 单抽逻辑（略，可自行补充）
            if stone < 120:
                type_print("青辉石不足😣，无法抽卡！")
                return stone, point
            stone -= 120
            # point增加
            point += 1
            import random

            # 步骤1：按概率选择列表（列表+对应概率）
            lists = [students_rare, students_3, students_2, students_1]
            list_weights = [0.007, 0.023, 0.185, 0.785]
            selected_list = random.choices(lists, weights=list_weights, k=1)[0]

            # 步骤2：从选中的列表中随机选1个元素
            selected_element = random.choice(selected_list)
            if selected_element in students_rare:
                def t1y_print(text, delay=0.3):
                    """带打字效果的打印函数，text是要打印的内容，delay是每个字符的间隔时间"""
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(delay)
                    print()  # 打印完换行

                t1y_print("呜嘿~")
                time.sleep(3)
                t1y_print("是：")
                print(selected_element + "!")
                t1y_print("好耶！是限定up😆")
                t1y_print("还不快快奖励阿罗娜~~~~要草莓味酸奶！🤤原味？🤤也行....😉")
            elif selected_element in students_3:
                def ty_print(text, delay=0.3):
                    """带打字效果的打印函数，text是要打印的内容，delay是每个字符的间隔时间"""
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(delay)
                    print()  # 打印完换行

                ty_print("呜嘿~")
                time.sleep(2)
                ty_print("是：")
                print(selected_element + "!")
                ty_print("好耶！是三星角色😆")
                ty_print("还不快快奖励阿罗娜~~~~要草莓味酸奶！🤤原味？🤤也行....😉")
            elif selected_element in students_2:
                def t2y_print(text, delay=0.3):
                    """带打字效果的打印函数，text是要打印的内容，delay是每个字符的间隔时间"""
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(delay)
                    print()  # 打印完换行

                t2y_print("呜嘿~")
                time.sleep(1)
                t2y_print("是：")
                print(selected_element + "  二星角色!")
            else:
                def ty1pe_print(text, delay=0.3):
                    """带打字效果的打印函数，text是要打印的内容，delay是每个字符的间隔时间"""
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(delay)
                    print()  # 打印完换行

                ty1pe_print("呜嘿~")
                time.sleep(1)
                ty1pe_print("是：")
                print(selected_element + "  一星角色!")



        elif a == 10:
            # 十连逻辑
            if stone < 1200:
                type_print("青辉石💎不足😣，无法十连！")
                return stone, point
            stone -= 1200
            point += 10
            blue_archive_gacha_10pull()
        else:
            type_print("sensei牡蛎！😣这样哒咩的！😫必须要好好惩罚一下老师了~🥵（-10青辉石💎）")
            stone -= 10
        return stone, point
    except:
        type_print("sensei牡蛎！😣这样哒咩的！😫必须要好好惩罚一下老师了~🥵（-10青辉石💎）")
        return stone - 10, point


# 5. 主循环（控制重复抽卡）
if __name__ == "__main__":
    stone = 6000  # 初始资源
    point = 0
    while True:
        stone,point = execute_command(stone,point)  # 执行抽卡，更新资源
        user_input = input("\nsensei还要继续抽吗😉？按e可以远离蓝色恶魔哟~🤣，按其他任意键继续~：")
        if user_input.strip().lower() == "e":
            type_print(f"剩余青辉石💎:{stone}|point:{point}")
            type_print("Sensei真的要走咩~๐·°(৹˃̵﹏˂̵৹)°·๐ ")
            break