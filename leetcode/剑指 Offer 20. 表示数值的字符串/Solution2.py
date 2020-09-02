class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            "STATE_INITIAL",    # 初始状态
            "STATE_SIGN",       # 符号
            "STATE_INTEGER",    # 整数部分
            "STATE_POINT",      # 小数点
            "STATE_POINT_WITHOUT_INT",  # 仅有小数点
            "STATE_FRACTION",   # 小数部分
            "STATE_EXP",        # 科学计数法e
            "STATE_EXP_SIGN",   # 科学计数法e符号
            "STATE_EXP_NUMBER", # 科学计数法数字
            "STATE_END",        # 结束
        ]
        charType = [
            "CHAR_NUMBER",  # 数字
            "CHAR_EXP",     # e
            "CHAR_POINT",   # 小数点
            "CHAR_SIGN",    # 符号
            "CHAR_END",     # 结束
            "CHAR_ILLEGAL", # 不合法字符
        ]

        def toCharType(ch):
            if ch.isdigit():
                return "CHAR_NUMBER"
            elif ch.lower() == "e":
                return "CHAR_EXP"
            elif ch == ".":
                return "CHAR_POINT"
            elif ch == "+" or ch == "-":
                return "CHAR_SIGN"
            else:
                return "CHAR_ILLEGAL"

        transfer = {
            "STATE_INITIAL": {
                "CHAR_NUMBER": "STATE_INTEGER",
                "CHAR_POINT": "STATE_POINT_WITHOUT_INT",
                "CHAR_SIGN": "STATE_SIGN",
            },
            "STATE_SIGN": {
                "CHAR_NUMBER": "STATE_INTEGER",
                "CHAR_POINT": "STATE_POINT_WITHOUT_INT",
            },
            "STATE_INTEGER": {
                "CHAR_NUMBER": "STATE_INTEGER",
                "CHAR_EXP": "STATE_EXP",
                "CHAR_POINT": "STATE_POINT",
                "CHAR_END": "STATE_END",
            },
            "STATE_POINT": {
                "CHAR_NUMBER": "STATE_FRACTION",
                "CHAR_EXP": "STATE_EXP",
                "CHAR_END": "STATE_END",
            },
            "STATE_POINT_WITHOUT_INT": {
                "CHAR_NUMBER": "STATE_FRACTION",
            },
            "STATE_FRACTION": {
                "CHAR_NUMBER": "STATE_FRACTION",
                "CHAR_EXP": "STATE_EXP",
                "CHAR_END": "STATE_END",
            },
            "STATE_EXP": {
                "CHAR_NUMBER": "STATE_EXP_NUMBER",
                "CHAR_SIGN": "STATE_EXP_SIGN",
            },
            "STATE_EXP_SIGN": {
                "CHAR_NUMBER": "STATE_EXP_NUMBER",
            },
            "STATE_EXP_NUMBER": {
                "CHAR_NUMBER": "STATE_EXP_NUMBER",
                "CHAR_END": "STATE_END",
            },
            "STATE_END": {
                "CHAR_END": "STATE_END",
            },
        }

        currentState = "STATE_INITIAL"
        s = s.strip()
        for word in s:
            strCharType = toCharType(word)
            if strCharType not in transfer[currentState]:
                return False
            currentState = transfer[currentState][strCharType]
        return currentState in ["STATE_INTEGER", "STATE_POINT", "STATE_FRACTION", "STATE_EXP_NUMBER", "STATE_END"]
