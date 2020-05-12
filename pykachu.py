import shutil
import urllib
import requests
import os
import imghdr

dex = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Charizard-MegaX',
       'Charizard-MegaY', 'Squirtle', 'Wartortle',
       'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto',
       'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew',
       'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidoran', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable',
       'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume',
       'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck',
       'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra',
       'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool',
       'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite',
       'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster',
       'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode',
       'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing',
       'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu',
       'Starmie', 'Mr.', 'Mr.', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp',
       'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar',
       'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair',
       'Dragonite', 'Mewtwo', 'Mew', 'Generation', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava',
       'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba',
       'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi',
       'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo',
       'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire',
       'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown-A', 'Unown-B', 'Unown-C',
       'Unown-D', 'Unown-E', 'Unown-F', 'Unown-G', 'Unown-H', 'Unown-I', 'Unown-J', 'Unown-K',
       'Unown-L', 'Unown-M', 'Unown-N', 'Unown-O', 'Unown-P', 'Unown-Q',
       'Unown-R', 'Unown-S', 'Unown-T', 'Unown-U', 'Unown-V', 'Unown-W',
       'Unown-X', 'Unown-Y', 'Unown-Z', 'Unown-qm', 'Unown-em', 'Wobbuffet', 'Girafarig', 'Pineco',
       'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle',
       'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola',
       'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy',
       'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby',
       'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-oh',
       'Celebi', 'Generation', 'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip',
       'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly',
       'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow',
       'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom',
       'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud',
       'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon',
       'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise',
       'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal',
       'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria',
       'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy',
       'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Castform-Rainy',
       'Castform-Snowy', 'Castform-Sunny', 'Kecleon', 'Shuppet',
       'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal',
       'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon',
       'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios',
       'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys-Normal', 'Deoxys-Attack', 'Deoxys-Speed', 'Deoxys-Defense',
       'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly',
       'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew',
       'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy-Plant', 'Burmy-Trash',
       'Burmy-Sandy', 'Wormadam-Plant', 'Wormadam-Sandy', 'Wormadam-Trash', 'Mothim', 'Combee',
       'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim-Sunshine', 'Cherrim-Overcast',
       'Shellos-West', 'Shellos-East', 'Gastrodon-West', 'Gastrodon-East', 'Ambipom',
       'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling',
       'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime', 'Mime', 'Happiny', 'Chatot', 'Spiritomb',
       'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi',
       'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow',
       'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss',
       'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir',
       'Froslass', 'Rotom', 'Rotom-Fan', 'Rotom-Heat', 'Rotom-Frost', 'Rotom-Mow', 'Rotom-Wash',
       'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina-Altered', 'Giratina-Origin',
       'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin-Land', 'Shaymin-Sky', 'Arceus-Normal', 'Arceus-Bug',
       'Arceus-Dark', 'Arceus-Dragon', 'Arceus-Electric', 'Arceus-Fighting', 'Arceus-Fire', 'Arceus-Flying',
       'Arceus-Ghost', 'Arceus-Grass', 'Arceus-Ground', 'Arceus-Ice', 'Arceus-Poison', 'Arceus-Psychic',
       'Arceus-Rock', 'Arceus-Steel', 'Arceus-Water',
       'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott',
       'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage',
       'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant',
       'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill',
       'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk',
       'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott',
       'Petilil', 'Lilligant', 'Basculin-Red-Striped', 'Basculin-Blue-Striped', 'Sandile', 'Krokorok', 'Krookodile',
       'Darumaka', 'Darmanitan-Standard-Mode', 'Darmanitan-Zen-Mode',
       'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus',
       'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino',
       'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna',
       'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling-Spring', 'Deerling-Autumn', 'Deerling-Summer',
       'Deerling-Winter', 'Sawsbuck-Spring', 'Sawsbuck-Autumn', 'Sawsbuck-Summer', 'Sawsbuck-Winter',
       'Emolga', 'Karrablast', 'Escavalier',
       'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed',
       'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem',
       'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal',
       'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard',
       'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino',
       'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus',
       'Tornadus-Incarnate', 'Tornadus-Therian', 'Thundurus-Incarnate', 'Thundurus-Therian', 'Reshiram', 'Zekrom',
       'Landorus-Incarnate', 'Landorus-Therian', 'Kyurem', 'Kyurem-White', 'Kyurem-Black', 'Keldeo', 'Keldeo-Resolute',
       'Meloetta-Aria', 'Meloetta-Pirouette', 'Genesect', 'Genesect-Burn', 'Genesect-Chill', 'Genesect-Shock',
       'Genesect-Douse']

