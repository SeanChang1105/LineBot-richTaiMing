LineBot-richTaiMing :soccer: 🤖 :money_with_wings:
===
2022 Fall Theory of computation final project by F74096352 張育維

Story
---
The FIFA 2022 World Cup came to an end on December 18. As a football enthusiast, I watched pretty much all of the games with some friends. We also spent some money on buying sport lottery but always ended up losing.

A wise Chinese man once said: **"小賭怡情，大賭郭台銘"**.

This means spending a little bit of money on lottery is fun, but spending a lot of money on it can make you become Guō Táimíng(郭台銘), whom is very rich.

I hope to be like Guō Táimíng in the future, so I made this Line bot to help me achieve the dream.

Line Bot Introduction
---
### Basic information
Line Bot name: 大賭郭台銘
Line Bot ID:@945eenxd
![profile](https://i.imgur.com/NlTiLER.jpg)

### Features
- Look up for some football matches in the major european leagues. 
- Look up for nearby lottery stations according to the input location.

#### Menu
- Type "menu" to open up the menu.

![](https://i.imgur.com/j8MmhSo.png)
- Choose "matches" to look for upcoming football matches
- Choose "lottery" to look for nearby lottery stations.

#### Football matches
![](https://i.imgur.com/mfnvYp2.png)

Choose "confirm" to continue, or choose "back" to go back to the menu.
Choose the desired league from:
1. Premier League(英超)
2. La Liga(西甲)
3. Ligue 1(法甲)
4. Serie A(義甲)

(The Line button can only have four options, sorry to all the Bundesliga fans :cry: )

![](https://i.imgur.com/NTtba66.png)

After choosing the desired league, hit confirm to see the upcoming coming matches within 3 match days.

#### Lottery stations
![](https://i.imgur.com/R0KsUKL.png)

Hit "confirm" to continue or "back" to gack to the menu.

![](https://i.imgur.com/yWNSHkC.png)

Enter location name and search radius.

![](https://i.imgur.com/L2TL4Ls.png)

All lottery staions in the radius will be printed (in the form of Google Maps URL) and sorted by ratings (Highest first).

FSM Structure
---
![](https://i.imgur.com/In7uvjB.png)

Extra functionalites used in this project
---
- web crawling
- Google Maps service API
- Line API
