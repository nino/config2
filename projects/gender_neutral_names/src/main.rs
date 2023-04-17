use rand::seq::SliceRandom;

fn main() {
    let names = vec![
        "Casey",
        "Riley",
        "Jessie",
        "Jackie",
        "Avery",
        "Jaime",
        "Peyton",
        "Kerry",
        "Jody",
        "Kendall",
        "Payton",
        "Skyler",
        "Frankie",
        "Pat",
        "Quinn",
        "Harley",
        "Reese",
        "Robbie",
        "Tommie",
        "Justice",
        "Kris",
        "Carey",
        "Emerson",
        "Blair",
        "Amari",
        "Elisha",
        "Sage",
        "Emery",
        "Stevie",
        "Rowan",
        "Ollie",
        "Shea",
        "Jaylin",
        "Phoenix",
        "Charley",
        "Armani",
        "Devyn",
        "Ivory",
        "Kendal",
        "Baby",
        "Mckinley",
        "Finley",
        "Milan",
        "Tory",
        "Shay",
        "Shiloh",
        "Lavern",
        "Sky",
        "Reilly",
        "Leighton",
        "Santana",
        "Arden",
        "Campbell",
        "Channing",
        "Kamari",
        "Alva",
        "Clair",
        "Lavon",
        "Kenyatta",
        "Britt",
        "Vernell",
        "Michal",
        "Austyn",
        "Rian",
        "Dominque",
        "Remy",
        "Jammie",
        "Ricki",
        "Jordin",
        "Trinidad",
        "Ryley",
        "Carrol",
        "Landry",
        "Lorin",
        "Yael",
        "Codi",
        "Sloan",
        "Jael",
        "Kodi",
        "Azariah",
        "Dakotah",
        "Lorenza",
        "Artie",
        "Maxie",
        "Torey",
        "Tai",
        "Kalani",
        "Codie",
        "Storm",
        "Jaedyn",
        "Merritt",
        "Allyn",
        "Jourdan",
        "Yuri",
        "Ellery",
        "Oakley",
        "Gentry",
        "Ellison",
        "Arin",
        "Sol",
        "Carrington",
        "Dell",
        "Carlin",
        "Lennie",
        "Dru",
        "Alpha",
        "Kiran",
        "Tristyn",
        "Camdyn",
        "Krishna",
        "Demetrice",
        "Berkley",
        "Linden",
        "Mikah",
        "Parris",
        "Kalin",
        "Kary",
        "Arie",
        "Aries",
        "Rio",
        "Sutton",
        "Rhyan",
        "Isa",
        "Arlyn",
        "Karsen",
        "Seneca",
        "Callan",
        "Garnett",
        "Micaiah",
        "Christan",
        "Aris",
        "Tylar",
        "Brighton",
        "Merlyn",
        "Kimani",
        "Salem",
        "Barrie",
        "Braylin",
        "Charly",
        "Ocean",
        "Ara",
        "Deane",
        "Andree",
        "Natividad",
        "Ardell",
        "Divine",
        "Ocie",
        "Lakota",
        "Ashtin",
        "Larkin",
        "Kamdyn",
        "Waverly",
        "Claudie",
        "Lannie",
        "Vernie",
        "Adair",
        "Kaidyn",
        "Verdell",
        "Jae",
        "Aven",
        "Kodie",
        "Shalom",
        "Daylin",
        "Osiris",
        "Dwan",
        "Lashaun",
        "Ashten",
        "Dann",
        "Shai",
        "Teegan",
        "Micha",
        "Tobie",
        "Jaelin",
        "Marlowe",
        "Kareen",
        "Ryen",
        "Marquette",
        "Joell",
        "Adel",
        "Golden",
        "An",
        "Ossie",
        "Stephane",
        "Vinnie",
        "Armoni",
        "Berlin",
        "Thanh",
        "Jimi",
        "Linn",
        "Marvis",
        "Tam",
        "Kaylon",
        "Kylin",
        "Lajuan",
        "Cameran",
        "Shamari",
        "Teddie",
        "Laramie",
        "Ricci",
        "Jule",
        "Cedar",
        "Drue",
        "Shade",
        "Jeryl",
        "Taylen",
        "Devonne",
        "Delane",
        "Arnell",
        "Earlie",
        "Tenzin",
        "Kendel",
        "Arlis",
        "Ashby",
        "Shia",
        "Berkeley",
        "Lin",
        "Freedom",
        "Rylin",
        "Aaryn",
        "Mykah",
        "Shaya",
        "Tanis",
        "Chancey",
        "Jaidan",
        "Jaydyn",
        "Kaedyn",
        "Talyn",
        "Le",
        "Hartley",
        "Avon",
        "Finnley",
        "Schyler",
        "Rennie",
        "Aly",
        "Kaydin",
        "Camari",
        "Clemmie",
        "Payson",
        "Anay",
        "Devine",
        "Terryl",
        "Bao",
        "Tru",
        "Indiana",
        "Evyn",
        "Deniz",
        "Emari",
        "Davi",
        "True",
        "De",
        "Samar",
        "Kriston",
        "Lian",
        "Brittan",
        "Torre",
        "Shawne",
        "Kailen",
        "Aundra",
        "Halen",
        "Yuki",
        "Marshell",
        "Rivers",
        "Jaziah",
        "Amaree",
        "Mycah",
        "Toy",
        "Tien",
        "Adi",
        "Callahan",
        "Jazz",
        "Reign",
        "Burnice",
        "Jamy",
        "Lavaughn",
        "Adrean",
        "Cache",
        "Britain",
        "Dalyn",
        "Dondi",
        "Dallis",
        "Nazareth",
        "Nieves",
        "Jireh",
        "Collen",
        "Onyx",
        "Raynell",
        "Sonnie",
        "Lyrik",
        "Marice",
        "Lexington",
        "Chi",
        "Eliyah",
        "Tonnie",
        "Teagen",
        "Rudi",
        "Kamani",
        "Han",
        "Jerre",
        "Alika",
        "Monta",
        "Jaydn",
        "Hadyn",
        "Kem",
        "Terrin",
        "Wisdom",
        "Natale",
        "Rossie",
        "Lugene",
        "Rebel",
        "Blayke",
        "Donyell",
        "Myrl",
        "Kaelen",
        "Miko",
        "Elza",
        "Kriss",
        "Shadow",
        "Raylen",
        "Ramey",
        "Jaryn",
        "Laren",
        "Leverne",
        "Khali",
        "Reiley",
        "Jaydee",
        "Luan",
        "Reily",
        "Caidyn",
        "Kaylor",
        "Juel",
        "Amrit",
        "Rayn",
        "Arien",
        "Britten",
        "Bela",
        "Arliss",
        "Aziah",
        "Lonie",
        "Pasha",
        "Caylen",
        "Talin",
        "Shaune",
        "Valen",
        "Ozie",
        "Dung",
        "Avry",
        "Zamari",
        "Kam",
        "Ronit",
        "Kelin",
        "Teigan",
        "Sun",
        "Karlin",
        "Lenell",
        "Jaleen",
        "Amory",
        "Loghan",
        "Kemani",
        "Aarin",
        "Elizah",
        "Maysen",
        "Yu",
        "Bergen",
        "Jalani",
        "Jamille",
        "Adama",
        "Laray",
        "Sully",
        "Latrelle",
        "Onnie",
        "Khanh",
        "Amil",
        "Braylyn",
        "Tanay",
        "Kailan",
        "Caelin",
        "Alexandr",
        "Daryan",
        "Wallis",
        "Kelechi",
        "Javonne",
        "Gean",
        "Kao",
        "Cypress",
        "Tamari",
        "Evann",
        "Tarren",
        "Jeffie",
        "Amel",
        "Jaspreet",
        "Amen",
        "Neema",
        "Hien",
        "Lorren",
        "Jonel",
        "Kelyn",
        "Jodeci",
        "Alexy",
        "Jayln",
        "Chayanne",
        "Brittain",
        "Selby",
        "Akili",
        "Kimari",
        "Anmol",
        "Kirin",
        "Min",
        "Eri",
        "Bralyn",
        "Alyn",
        "Osie",
        "Shiva",
        "Kamerin",
        "Pheonix",
        "Abrar",
        "Darnelle",
        "Haydin",
        "Davonne",
        "Makana",
        "Ayomide",
        "Daine",
        "Avrey",
        "Truth",
        "Uchenna",
        "Gracin",
        "Chong",
        "Marrion",
        "Atley",
        "Luverne",
        "Lunden",
        "Manpreet",
        "Kodee",
        "Kyri",
        "Donnelle",
        "Koree",
        "Riyan",
        "Sagan",
        "Teran",
        "Avory",
        "Lior",
        "Hoa",
        "Alexx",
        "Arleigh",
        "Brier",
        "Lyndall",
        "Terin",
        "Kallan",
        "Maika",
        "Trayce",
        "Deavion",
        "Indy",
        "Ellington",
        "Feliz",
        "Alexiz",
        "Neftaly",
        "Kaegan",
        "Edris",
        "Harpreet",
        "Jailin",
        "Mackinley",
        "Kendle",
        "Donyae",
        "Koi",
        "Eastyn",
        "Vertis",
        "Shady",
        "Shondell",
        "Monti",
        "Ardie",
        "Londen",
        "Kayde",
        "Gabryel",
        "Chai",
        "Gurpreet",
        "Tomie",
        "Corley",
        "Mishael",
        "Shalin",
        "Shann",
        "Lyndal",
        "Jamani",
        "Chee",
        "Deshay",
        "Devlyn",
        "Royale",
        "Jaidin",
        "Dayan",
        "Jari",
        "Amarii",
        "Dilyn",
        "Yuval",
        "Toryn",
        "Rajah",
        "Tatem",
        "Chidera",
        "Amarri",
        "Rielly",
        "Bobie",
        "Miciah",
        "Shaden",
        "Codee",
        "Ottie",
        "Haydyn",
        "Ary",
        "Tajae",
        "Aki",
        "Haedyn",
        "Jasiyah",
        "Averey",
        "Hyun",
        "Jamile",
        "Yona",
        "Yee",
        "Evian",
        "Amandeep",
        "Vandy",
        "Trenell",
        "Rei",
        "Weslie",
        "Ariyan",
        "Kemoni",
        "Rossi",
        "Danel",
        "Mandeep",
        "Ji",
        "Ying",
        "Kijana",
        "Embry",
        "Braelin",
        "Ja",
        "Shawndell",
        "Ronie",
        "Jamisen",
        "Makell",
        "Amori",
        "Nuri",
        "Caylan",
        "Tennessee",
        "Linell",
        "Giani",
        "Rudell",
        "Germany",
        "Johari",
        "Lorrin",
        "Lenzie",
        "Carle",
        "Cayle",
        "Bay",
        "Ova",
        "Cailen",
        "Rhylan",
        "Zaylin",
        "Romelle",
        "Brownie",
        "Grier",
        "Vondell",
        "Dannell",
        "Aquarius",
        "Lavoris",
        "Phenix",
        "Keylen",
        "Cristan",
        "Daylyn",
        "Riely",
        "Rogue",
        "Karem",
        "Olamide",
        "Dawsyn",
        "Halsey",
        "Samie",
        "Matisse",
        "Dail",
        "Oluwaseun",
        "Emanuelle",
        "Harlyn",
        "Lamari",
        "Schylar",
        "Kamori",
        "Kaydyn",
        "Kimoni",
        "Tian",
        "Alvia",
        "Skylan",
        "Ajai",
        "Tyjae",
        "Mc",
        "Chae",
        "Climmie",
        "Kymari",
        "Brittin",
        "Maven",
        "Cheney",
        "Jaz",
        "Malone",
        "Rashi",
        "Puneet",
        "Juda",
        "Rane",
        "Dezi",
        "Skiler",
        "Elya",
        "Rieley",
        "Tajai",
        "Da",
        "Deshannon",
        "Logyn",
        "Wrigley",
        "Happy",
        "Cyncere",
        "Callaway",
        "Shell",
        "Fontaine",
        "Jung",
        "Dossie",
        "Mayan",
        "Odean",
        "Baylin",
        "Austine",
        "Cagney",
        "Scotland",
        "Cire",
        "Harvest",
        "Bless",
        "Vegas",
        "Rael",
        "Mahari",
        "Perris",
        "Reilley",
        "Taygen",
        "Shey",
        "Oluwatosin",
        "Jemiah",
        "Oluwadamilola",
        "Markelle",
        "Gianny",
        "Jlyn",
        "Jeris",
        "Jaki",
        "Raymie",
        "Aldean",
        "Gal",
        "Hudsyn",
        "Deone",
        "Deundra",
        "Nasiah",
        "Donyea",
        "Shyler",
        "Mattia",
        "Navdeep",
        "Rameen",
        "Wai",
        "Eh",
        "Paxtyn",
        "Shaylon",
        "Kamoni",
        "Jadis",
        "Avyn",
        "Kitt",
        "Ebbie",
        "Amadi",
        "Clary",
        "Nakota",
        "Jacquese",
        "Gurnoor",
        "Brylin",
        "Kippy",
        "Sevyn",
        "Oluwaseyi",
        "Blaike",
        "Tagen",
        "Taite",
        "Dorsie",
        "Jolly",
        "Yi",
        "Dustine",
        "Brae",
        "Almer",
        "Zaelyn",
        "Hero",
        "Brennyn",
        "Coren",
        "Sher",
        "Geral",
        "Aalijah",
        "Yanis",
        "Rhythm",
        "Manjot",
        "Airen",
        "Giavonni",
        "Xan",
        "Tahjae",
        "Skyeler",
        "Kmari",
        "Taje",
        "Elis",
        "Temiloluwa",
        "Reise",
        "Oriel",
        "Kamarri",
        "Romey",
        "Maciah",
        "Jerris",
        "Meko",
        "Aimar",
        "Kehinde",
        "Ashtan",
        "Oreoluwa",
        "Kairee",
        "Leotha",
        "Jaylenn",
        "Celester",
        "Zekiah",
        "Tarrin",
        "Jerzy",
        "Nike",
        "Domnique",
        "Maitland",
        "Jaydence",
        "Kayton",
        "Jourdin",
        "Navjot",
        "Casy",
        "Staley",
        "Maxi",
        "Jamoni",
        "Jasmon",
        "Mell",
        "Ziyan",
        "Keatyn",
        "Jaree",
        "Day",
        "Posey",
        "Nemiah",
        "Lyrick",
        "Jahni",
        "Aijalon",
        "Oddie",
        "Zaide",
        "Shamell",
        "Cailan",
        "Zarin",
        "Keymani",
        "Preet",
        "Ekam",
        "Kayler",
        "Elim",
        "Jeryn",
        "Olanda",
        "Harbor",
        "Oluwanifemi",
        "Cledith",
        "Mishawn",
        "Dae",
        "Kenyatte",
        "Dai",
        "Mekiah",
        "Vernis",
        "Jianni",
        "Kamali",
        "Kellis",
        "Asheton",
        "Raedyn",
        "Yardley",
        "Donyel",
        "Zell",
        "Tyjai",
        "Eldean",
        "Donne",
        "Agam",
        "Myan",
        "Kele",
        "Skylen",
        "Shadee",
        "Connelly",
        "Harlo",
        "Arrin",
        "Quanta",
        "Caylor",
        "Gaylin",
        "Soua",
        "Darly",
        "Yoltzin",
        "Zohar",
        "Yarden",
        "Erian",
        "Jermany",
        "Currie",
        "Mechel",
        "Camauri",
        "Siah",
        "Lakoda",
        "Demarie",
        "Rumi",
        "Raeden",
        "Senai",
        "Kindred",
        "Deondrea",
        "Babe",
        "March",
        "Maddyx",
        "Jorryn",
        "Adisa",
        "Wen",
        "Audi",
        "Shaquel",
        "Michiah",
        "Chandlar",
        "Moe",
        "Arieon",
        "Yarnell",
        "Ayo",
        "Chey",
        "Clemence",
        "Ajene",
        "Tkai",
        "Lawan",
        "Zannie",
        "Denym",
        "Sayre",
        "Kamarii",
        "Tavi",
        "Kymoni",
        "Zaiah",
        "Amaurie",
        "Paiden",
        "Aamari",
        "Tris",
        "Rorey",
        "Meiko",
        "Asuncion",
        "Jodey",
        "Declyn",
        "Camil",
        "Oluwademilade",
        "Duanne",
        "Rudie",
        "Lauris",
        "Child",
        "Jaydeen",
        "Kery",
        "Nesta",
        "Merrit",
        "Ermal",
        "Kaisyn",
        "Neziah",
        "Lattie",
        "Nyaire",
        "Damarie",
        "Murle",
        "Sekai",
        "Merion",
        "Danyl",
        "Areon",
        "Seville",
        "Freddi",
        "Ruari",
        "Rayen",
        "Kadian",
        "Brookes",
        "Rilley",
        "Gaynor",
        "Sopheap",
        "Oluwatomisin",
        "Shayde",
        "Altair",
        "Jayel",
        "Foye",
        "Lovelle",
        "Jasmond",
        "Larin",
        "Malijah",
        "Brenn",
        "Maziah",
        "Chapel",
        "Linnell",
        "Tahje",
        "Peyson",
        "Jacquise",
        "Rease",
        "Breslin",
        "Remmy",
        "Sukhman",
        "Atari",
        "Shaquelle",
        "Brighten",
        "Jaton",
        "Jahdai",
        "Deovion",
        "Maui",
        "Ronne",
        "Sehaj",
        "Tagan",
        "Luvern",
        "Lyan",
        "Peniel",
        "Ryin",
        "Skylur",
        "Skylier",
        "Oluwadarasimi",
        "Psalm",
        "Aidynn",
        "Juliani",
        "Johany",
        "Rainn",
        "Liron",
        "Vail",
        "Gillie",
        "Armari",
        "Kache",
        "Eudell",
        "Mikele",
        "Alija",
        "Carel",
        "Olayinka",
        "Eaden",
        "Inioluwa",
        "Gwin",
        "Yacine",
        "Aeon",
    ];

    println!("{}", names.choose(&mut rand::thread_rng()).unwrap());
}
