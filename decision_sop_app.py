import streamlit as st
import pandas as pd

st.set_page_config(page_title="顶级决策哲学家 SOP 系统", layout="wide")

# 初始化状态变量以保存用户输入
keys = [
    "step1_ideas", "step1_goal", "step2_facts", "step2_cooling",
    "step3_fail", "step3_cost", "step3_mech", "step3_loss", "step3_circle",
    "step4_10d", "step4_10m", "step4_10y", "step4_asym",
    "step5_prob", "step5_reward", "step5_loss", "step5_lolla",
    "step6_action", "step6_kpi", "step6_anti1", "step6_anti2", "step6_anti3",
    "step7_q1", "step7_q2", "step7_q3", "step7_q4", "step7_do", "step7_verify", "step7_avoid"
]
for k in keys:
    if k not in st.session_state:
        st.session_state[k] = ""
if "step5_prob" not in st.session_state or st.session_state.step5_prob == "":
    st.session_state.step5_prob = 50
if "step" not in st.session_state:
    st.session_state.step = 1

def load_example():
    st.session_state.update({
        "step1_ideas": "想要提升英语口语\n想考雅思拿7分以上\n想去外企拿高薪或者出国读研\n怕自己坚持不下来\n不想花太多钱报天价班",
        "step1_goal": "在6个月的时间和2万元预算限制下，我只追求雅思总分达到7.0，内心不再纠结。",
        "step2_facts": "1. 官方规则：雅思考试费约2170元。\n2. 市场平均：中国考生平均备考需要300小时，雅思7分通过率约12%。\n3. 历史数据：我过往四级裸考500分，目前词汇量约4500。",
        "step2_cooling": True,
        "step3_fail": "1. 每天只背单词，不练口语输出。\n2. 沉迷于收集各个名师的资料而不做剑桥真题。\n3. 考前一周极度焦虑导致失眠。",
        "step3_cost": "总计约1.5万元人民币（考试费+资料+外教口语课） + 每天3小时×180天（约540小时）。",
        "step3_mech": "通过高强度的定向刻意练习（System 2工作）达到雅思考试要求，从而拿到Top名校Offer或外企面试门票。",
        "step3_loss": "损失1.5万元，白学6个月，但英语底子还在，随时可以重考。",
        "step3_circle": True,
        "step4_10d": "每天下班/放学后极度疲惫，还要强迫自己听写听力和背单词，十分痛苦。",
        "step4_10m": "已经拿到了雅思7分成绩单，正在自信地进行全英文的学校申请或外企面试。",
        "step4_10y": "在跨国公司或海外工作，英语已成为获取全球一线信息的无障碍工具。",
        "step4_asym": True,
        "step5_prob": 40,
        "step5_reward": 90,
        "step5_loss": 20,
        "step5_lolla": "逻辑成立 + 数据EV为正 + 是典型的不对称机会（下行风险极小，上行收益极大） + 逆向思维已排雷。四大因素汇聚，决定执行！",
        "step6_action": "今晚8点前，在雅思官网注册账号并报名下个月的一场考试倒逼自己。",
        "step6_kpi": "每周六上午严格按照真实考试时间，完成一套完整的剑桥雅思全真模考。",
        "step6_anti1": "连续两周模考阅读分数低于6.5分。",
        "step6_anti2": "连续三天因为各种借口没有完成每天3小时的学习量。",
        "step6_anti3": "口语录音回放时自己都听不懂（发音清晰度停滞）。",
        "step7_q1": "预计每天能坚持3小时高强度学习，6个月顺利考到7分。",
        "step7_q2": "实际前两个月每天只学了1.5小时，中间断更了一周，最终花了8个月考到6.5分。",
        "step7_q3": "规划谬误（Kahneman）：严重低估了执行过程中的疲劳感；过度自信导致时间规划不合理。",
        "step7_q4": "下次做长期计划时，时间估算必须直接乘以1.5倍。引入外部监督机制（如打卡群）。",
        "step7_do": "需要长期纪律积累的硬技能学习（如语言、健身）。",
        "step7_verify": "需要主观判断的趋势投资（必须找人验证）。",
        "step7_avoid": "没有任何容错率、亏光本金的短期投机。"
    })

