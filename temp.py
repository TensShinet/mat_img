formula_text_temps = [
    # 0 最简单模板
    {
        "begin": "$$\\begin{matrix}",
        "char_interval": "&",
        "line_interval": "\\\\",
        "end": "\\end{matrix}$$"
    },
    # 花括号模板
    {
        "begin": "$$\\left\\{\\begin{matrix}",
        "char_interval": "&",
        "line_interval": "\\\\",
        "end": "\\end{matrix}\\right\\}$$"
    },
    # 中括号模板
    {
        "begin": "$$\\left[\\begin{matrix}",
        "char_interval": "&",
        "line_interval": "\\\\",
        "end": "\\end{matrix}\\right]$$"
    }
]
