from fsm import TocMachine

def create_machine():
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
                'show_stations',
            ],
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
    )
    return machine