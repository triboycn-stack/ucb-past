# target6_statemachine.py
"""状态机 - 纯函数版本，适合 PAST 测试"""


def transition(state: str, counter: int, action: str) -> tuple:
    """
    状态转换纯函数
    输入: 当前状态, 计数器, 动作
    输出: (新状态, 新计数器, 结果消息)

    测试预期:
    - RUNNING 状态下 RESET 不生效 → 返回 NO_CHANGE
    - counter 最大为 10，达到后 INCREMENT 返回 NO_CHANGE
    - 类型错误时返回 NO_CHANGE
    """
    # 问题3修复：类型检查（PAST测试需要这个）
    if not isinstance(state, str) or not isinstance(counter, int) or not isinstance(action, str):
        return (state, counter, "NO_CHANGE")

    if state == "IDLE":
        if action == "START":
            return ("RUNNING", 0, "STARTED")
        elif action == "RESET":
            return ("IDLE", counter, "RESET")

    elif state == "RUNNING":
        # 问题1修复：RUNNING状态下RESET不应该生效
        if action == "RESET":
            return ("RUNNING", counter, "NO_CHANGE")
        elif action == "STOP":
            return ("STOPPED", counter, "STOPPED")
        elif action == "INCREMENT":
            # 问题2修复：counter 达到 10 后不能再增加
            if counter >= 10:
                return ("RUNNING", 10, "NO_CHANGE")

            new_counter = counter + 1
            if new_counter == 10:
                return ("COMPLETED", 10, "COMPLETED")
            return ("RUNNING", new_counter, "INCREMENTED")

    elif state == "STOPPED":
        if action == "RESUME":
            return ("RUNNING", counter, "RESUMED")
        elif action == "RESET":
            return ("IDLE", 0, "RESET")

    elif state == "COMPLETED":
        if action == "RESET":
            return ("IDLE", 0, "RESET")

    # 无效动作
    return (state, counter, "NO_CHANGE")


def validate_transition(state: str, action: str) -> bool:
    """验证状态转换是否有效"""
    valid_actions = {
        "IDLE": ["START", "RESET"],
        "RUNNING": ["STOP", "INCREMENT"],  # RESET 在 RUNNING 状态下无效
        "STOPPED": ["RESUME", "RESET"],
        "COMPLETED": ["RESET"]
    }
    return action in valid_actions.get(state, [])


def can_increment(state: str, counter: int) -> bool:
    """检查是否可以增加计数"""
    if state != "RUNNING":
        return False
    return counter < 10  # counter 最大为 9 时可以增加，10 时不可以


def get_next_action(state: str, counter: int) -> str:
    """根据当前状态推荐下一个动作"""
    if state == "IDLE":
        return "START"
    elif state == "RUNNING":
        if counter < 9:
            return "INCREMENT"  # 可以安全增加
        elif counter == 9:
            return "INCREMENT"  # 最后一次增加，会触发 COMPLETED
        else:  # counter == 10
            return "STOP"  # 已经达到上限，建议停止
    elif state == "STOPPED":
        return "RESUME"
    elif state == "COMPLETED":
        return "RESET"
    return "NO_CHANGE"


def process_sequence(actions: list) -> list:
    """处理一系列动作，返回结果列表"""
    state = "IDLE"
    counter = 0
    results = []

    for action in actions:
        state, counter, result = transition(state, counter, action)
        results.append({
            "action": action,
            "result": result,
            "state": state,
            "counter": counter
        })

    return results


# 为了方便测试，添加一个辅助函数
#def get_all_states():
#    """返回所有可能的状态"""
#    return ["IDLE", "RUNNING", "STOPPED", "COMPLETED"]


#def get_all_actions():
#    """返回所有可能的动作"""
#    return ["START", "STOP", "INCREMENT", "RESET", "RESUME"]