def clear_data():
    for k in keys:
        if isinstance(st.session_state.get(k), bool):
            st.session_state[k] = False
        elif k == "step5_prob":
            st.session_state[k] = 50
        else:
            st.session_state[k] = ""

st.title("🧠 顶级决策哲学家 SOP 互动工作台")
st.markdown("融合 **Naval（不对称收益）**、**Munger（逆向思维）** 和 **Kahneman（系统1与系统2）** 的底层逻辑。此版本支持**文本输入保存**，并在侧边栏提供**真实案例一键载入**功能。")

st.sidebar.header("🎯 控制面板")
if st.sidebar.button("💡 一键载入【雅思备考】案例", help="加载一个完整的案例帮助你理解每一步怎么填"):
    load_example()
if st.sidebar.button("🗑️ 清空所有数据"):
    clear_data()

st.sidebar.markdown("---")
st.sidebar.header("📂 决策步骤导航")
steps = [
    "1. 明确唯一目标", "2. 查客观事实", "3. 第一性原理追问", 
    "4. 长期推演", "5. 计算概率与EV", "6. 执行与反馈闭环", 
    "7. 复盘与系统更新", "8. 📊 完整决策报告"
]

for i, step_name in enumerate(steps, 1):
    if st.sidebar.button(step_name, key=f"nav_{i}"):
        st.session_state.step = i

def nav_buttons():
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.step > 1:
            if st.button("⬅️ 上一步"):
                st.session_state.step -= 1
                st.rerun()
    with col2:
        if st.session_state.step < 8:
            if st.button("下一步 ➡️"):
                st.session_state.step += 1
                st.rerun()

# ----------------- Step 1 -----------------
if st.session_state.step == 1:
    st.header("第一步：明确唯一的决策目标")
    st.error("⚠️ **Kahneman 认知警告：WYSIATI陷阱 & System 1 第一反应不可信**\n你看到的只是脑海里浮现的，必须强制启动 System 2 慢思考。")

    st.subheader("动作一：列出并两两 PK 淘汰")
    st.write("把你关于这件事的所有想法和诉求写下来。然后两两对比，强制淘汰，直到剩下一个绝对不能妥协的目标。")
    st.text_area("✍️ 诉求清单（每行一条，写完在脑海中两两PK）", key="step1_ideas", height=150)

    st.warning("💡 **Naval 检验法**：用『内心是否纠结』作为检验器。还在纠结，答案就是不做。把目标限定在【人、事、地点】上。")

    st.subheader("交付结果")
    st.text_input("🎯 带有明确数字约束的唯一目标：", key="step1_goal", placeholder="在___限制下，我只追求___，内心不再纠结。")
    nav_buttons()

# ----------------- Step 2 -----------------
elif st.session_state.step == 2:
    st.header("第二步：只查客观的数据和事实")
    st.error("⚠️ **Kahneman 认知警告：锚定偏误、可得性启发、确认偏误**\n不要被第一个数字锚定，不要只看支持你的证据。")
    st.warning("💡 **Naval 警告**：拒绝众包决策！如果你想做出错误的决定，就去问所有人。只查数据，不问意见。")

    st.subheader("动作一：情绪词清除 & 三类硬信息清单")
    st.write("只查客观的：1. 官方规则 2. 市场平均数据 3. 历史真实数据（要求标明来源，去除'据说/太坑了'等主观词汇）。")
    st.text_area("📊 你的事实清单（必须带数字和来源）：", key="step2_facts", height=200)

    st.subheader("动作二：主动冷却，强制延迟")
    st.checkbox("我已经隔了一晚，让 System 1 冷却，由 System 2 接管审查事实漏洞。", key="step2_cooling")
    nav_buttons()