poke_err = {}
if os.path.isfile("./sprites/pokemon/log.txt"):
    with open("./sprites/pokemon/log.txt") as file:
        data = file.read().split('\n')
        for poke in data:
            poke_err[poke] = True


def download_img(name, url):
    if os.path.isfile("sprites/pokemon/" + name + ".gif"):
        print("pykachu: already downloaded resource: ", name)
        return
    if url in poke_err:
        print("pykachu: image was not found in source url before. -- skipped")
        return
    flag = False
    with open("sprites/pokemon/" + name + ".gif", 'wb') as handle:
        print("downloading: " + name)
        response = requests.get(url, stream=True)

        if not response.ok:
            flag = True
            print("error: ", url)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    if flag:
        try:
            os.remove("sprites/pokemon/" + name + ".gif")
            with open("./sprites/pokemon/log.txt", "a") as file:
                file.write(url + "\n")
        except:
            pass


def create_dirs():
    if not os.path.isdir("./sprites"):
        os.mkdir("./sprites")
    if os.path.isdir("./sprites/pokemon"):
        shutil.rmtree("./sprites/pokemon")
    os.mkdir("./sprites/pokemon")
    os.mkdir("./sprites/pokemon/normal")
    os.mkdir("./sprites/pokemon/back-normal")
    os.mkdir("./sprites/pokemon/shiny")
    os.mkdir("./sprites/pokemon/back-shiny")


def fetch_gb_sprite(pokemon):
    base_url = 'https://img.pokemondb.net/sprites/black-white/anim/'
    download_img("normal/" + pokemon.lower(), base_url + "normal/" + pokemon.lower() + ".gif")
    download_img("shiny/" + pokemon.lower(), base_url + "shiny/" + pokemon.lower() + ".gif")
    download_img("back-normal/" + pokemon.lower(), base_url + "back-normal/" + pokemon.lower() + ".gif")
    download_img("back-shiny/" + pokemon.lower(), base_url + "back-shiny/" + pokemon.lower() + ".gif")
    download_img("normal/" + pokemon.lower() + "-f", base_url + "normal/" + pokemon.lower() + "-f.gif")
    download_img("shiny/" + pokemon.lower() + "-f", base_url + "shiny/" + pokemon.lower() + "-f.gif")
    download_img("back-normal/" + pokemon.lower() + "-f",
                 base_url + "back-normal/" + pokemon.lower() + "-f.gif")
    download_img("back-shiny/" + pokemon.lower() + "-f", base_url + "back-shiny/" + pokemon.lower() + "-f.gif")

    base_url = 'https://img.pokemondb.net/sprites/black-white-2/anim/'
    download_img("normal/" + pokemon.lower(), base_url + "normal/" + pokemon.lower() + ".gif")
    download_img("shiny/" + pokemon.lower(), base_url + "shiny/" + pokemon.lower() + ".gif")
    download_img("back-normal/" + pokemon.lower(), base_url + "back-normal/" + pokemon.lower() + ".gif")
    download_img("back-shiny/" + pokemon.lower(), base_url + "back-shiny/" + pokemon.lower() + ".gif")
    download_img("normal/" + pokemon.lower() + "-f", base_url + "normal/" + pokemon.lower() + "-f.gif")
    download_img("shiny/" + pokemon.lower() + "-f", base_url + "shiny/" + pokemon.lower() + "-f.gif")
    download_img("back-normal/" + pokemon.lower() + "-f",
                 base_url + "back-normal/" + pokemon.lower() + "-f.gif")
    download_img("back-shiny/" + pokemon.lower() + "-f", base_url + "back-shiny/" + pokemon.lower() + "-f.gif")


