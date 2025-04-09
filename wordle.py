from flask import Flask, request, render_template
from markupsafe import escape

try:
    from create_message import hantei
except:
    pass

try:
    from create_message import reset
except:
    pass

try:
    from create_message import hint
except:
    pass

try:
    from create_message import vs
except:
    pass

try:
    from create_message import answer
except:
    pass

try:
    from create_message import helps
except:
    pass

try:
    from create_message import debug_message
except:
    pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ''
    current_message = ''
    message = ''
    selected_option1 = ''
    selected_option2 = ''
    debug = False
    vsai_flag = False
    options1 = ['指定なし', 'ノーマル', 'ほのお', 'みず', 'でんき', 'くさ', 'こおり', 'かくとう', 'どく', 'じめん', 'ひこう', 'エスパー', 'むし', 'いわ', 'ゴースト', 'ドラゴン','あく', 'はがね']
    options2 = options1
    if request.method == 'POST':
        message = request.form.get('current_message', '')
        user_input_raw = request.form.get('user_input', '')
        user_input = str(escape(user_input_raw))
        if 'debug' in request.form:
            message += debug_message(user_input, request.form) + "<br>"
        if 'vsai' in request.form:
            message += vs(user_input) + "<br>"
        elif 'helps' in request.form:
            message += helps() + "<br>"
        elif 'hint' in request.form:
            message += hint() + "<br>"
        elif 'answer' in request.form:
            message += answer() + "<br>"
        elif 'reset' in request.form:
            selected_option1 = request.form.get('options1')
            selected_option2 = request.form.get('options2')
            current_message = ''
            message = reset(selected_option1, selected_option2)
        else:
            user_input_raw = request.form.get('user_input', '')
            user_input = str(escape(user_input_raw))
            message += hantei(user_input) + "<br>"
    return render_template('index.html', user_input=user_input, message=message, current_message=current_message, debug=debug, options1=options1, options2=options2, selected_option1=selected_option1, selected_option2=selected_option2)

if __name__ == "__main__":
    app.run(debug=True)