# ----------------- Step 3 -----------------
elif st.session_state.step == 3:
    st.header("第三步：用第一性原理追问决策的本质")
    st.error("⚠️ **Kahneman 认知警告：内部视角陷阱**\n人总是把自己的情况当成独一无二的，从而系统性高估成功率。")

    st.subheader("动作一：芒格逆向思维 (Inversion)")
    st.warning("💡 **Munger**：我只想知道我会死在哪里，这样我就永远不去那里。")
    st.text_area("💀 失败路径清单（列出保证这个决策失败的前提条件，以及你如何规避）：", key="step3_fail", height=120)

    st.subheader("动作二：三个底层追问")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_area("💰 真实总成本（钱+时间）：", key="step3_cost", height=100)
    with col2:
        st.text_area("⚙️ 收益产生机制（非运气）：", key="step3_mech", height=100)
    with col3:
        st.text_area("📉 最坏情况具体损失：", key="step3_loss", height=100)

    st.checkbox("🔍 芒格能力圈自检：我能清晰解释以上机制，这在我的能力圈内。", key="step3_circle")
    nav_buttons()

# ----------------- Step 4 -----------------
elif st.session_state.step == 4:
    st.header("第四步：推演各选项的长期结果")
    st.error("⚠️ **Kahneman 认知警告：规划谬误**\n人们几乎永远低估时间和成本。请把你以为的时间×1.5倍，成本×2倍进行推演！")

    st.subheader("动作一：三层时间线推演")
    st.warning("💡 **Naval**：短期更痛苦的选项，往往是长期正确的选项。")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_area("⏳ 10天后（日常状态）：", key="step4_10d", height=150)
    with col2:
        st.text_area("📅 10个月后（能力/处境）：", key="step4_10m", height=150)
    with col3:
        st.text_area("🚀 10年后（核心资产/竞争力）：", key="step4_10y", height=150)

    st.subheader("动作二：识别不对称机会")
    st.warning("💡 **Munger 二阶思维**：不断追问'然后呢？'。**Naval**：寻找下行风险有限、上行收益无上限的机会。")
    st.checkbox("⚖️ 这是一个不对称机会（最坏结果固定可承受，最好结果想象空间开放）", key="step4_asym")
    nav_buttons()

# ----------------- Step 5 -----------------
elif st.session_state.step == 5:
    st.header("第五步：计算概率与期望值 (EV)")
    st.error("⚠️ **Kahneman 认知警告：过度自信偏误 & 损失厌恶**\n你的成功率必须打八折！如果你问自己'一年后这损失还影响我吗'答案是否，请调低损失权重。")

    st.subheader("期望值计算器")
    st.slider("从外部视角（基础概率）估算您的原始成功率 (%)", 0, 100, key="step5_prob")
    adj_prob = st.session_state.step5_prob * 0.8

    col1, col2 = st.columns(2)
    with col1:
        st.number_input("成功带来的具体收益量化得分 (0-100)", 0, 100, key="step5_reward")
    with col2:
        st.number_input("失败造成的客观损失量化得分 (0-100)", 0, 100, key="step5_loss")

    ev = ((adj_prob/100) * st.session_state.step5_reward) - ((1 - adj_prob/100) * st.session_state.step5_loss)

    st.info(f"🔢 **打八折后的真实概率：{adj_prob:.1f}%** | 📈 **计算得出的期望值 (EV): {ev:.2f}**")
    if ev > 0:
        st.success("✅ EV 为正。")
    else:
        st.error("❌ EV 为负，建议放弃或重新设计。")

    st.warning("💡 **Munger 多因素汇聚检验 (Lollapalooza)**：是否有多个独立因素指向同一结论？")
    st.text_area("🧩 多因素汇聚结论说明（逻辑+数据+推演+逆向）：", key="step5_lolla", height=100)
    nav_buttons()

# ----------------- Step 6 -----------------
elif st.session_state.step == 6:
    st.header("第六步：执行并建立反馈闭环")
    st.error("⚠️ **Kahneman 认知警告：确认偏误**\n一旦执行，大脑会自动保护决策，只看支持证据。")
    st.warning("💡 **Naval 警告**：自我服务性结论（恰好证明我是对的）需要更高的证据门槛。")

    st.subheader("动作：设定执行指令与客观指标")
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("🏃 第一步具体动作（今天就能做的最小动作）：", key="step6_action", height=100)
    with col2:
        st.text_area("📏 衡量效果的客观 KPI 指标（必须是数字）：", key="step6_kpi", height=100)

    st.subheader("🎯 预设『反例触发器』")
    st.write("每次阶段回顾，强制先找三条【证明决策是错的】证据：")
    st.text_input("反证 1：", key="step6_anti1")
    st.text_input("反证 2：", key="step6_anti2")
    st.text_input("反证 3：", key="step6_anti3")
    nav_buttons()

