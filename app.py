from flask import Flask, render_template
from game import Game


app = Flask(__name__)
game = Game()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')


@app.route('/start_game/', methods=['POST'])
def new_game():
    game.clear()
    return game.set_levels()


@app.route('/level/<num>', methods=['POST'])
def level(num):
    num = int(num)
    return game.start_level(num)


@app.route('/click/<item>', methods=['POST'])
def click(item):
    if game.check_win(item):
        return win()
    return game.next_level_state(item)


@app.route('/win/', methods=['POST'])
def win():
    win_message = game.get_win_message()
    return render_template('win.html', message=win_message)


if __name__ == "__main__":
    app.run(debug=True)