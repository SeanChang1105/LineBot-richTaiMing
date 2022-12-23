import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message


load_dotenv()


machine = TocMachine(
    states=[
        'user',
        'menu',
        'choose_matches',
        'select_league',
        'premier_league',
        'la_liga',
        'ligue_1',
        'serie_A',
        'show_PL',
        'show_LL',
        'show_LG',
        'show_SA',
        'choose_lottery',
        'input_location',
        'input_radius',
        'show_stations'
    ],
    transitions=[
        {'trigger': 'advance', 'source': 'user', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
        {'trigger': 'advance', 'source': 'menu', 'dest': 'choose_matches', 'conditions': 'is_going_to_choose_matches'},
        {'trigger': 'advance', 'source': 'choose_matches', 'dest': 'select_league', 'conditions': 'is_going_to_select_league'},
        {'trigger': 'advance', 'source': 'choose_matches', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
        {'trigger': 'advance', 'source': 'select_league', 'dest': 'premier_league', 'conditions': 'is_going_to_premier_league'},
        {'trigger': 'advance', 'source': 'select_league', 'dest': 'la_liga', 'conditions': 'is_going_to_la_liga'},
        {'trigger': 'advance', 'source': 'select_league', 'dest': 'ligue_1', 'conditions': 'is_going_to_ligue_1'},
        {'trigger': 'advance', 'source': 'select_league', 'dest': 'serie_A', 'conditions': 'is_going_to_serie_A'},
        {'trigger': 'advance', 'source': 'premier_league', 'dest': 'show_PL', 'conditions': 'is_going_to_show_PL'},
        {'trigger': 'advance', 'source': 'premier_league', 'dest': 'select_league', 'conditions': 'is_going_to_select_league'},
        {'trigger': 'advance', 'source': 'la_liga', 'dest': 'show_LL', 'conditions': 'is_going_to_show_LL'},
        {'trigger': 'advance', 'source': 'la_liga', 'dest': 'select_league', 'conditions': 'is_going_to_select_league'},
        {'trigger': 'advance', 'source': 'ligue_1', 'dest': 'show_LG', 'conditions': 'is_going_to_show_LG'},
        {'trigger': 'advance', 'source': 'ligue_1', 'dest': 'select_league', 'conditions': 'is_going_to_select_league'},
        {'trigger': 'advance', 'source': 'serie_A', 'dest': 'show_SA', 'conditions': 'is_going_to_show_SA'},
        {'trigger': 'advance', 'source': 'serie_A', 'dest': 'select_league', 'conditions': 'is_going_to_select_league'},
        {'trigger': 'advance', 'source': 'menu', 'dest': 'choose_lottery', 'conditions': 'is_going_to_choose_lottery'},
        {'trigger': 'advance', 'source': 'choose_lottery', 'dest': 'input_location', 'conditions': 'is_going_to_input_location'},
        {'trigger': 'advance', 'source': 'choose_lottery', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
        {'trigger': 'advance', 'source': 'input_location', 'dest': 'input_radius', 'conditions': 'is_going_to_input_radius'},
        {'trigger': 'advance', 'source': 'input_radius', 'dest': 'show_stations', 'conditions': 'is_going_to_show_stations'},

        {'trigger': 'go_back',
            'source': [
                'show_PL',
                'show_LL',
                'show_LG',
                'show_SA',
                'show_BD',
                'show_stations',
            ],
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path='')


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

mode = 0

@app.route('/callback', methods=['POST'])
def webhook_handler():
    global mode
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f'Request body: {body}')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f'\nFSM STATE: {machine.state}')
        print(f'REQUEST BODY: \n{body}')

        response = machine.advance(event)

        if response == False:
            if event.message.text.lower() == 'fsm':
                send_text_message(event.reply_token, 'showing fsm image')
            elif machine.state == 'user':
                send_text_message(event.reply_token, '準備好跟郭台銘一樣有錢了嗎?\n Enter "menu" to start!')
            elif machine.state == 'input_location':
                send_text_message(event.reply_token, 'Please enter you location')
            elif machine.state == 'input_radius':
                send_text_message(event.reply_token, 'Please enter number!')
    return 'OK'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return send_file('fsm.png', mimetype='image/png')


if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port, debug=True)