# ----------------- Step 7 -----------------
elif st.session_state.step == 7:
    st.header("第七步：对比结果，找出系统性漏洞 (复盘)")
    st.error("⚠️ **Kahneman 认知警告：事后诸葛亮偏误**\n人们会扭曲记忆说'我早就知道'。必须对照第一步到第六步的原始记录复盘！")

    st.subheader("动作一：四问复盘法 (AAR) + 事前验尸法反用")
    st.text_area("1. 当初预计会发生什么（查阅原始记录）？", key="step7_q1")
    st.text_area("2. 实际发生了什么（写客观数字）？", key="step7_q2")
    st.text_area("3. 偏差出在哪一步（目标漂移/概率高估/规划谬误）？", key="step7_q3")
    st.text_area("4. 下次如何具体改变（落实到SOP某一步）？", key="step7_q4")

    st.subheader("动作二：更新能力圈边界 (Munger)")
    st.text_input("✅ 可以独立做的决策类型：", key="step7_do")
    st.text_input("⚠️ 必须引入外部验证的决策：", key="step7_verify")
    st.text_input("⛔ 永远回避的系统性弱点领域：", key="step7_avoid")
    nav_buttons()

# ----------------- Step 8 -----------------
elif st.session_state.step == 8:
    st.header("📊 您的决策 SOP 完整报告")
    st.success("🎉 以下是您在整个决策流程中生成的结构化记录。")

    report_md = f"""
### 1. 唯一目标
- **原始诉求**: {st.session_state.step1_ideas}
- **最终唯一目标**: {st.session_state.step1_goal}

### 2. 客观事实
- **事实清单**: {st.session_state.step2_facts}
- **是否通过冷却期**: {'是' if st.session_state.step2_cooling else '否'}

### 3. 第一性原理追问
- **失败路径规避 (Munger逆向)**: {st.session_state.step3_fail}
- **真实总成本**: {st.session_state.step3_cost}
- **收益机制**: {st.session_state.step3_mech}
- **最坏损失**: {st.session_state.step3_loss}
- **在能力圈内**: {'是' if st.session_state.step3_circle else '否'}

### 4. 长期推演 (10/10/10)
- **10天后**: {st.session_state.step4_10d}
- **10个月后**: {st.session_state.step4_10m}
- **10年后**: {st.session_state.step4_10y}
- **是否为不对称机会**: {'是' if st.session_state.step4_asym else '否'}

### 5. 期望值 (EV) 与多因素汇聚
- **打折后成功率**: {st.session_state.step5_prob * 0.8}%
- **成功收益 / 失败损失**: {st.session_state.step5_reward} / {st.session_state.step5_loss}
- **多因素汇聚结论**: {st.session_state.step5_lolla}

### 6. 执行与闭环
- **今日第一步动作**: {st.session_state.step6_action}
- **客观 KPI**: {st.session_state.step6_kpi}
- **反例触发器**: 
  1. {st.session_state.step6_anti1}
  2. {st.session_state.step6_anti2}
  3. {st.session_state.step6_anti3}

### 7. 复盘与能力圈更新
- **AAR 偏差分析**: {st.session_state.step7_q3}
- **能力圈更新**:
  - ✅ 擅长领域: {st.session_state.step7_do}
  - ⚠️ 需验证领域: {st.session_state.step7_verify}
  - ⛔ 永远回避: {st.session_state.step7_avoid}
"""
    st.markdown(report_md)
    st.download_button("📥 导出 Markdown 报告", data=report_md, file_name="决策SOP报告.md", mime="text/markdown")
    nav_buttons()
