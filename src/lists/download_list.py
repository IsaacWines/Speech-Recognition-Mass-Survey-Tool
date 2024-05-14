import os
import sys
def get_list():
    country_path, metal_path, hip_hop_path, pop_path, rock_path = paths()
    return {
        'road': {'path': country_path, 'link': 'https://youtu.be/M6Ggp3TJjuE?si=S2W1Orj0rC9RqxKJ', 'artist': 'Willie Nelson', 'real_name': 'On the Road Again'},
        'alone': {'path': country_path, 'link': 'https://youtu.be/yZdfXkqe8lo?si=ZRTv-9RVJ6-yAkVS', 'artist': 'Hank Williams', 'real_name': 'Alone and Forsaken'},
        'gamble': {'path': country_path, 'link': 'https://youtu.be/7hx4gdlfamo?si=aKk8y7Vup0-KEyge', 'artist': 'Kenny Rogers', 'real_name': 'The Gambler'},
        'jolene': {'path': country_path, 'link': 'https://youtu.be/Ixrje2rXLMA?si=FM9Ku0CjlZkL0Q1A', 'artist': 'Dolly Parton', 'real_name': 'Jolene'},
        'dance': {'path': country_path, 'link': 'https://youtu.be/6FHvP_Yv0wE?si=0QJv672uGvf7FfFw', 'artist': 'Garth Brooks', 'real_name': 'The Dance'},
        'islands': {'path': country_path, 'link': 'https://youtu.be/KSc9TCFuuJM?si=LW3Tw2GfBn3zPIQN', 'artist': 'Kenny Rogers', 'real_name': 'Islands In The Stream'},
        'iron': {'path': country_path, 'link': 'https://youtu.be/-NuX79Ud8zI?si=piAyAnw_IVH61gaj', 'artist': 'Marty Robbins', 'real_name': 'Big Iron'},
        'takemehome': {'path': country_path, 'link': 'https://youtu.be/1vrEljMfXYo?si=GE0NBfGBpD4L3Osv', 'artist': 'John Denver', 'real_name': 'Take Me Home, Country Roads'},
        'thunder': {'path': country_path, 'link': 'https://youtu.be/tdsJI8Wc2D4?si=ZW7-T_NX-Vo0EueE', 'artist': 'Garth Brooks', 'real_name': 'The Thunder Rolls'},
        'lady': {'path': country_path, 'link': 'https://youtu.be/0T1J8JuTtR8?si=Y9TsDAdCg8Zzzqes', 'artist': 'Kenny Rogers', 'real_name': 'Lady'},
        'fire': {'path': country_path, 'link': 'https://youtu.be/5WyLhwYFgmk?si=oJLs0W7uG-7rfJHk', 'artist': 'Johnny Cash', 'real_name': 'Ring of Fire'},
        'yourman': {'path': country_path, 'link': 'https://youtu.be/nADTbWQof7Y?si=ftGjVtVFYQgCGlfd', 'artist': 'Josh Turner', 'real_name': 'Your Man'},
        'blue': {'path': country_path, 'link': 'https://youtu.be/JqLU-Ow66_c?si=IkjOt2s3TIHx8Ubp', 'artist': 'Johnny Cash', 'real_name': 'Folsom Prison Blues'},
        'cowboys': {'path': country_path, 'link': 'https://youtu.be/Ufjv0SRZ-IY?si=879VmcSANBx5191Y', 'artist': 'Willie Nelson', 'real_name': "Mammas Don't Let Your Babies Grow up to Be Cowboys"},
        '9to5': {'path': country_path, 'link': 'https://youtu.be/UbxUSsFXYo4?si=fFVJP4EzcrbBH7CW', 'artist': 'Dolly Parton', 'real_name': '9 To 5'},

        'twist': {'path': metal_path, 'link': 'https://youtu.be/TcePkwagNFA?si=P4bajzJKLiXXOTak', 'artist': 'Korn', 'real_name': 'Twist'},
        'trooper': {'path': metal_path, 'link': 'https://youtu.be/ZsVFwCLMwPg?si=s6snp1f1KfLLB0uk', 'artist': 'Iron Maiden', 'real_name': 'The Trooper'},
        'warpigs': {'path': metal_path, 'link': 'https://youtu.be/bYgpv5clf3Y?si=Kp5RECgyfQxjI0nl', 'artist': 'Black Sabbath', 'real_name': 'War Pigs'},
        'fireandflames': {'path': metal_path, 'link': 'https://youtu.be/0jgrCKhxE1s?si=yr60jNL2igeeRakD', 'artist': 'DragonForce', 'real_name': 'Through the Fire and Flames'},
        'blind': {'path': metal_path, 'link': 'https://youtu.be/x81SMw8qUh0?si=OoqnqGljGKhJhN7a', 'artist': 'Korn', 'real_name': 'Blind'},
        'chopsuey': {'path': metal_path, 'link': 'https://youtu.be/CSvFpBOe8eY?si=fYl62dp0hkYx9whq', 'artist': 'System Of A Down', 'real_name': 'Chop Suey!'},
        'icarus': {'path': metal_path, 'link': 'https://youtu.be/p4w2BZXL6Ss?si=r3OHU8xeTszzNNCm', 'artist': 'Iron Maiden', 'real_name': 'Flight Of Icarus'},
        'masterpiece': {'path': metal_path, 'link': 'https://youtu.be/rbFaVDfkI00?si=iujbsRDI_rQvPa0o', 'artist': 'Motionless in White', 'real_name': 'Masterpiece'},
        'belltolls': {'path': metal_path, 'link': 'https://youtu.be/0u_n7tNmmyU?si=T2gq6kFAtOuqCh2t', 'artist': 'Metallica', 'real_name': 'For Whom the Bell Tolls'},
        'barkatthemoon': {'path': metal_path, 'link': 'https://youtu.be/LplPi2CxNHI?si=27woBLwdEXUx4UVA', 'artist': 'Ozzy Osbourne', 'real_name': 'Bark at the Moon'},
        'breakinglaw': {'path': metal_path, 'link': 'https://youtu.be/L397TWLwrUU?si=tc1FQ2Y5-ZSwYynY', 'artist': 'Judas Priest', 'real_name': 'Breaking The Law'},
        'toxicity': {'path': metal_path, 'link': 'https://youtu.be/iywaBOMvYLI?si=_vT1dDXk6N6WZdx6', 'artist': 'System Of A Down', 'real_name': 'Toxicity'},
        'nomoretears': {'path': metal_path, 'link': 'https://youtu.be/CprfjfN5PRs?si=IfwYN7JOiP5ZdUvo', 'artist': 'Ozzy Osbourne', 'real_name': 'No More Tears'},

        'element': {'path': hip_hop_path, 'link': 'https://youtu.be/glaG64Ao7sM?si=1Ucs6PIfJNYC9QO9', 'artist': 'Kendrick Lamar', 'real_name': 'ELEMENT.'},
        'rosaparks': {'path': hip_hop_path, 'link': 'https://youtu.be/2g5q-aEINDw?si=X2QQdnhoZzyXHf2L', 'artist': 'Outkast', 'real_name': 'Rosa Parks'},
        'allthelights': {'path': hip_hop_path, 'link': 'https://youtu.be/w2Yh9sxfTd8?si=j0VMvxjy3sAMhYx6', 'artist': 'Kanye West', 'real_name': 'All Of The Lights'},
        'itwasagoodday': {'path': hip_hop_path, 'link': 'https://youtu.be/h4UqMyldS7Q?si=2dRaSQpF3DjQALxh', 'artist': 'Ice Cube', 'real_name': 'It Was A Good Day'},
        'loseyourself': {'path': hip_hop_path, 'link': 'https://youtu.be/tR1ECf4sEpw?si=4Iak5lgEpoTn-1W-', 'artist': 'Eminem', 'real_name': 'Lose Yourself'},
        'nextepisode': {'path': hip_hop_path, 'link': 'https://youtu.be/BqZvXIFM1T4?si=PZlCRJlqpI3xtOqp', 'artist': 'Dr.Dre', 'real_name': 'The Next Episode'},
        'stilldre': {'path': hip_hop_path, 'link': 'https://youtu.be/KDK5j-pd8tQ?si=jeiN03Xe4w2IlO4q', 'artist': 'Dr.Dre', 'real_name': 'Still D.R.E.'},        
        'forgotdre': {'path': hip_hop_path, 'link': 'https://youtu.be/x9Jf4349pmU?si=pdaictEz4Q_4Kxfu', 'artist': 'Dr.Dre', 'real_name': 'Forgot About Dre'},
        'uptownfunk': {'path': hip_hop_path, 'link': 'https://youtu.be/5JtL8b2t1EQ?si=zjP7D5iLR7sH7QGB', 'artist': 'Mark Ronson', 'real_name': 'Uptown Funk'},
        'juicy': {'path': hip_hop_path, 'link': 'https://youtu.be/_JZom_gVfuw?si=0nfts6LN2yGouptr', 'artist': 'The Notorious B.I.G.', 'real_name': 'Juicy'},
        'hypnotize': {'path': hip_hop_path, 'link': 'https://youtu.be/H9NuWEeODew?si=C0FHQDO8U3iNqojQ', 'artist': 'The Notorious B.I.G.', 'real_name': 'Hypnotize'},
        'myband': {'path': hip_hop_path, 'link': 'https://youtu.be/6R7kAqvz6z8?si=kCd_EnI38QILe7ZR', 'artist': 'D12', 'real_name': 'My Band'},
        'rapgod': {'path': hip_hop_path, 'link': 'https://youtu.be/xgT7QhUq6sQ?si=xB-EJglt3QM2-SDk', 'artist': 'Eminem', 'real_name': 'Rap God'},
        'godzilla': {'path': hip_hop_path, 'link': 'https://youtu.be/SmBzqkgdH9I?si=B-icYGHhsO0cK-47', 'artist': 'Eminem', 'real_name': 'Godzilla'},
        'billiejean': {'path': hip_hop_path, 'link': 'https://youtu.be/DKFS2tDsZRY?si=uUrBfgVjquPY5olY', 'artist': 'Micheal Jackson', 'real_name': 'Billie Jean'},
        

        'saveyourtears': {'path': pop_path, 'link': 'https://youtu.be/XXYlFuWEuKI?si=Ypl87vCCeRlWQALV', 'artist': 'The Weeknd', 'real_name': 'Save Your Tears'},
        'planet': {'path': pop_path, 'link': 'https://youtu.be/9_Ng6II36ec?si=QXKODy-BGwhQwhgu', 'artist': 'Aidan Bissett', 'real_name': 'Planet'},
        'someoneyouloved': {'path': pop_path, 'link': 'https://youtu.be/zABLecsR5UE?si=zFSRsLC2OS4z6uUr', 'artist': 'Lewis Capaldi', 'real_name': 'Someone You Loved'},
        'beautifulthings': {'path': pop_path, 'link': 'https://youtu.be/Oa_RSwwpPaA?si=nZ62EtlpHoaE6dxI', 'artist': 'Benson Boone', 'real_name': 'Beautiful Things'},
        'shapeofyou': {'path': pop_path, 'link': 'https://youtu.be/JGwWNGJdvx8?si=cVrK9u63wrG5APBJ', 'artist': 'Ed Sheeran', 'real_name': 'Shape of You'},
        'clocks': {'path': pop_path, 'link': 'https://youtu.be/d020hcWA_Wg?si=D-7dBRPgmgSX61P-', 'artist': 'Coldplay', 'real_name': 'Clocks'},        
        'rollingdeep': {'path': pop_path, 'link': 'https://youtu.be/rYEDA3JcQqw?si=vlywp9Tw5o2WaaJe', 'artist': 'Adele', 'real_name': 'Rolling in the Deep'},
        'scientist': {'path': pop_path, 'link': 'https://youtu.be/RB-RcX5DS5A?si=wT7xsdw81fJ4KbtI', 'artist': 'Coldplay', 'real_name': 'The Scientist'},
        'vivaladvida': {'path': pop_path, 'link': 'https://youtu.be/dvgZkm1xWPE?si=UkNdqdBqunce7Co7', 'artist': 'Coldplay', 'real_name': 'Viva La Vida'},
        'perfect': {'path': pop_path, 'link': 'https://youtu.be/2Vv-BfVoq4g?si=pGbDrvdvQ5XI6Cnf', 'artist': 'Ed Sheeran', 'real_name': 'Perfect'},
        'sugar': {'path': pop_path, 'link': 'https://youtu.be/09R8_2nJtjg?si=8pzUn7h41pU0mHqU', 'artist': 'Maroon 5', 'real_name': 'Sugar'},
        'flowers': {'path': pop_path, 'link': 'https://youtu.be/G7KNmW9a75Y?si=X45ilVtMHjeZTByf', 'artist': 'Miley Cyrus', 'real_name': 'Flowers'},
        'pokerface': {'path': pop_path, 'link': 'https://youtu.be/bESGLojNYSo?si=Aba-GqMmjPNOMbsQ', 'artist': 'Lady Gaga', 'real_name': 'Poker Face'},
        'wedonttalk': {'path': pop_path, 'link': 'https://youtu.be/3AtDnEC4zak?si=Cx4pIu7weEbsDBC4', 'artist': 'Charlie Puth', 'real_name': "We Don't Talk Anymore"},
        'asitwas': {'path': pop_path, 'link': 'https://youtu.be/H5v3kku4y6Q?si=Zkw2WbFU9B_jKAqW', 'artist': 'Harry Styles', 'real_name': 'As It Was'},

        'numb': {'path': rock_path, 'link': 'https://youtu.be/kXYiU_JCYtU?si=sSrpwYptS8KFJc8z', 'artist': 'Linkin Park', 'real_name': 'Numb'},
        'novemberrain': {'path': rock_path, 'link': 'https://youtu.be/8SbUC-UaAxE?si=DUB77qOTPCBVzu9X', 'artist': "Guns N' Roses", 'real_name': 'November Rain'},
        'smellsliketeen': {'path': rock_path, 'link': 'https://youtu.be/hTWKbfoikeg?si=BbnFRuOBmLUweXRh', 'artist': 'Nirvana', 'real_name': 'Smells Like Teen Spirit'},
        'bohrapsody': {'path': rock_path, 'link': 'https://youtu.be/fJ9rUzIMcZQ?si=89T9QTe0kQufFrdd', 'artist': 'Queen', 'real_name': 'Bohemian Rhapsody'},
        'intheend': {'path': rock_path, 'link': 'https://youtu.be/eVTXPUF4Oz4?si=C7_EzVfPNhMy9HuT', 'artist': 'Linkin Park', 'real_name': 'In The End'},
        'sweetchild': {'path': rock_path, 'link': 'https://youtu.be/1w7OgIMMRc4?si=8AOL2_R0_irD_FP1', 'artist': "Guns N' Roses", 'real_name': "Sweet Child O' Mine"},
        'doiwannaknow': {'path': rock_path, 'link': 'https://youtu.be/bpOSxM0rNPM?si=Vx2eRaBdefP7IYAJ', 'artist': 'Artic Monkeys', 'real_name': 'Do I Wanna Know?'},        
        'thunderstruck': {'path': rock_path, 'link': 'https://youtu.be/v2AC41dglnM?si=kVAUY-Bwj0PkxudB', 'artist': 'AC/DC', 'real_name': 'Thunderstruck'},
        'itsmylife': {'path': rock_path, 'link': 'https://youtu.be/vx2u5uUu3DE?si=2b71gUifbslDPcn0', 'artist': 'Bon Jovi', 'real_name': "It's My Life"},
        'nothingelsematters': {'path': rock_path, 'link': 'https://youtu.be/HyrWd_gfQNQ?si=_PnsVd9kDvsY3ZaI', 'artist': 'Metallica', 'real_name': 'Nothing Else Matters'},
        'everybreath': {'path': rock_path, 'link': 'https://youtu.be/OMOGaugKpzs?si=u7TsCuKwZsLzTVUD', 'artist': 'The Police', 'real_name': 'Every Breath You Take'},
        'losingmyreligion': {'path': rock_path, 'link': 'https://youtu.be/xwtdhWltSIg?si=SFJz22Ct1V8Qfezh', 'artist': 'R.E.M.', 'real_name': 'Losing My Religion'},
        'likeastone': {'path': rock_path, 'link': 'https://youtu.be/7QU1nvuxaMA?si=PZsUIXmY-MX-oooI', 'artist': 'Audioslave', 'real_name': 'Like a Stone'},
        'livinonaprayer': {'path': rock_path, 'link': 'https://youtu.be/lDK9QqIzhwk?si=1dkXNYpsXQrA_Ec-', 'artist': 'Bon Jovi', 'real_name': "Livin' On A Prayer"},
        'californication': {'path': rock_path, 'link': 'https://youtu.be/sqLWfFCbYBI?si=JYQCIVOGw15GOO11', 'artist': 'Red Hot Chili Peppers', 'real_name': 'Californication'},
        

    }

def get_genre(path):
    country_path, metal_path, hip_hop_path, rock_path, pop_path = paths()
    return {country_path: "country",
            metal_path: "metal",
            hip_hop_path: "hiphop",
            pop_path: "jazz",
            pop_path : "pop",
            rock_path: "rock"}[path]

def paths():
    path = sys.argv[0]
    head,tail = os.path.split(path)
    headTwo,tail = os.path.split(head)
    headThree,tail = os.path.split(headTwo)
    country_path = os.path.join(headTwo, "data", "country_genre")
    metal_path   = os.path.join(headTwo, "data", "heavy_metal")
    hip_hop_path = os.path.join(headTwo, "data", "hip_hop_genre")
    pop_path = os.path.join(headTwo, "data", "pop_genre")
    rock_path = os.path.join(headTwo, "data", "rock_genre")
    return country_path, metal_path, hip_hop_path, pop_path, rock_path