def fetch_nds_sprite(pokemon):
    # download normal and shiny sprites.
    base_url = 'https://projectpokemon.org/images/'
    download_img("normal/" + pokemon.lower(), base_url + "normal-sprite/" + pokemon.lower() + ".gif")
    download_img("shiny/" + pokemon.lower(), base_url + "shiny-sprite/" + pokemon.lower() + ".gif")

    download_img("normal/" + pokemon.lower() + "-f", base_url + "normal-sprite/" + pokemon.lower() + "_f.gif")
    download_img("shiny/" + pokemon.lower() + "-f", base_url + "shiny-sprite/" + pokemon.lower() + "_f.gif")

    if not os.path.isfile("./sprites/pokemon/" + "normal/" + pokemon.lower() + ".gif"):
        download_img("normal/" + pokemon.lower(), base_url + "normal-sprite/" + pokemon.lower() + "_m.gif")
    if not os.path.isfile("./sprites/pokemon/" + "shiny/" + pokemon.lower() + ".gif"):
        download_img("shiny/" + pokemon.lower(), base_url + "shiny-sprite/" + pokemon.lower() + "_m.gif")

    download_img("normal/" + pokemon.lower() + "-mega", base_url + "normal-sprite/" + pokemon.lower() + "-mega.gif")
    download_img("shiny/" + pokemon.lower() + "-mega", base_url + "shiny-sprite/" + pokemon.lower() + "-mega.gif")

    # download back-normal and back-shiny sprites
    base_url = 'https://projectpokemon.org/images/sprites-models/'
    download_img("back-normal/" + pokemon.lower(), base_url + "normal-back/" + pokemon.lower() + ".gif")
    download_img("back-shiny/" + pokemon.lower(), base_url + "shiny-back/" + pokemon.lower() + ".gif")

    download_img("back-normal/" + pokemon.lower() + "-f", base_url + "normal-back/" + pokemon.lower() + "_f.gif")
    download_img("back-shiny/" + pokemon.lower() + "-f", base_url + "shiny-back/" + pokemon.lower() + "_f.gif")

    if not os.path.isfile("./sprites/pokemon/" + "back-normal/" + pokemon.lower() + ".gif"):
        download_img("back-normal/" + pokemon.lower(), base_url + "normal-back/" + pokemon.lower() + "_m.gif")
    if not os.path.isfile("./sprites/pokemon/" + "back-shiny/" + pokemon.lower() + ".gif"):
        download_img("back-shiny/" + pokemon.lower(), base_url + "shiny-back/" + pokemon.lower() + "_m.gif")

    download_img("back-normal/" + pokemon.lower() + "-mega", base_url + "normal-back/" + pokemon.lower() + "-mega.gif")
    download_img("back-shiny/" + pokemon.lower() + "-mega", base_url + "shiny-back/" + pokemon.lower() + "-mega.gif")


def rm_corrupt_gifs():
    for subdir, dirs, files in os.walk('./sprites/pokemon'):
        for filename in files:
            if filename == "log.txt":
                continue
            filepath = subdir + "/" + filename
            if imghdr.what(filepath) != "gif":
                print("pykachu: removing corrupt gif: ", filepath)
                os.remove(filepath)


if __name__ == '__main__':
    if not os.path.isdir("./sprites"):
        create_dirs()

    option = input('Do you want to reset the downloaded sprites (y/n)?')
    if option.lower() == 'y':
        create_dirs()

    option = input('Do you want to download NDS sprites or GB sprites? (n for nds, g for gb sprites)').lower()

    rm_corrupt_gifs()

    for pokemon in dex:
        try:
            if option == 'n':
                fetch_nds_sprite(pokemon)
            elif option == 'g':
                fetch_gb_sprite(pokemon)

        except:
            print("error occured while fetching resource group for: ", pokemon.lower())
