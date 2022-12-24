from transitions.extensions import GraphMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
import pandas as pd
import googlemaps

#global variables
location_name=''
radius=1000

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self,event):
        text = event.message.text
        if(text=='menu' or ((self.state=='choose_matches' or self.state=='choose_lottery') and text=='back')):
            return True

    # menu
    def on_enter_menu(self, event):
        title = 'Choose your action!'
        text = 'Look for recent matches or lottery stations nearby.'
        btn = [
            MessageTemplateAction(
                label = 'matches',
                text ='matches'
            ),
            MessageTemplateAction(
                label = 'lottery',
                text = 'lottery'
            ),
        ]
        url = 'https://www.honhai.com/img/about/group-profile/founder-m.png?5f65a'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_choose_matches(self, event):
        text = event.message.text
        if(text=='matches'):
            return True
        return False

    def is_going_to_choose_lottery(self, event):
        text = event.message.text
        if(text=='lottery'):
            return True
        return False
    
    # choose matches
    def on_enter_choose_matches(self,event):
        title = 'Chosing matches'
        text = 'confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Sydney-Galaxy-homebush.jpg/800px-Sydney-Galaxy-homebush.jpg'
        send_button_message(event.reply_token, title, text, btn,url)

    def is_going_to_select_league(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='choose_matches') or ((self.state=='premier_league' or self.state=='la_liga' or self.state=='ligue_1' or self.state=='serie_A' or self.state=='bundesliga')and text=='back'):
            return True
        return False

    # select league
    def on_enter_select_league(self, event):
        title = 'Select a league:'
        text = 'from the major leagues'
        btn = [
            MessageTemplateAction(
                label = 'Premier League',
                text ='PL'
            ),
            MessageTemplateAction(
                label = 'La Liga',
                text = 'LL'
            ),
            MessageTemplateAction(
                label = 'Ligue 1',
                text = 'LG'
            ),
            MessageTemplateAction(
                label = 'Serie A',
                text = 'SA'
            ),
        ]
        url = 'https://thumbs.dreamstime.com/b/%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-rgb-official-uefa-european-top-league-logos-set-football-soccer-leagues-logo-premier-laliga-serie-262254180.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_premier_league(self,event):
        text = event.message.text
        if(text=='PL'):
            return True
        return False

    def is_going_to_la_liga(self,event):
        text = event.message.text
        if(text=='LL'):
            return True
        return False

    def is_going_to_ligue_1(self,event):
        text = event.message.text
        if(text=='LG'):
            return True
        return False

    def is_going_to_serie_A(self,event):
        text = event.message.text
        if(text=='SA'):
            return True
        return False
    

    # premier league
    def on_enter_premier_league(self,event):
        title='Premier League'
        text='confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://static.vecteezy.com/system/resources/previews/010/994/451/original/premier-league-logo-symbol-with-name-design-england-football-european-countries-football-teams-illustration-with-purple-background-free-vector.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_show_PL(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='premier_league'):
            return True
        return False

    # la liga
    def on_enter_la_liga(self,event):
        title='La Liga'
        text='confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://assets.laliga.com/assets/logos/laliga-v/laliga-v-1200x1200.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_show_LL(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='la_liga'):
            return True
        return False

    # ligue 1
    def on_enter_ligue_1(self,event):
        title='Ligue 1'
        text='confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/49/Ligue1_Uber_Eats_logo.png'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_show_LG(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='ligue_1'):
            return True
        return False

    # serie A
    def on_enter_serie_A(self,event):
        title='Serie A'
        text='confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Serie_A_logo_2022.svg/800px-Serie_A_logo_2022.svg.png'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_show_SA(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='serie_A'):
            return True
        return False

    # show PL
    def on_enter_show_PL(self,event):
        url='https://www.theguardian.com/football/premierleague/fixtures'
        html_text=requests.get(url).text
        soup=BeautifulSoup(html_text,'html.parser')
        matches_days=soup.find_all('div',class_='football-matches__day')
        matchDaysCount=3 #matches in recent 3 matchdays
        outputString='Premier League matches in the recent 3 days:\n'
        for matches_day in matches_days:
            if(matchDaysCount==0):break
            date=matches_day.find('div', class_='date-divider')
            teams=matches_day.find_all('span', class_='team-name__long')
            idx=0
            outputString+=date.text+"\n"
            for team in teams:
                if(idx%2==0):
                    str=''
                    str+=team.text+" vs "
                else:
                    str+=team.text
                    outputString+=str+'\n'
                idx+=1
            outputString+='\n'
            matchDaysCount-=1
        send_text_message(event.reply_token, outputString)
        self.go_back()
        
    # show LL
    def on_enter_show_LL(self,event):
        url='https://www.theguardian.com/football/laligafootball/fixtures'
        html_text=requests.get(url).text
        soup=BeautifulSoup(html_text,'html.parser')
        matches_days=soup.find_all('div',class_='football-matches__day')
        matchDaysCount=3 #matches in recent 3 matchdays
        outputString='La liga matches in the recent 3 days:\n'
        for matches_day in matches_days:
            if(matchDaysCount==0):break
            date=matches_day.find('div', class_='date-divider')
            teams=matches_day.find_all('span', class_='team-name__long')
            idx=0
            outputString+=date.text+"\n"
            for team in teams:
                if(idx%2==0):
                    str=''
                    str+=team.text+" vs "
                else:
                    str+=team.text
                    outputString+=str+'\n'
                idx+=1
            outputString+='\n'
            matchDaysCount-=1
        send_text_message(event.reply_token, outputString)
        self.go_back()

    # show LG
    def on_enter_show_LG(self,event):
        url='https://www.theguardian.com/football/ligue1football/fixtures'
        html_text=requests.get(url).text
        soup=BeautifulSoup(html_text,'html.parser')
        matches_days=soup.find_all('div',class_='football-matches__day')
        matchDaysCount=3 #matches in recent 3 matchdays
        outputString='Ligue 1 matches in the recent 3 days:\n'
        for matches_day in matches_days:
            if(matchDaysCount==0):break
            date=matches_day.find('div', class_='date-divider')
            teams=matches_day.find_all('span', class_='team-name__long')
            idx=0
            outputString+=date.text+"\n"
            for team in teams:
                if(idx%2==0):
                    str=''
                    str+=team.text+" vs "
                else:
                    str+=team.text
                    outputString+=str+'\n'
                idx+=1
            outputString+='\n'
            matchDaysCount-=1
        send_text_message(event.reply_token, outputString)
        self.go_back()


    # show SA
    def on_enter_show_SA(self,event):
        url='https://www.theguardian.com/football/serieafootball/fixtures'
        html_text=requests.get(url).text
        soup=BeautifulSoup(html_text,'html.parser')
        matches_days=soup.find_all('div',class_='football-matches__day')
        matchDaysCount=3 #matches in recent 3 matchdays
        outputString='Serie A matches in the recent 3 days:\n'
        for matches_day in matches_days:
            if(matchDaysCount==0):break
            date=matches_day.find('div', class_='date-divider')
            teams=matches_day.find_all('span', class_='team-name__long')
            idx=0
            outputString+=date.text+"\n"
            for team in teams:
                if(idx%2==0):
                    str=''
                    str+=team.text+" vs "
                else:
                    str+=team.text
                    outputString+=str+'\n'
                idx+=1
            outputString+='\n'
            matchDaysCount-=1
        send_text_message(event.reply_token, outputString)
        self.go_back()


    # choose lottery
    def on_enter_choose_lottery(self,event):
        title = 'looking for lottery stations'
        text = 'confirm?'
        btn = [
            MessageTemplateAction(
                label = 'confirm',
                text ='confirm'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Taiwan_Sports_Lottery_Logo.svg/200px-Taiwan_Sports_Lottery_Logo.svg.png'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_input_location(self,event):
        text = event.message.text
        if(text=='confirm' and self.state=='choose_lottery'):
            return True
        return False
    
    # input location
    def on_enter_input_location(self,event):
        send_text_message(event.reply_token, 'Enter your location name: \n(Ex.國立成功大學)')

    def is_going_to_input_radius(self,event):
        text = event.message.text
        global location_name
        location_name=text
        if(text!='' and self.state=='input_location'):
            return True
        return False

    # input radius
    def on_enter_input_radius(self,event):
        send_text_message(event.reply_token, 'Enter radius in meters: \nex.1000')

    def is_going_to_show_stations(self,event):
        global radius
        text = event.message.text
        radius=text
        if(text.lower().isnumeric() and self.state=='input_radius'):
            return True
        return False

    # show stations
    def on_enter_show_stations(self,event):
        global location_name
        global radius
        API_KEY='AIzaSyBODX1wRbkzmQ55kZJIUiFNuQoM0SZzGUE'
        map_client=googlemaps.Client(API_KEY)
        response=map_client.places(query=location_name)
        result=response.get('results')
        if(result): #if is not empty(places exist)
            lat=result[0]['geometry']['location']['lat']
            lng=result[0]['geometry']['location']['lng']
            search_string='台灣運彩'
            businessList=[]
            response=map_client.places_nearby(
            location=(lat,lng),
            keyword=search_string,
            radius=radius,
            language='zh-tw'
            )
            businessList.extend(response.get('results'))
            if(businessList):
                df=pd.DataFrame(businessList)
                df['url']='https://www.google.com/maps/place/?q=place_id:'+df['place_id']
                df.sort_values(by=['rating'],inplace=True,ascending=False)
                output=''
                for i in df['url']:
                    output+=i+'\n'
                send_text_message(event.reply_token, 'showing nearby lottery stations:\n'+output)
            else:
                send_text_message(event.reply_token, 'No match found!')
            
        else:
            send_text_message(event.reply_token, 'Your location does not exist!')


        self.go_back()