import os
import requests
import temp


def formula_as_file(formula, file, negate=False):
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get(
        'http://latex.codecogs.com/png.latex?\dpi{300} \huge %s' % formula)
    f = open(tfile, 'wb')
    f.write(r.content)
    f.close()
    if negate:
        os.system('convert tmp.png -channel RGB -negate -colorspace rgb %s' % file)


def generate_formula(mat, choice=0):

    formula_text_temp = temp.formula_text_temps[choice]
    formula_text = formula_text_temp["begin"]
    
    cols = len(mat[0])
    rows = len(mat)

    for i in range(cols):
        for j in range(rows):
            if j == 0:
                formula_text += str(mat[i][0])
            else:
                formula_text += (formula_text_temp["char_interval"] + str(mat[i][0]))
        if i == cols - 1:
            continue
        else:
            formula_text += formula_text_temp["line_interval"]

    formula_text += formula_text_temp["end"]

    return formula_text


def main():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [10, 10, 10]
    ]

    formula_text = generate_formula(a, 2)
    formula_as_file(formula_text, "test2.png")


if __name__ == "__main__":
    main()
