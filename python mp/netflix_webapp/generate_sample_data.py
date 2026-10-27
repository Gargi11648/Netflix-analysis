"""
Generates data/netflix_titles.csv using a CURATED LIST OF REAL NETFLIX TITLES, in the same
column format as the real Kaggle "Netflix Movies and TV Shows" dataset (netflix_titles.csv).

IMPORTANT
- Titles, type, director, cast, country, release year, genres are written from general knowledge.
  Ratings, durations and season counts are approximate (they match the dataset era, around 2021).
- The `date_added` column is SIMULATED (random date in the plausible year), NOT the real date.
- Only ~65 titles are included. For your final submission, download the full real dataset:
      https://www.kaggle.com/datasets/shivamb/netflix-shows
  and replace data/netflix_titles.csv with it. No code changes are needed.
"""
import random
import pandas as pd

random.seed(11)

# title, director, cast, country, release_year, rating, duration, listed_in, description
MOVIES = [
    ("Roma", "Alfonso Cuarón", "Yalitza Aparicio, Marina de Tavira", "Mexico", 2018, "R", "135 min", "Dramas, International Movies", "A domestic worker in 1970s Mexico City lives through a year of family upheaval."),
    ("The Irishman", "Martin Scorsese", "Robert De Niro, Al Pacino, Joe Pesci", "United States", 2019, "R", "209 min", "Dramas", "A hitman looks back on his life in organized crime and his ties to a union boss."),
    ("Marriage Story", "Noah Baumbach", "Adam Driver, Scarlett Johansson, Laura Dern", "United States", 2019, "R", "137 min", "Dramas", "A director and an actress navigate a painful divorce and custody dispute."),
    ("Bird Box", "Susanne Bier", "Sandra Bullock, Trevante Rhodes, John Malkovich", "United States", 2018, "R", "124 min", "Horror Movies, Thrillers", "A mother leads her children through a world where looking outside can be deadly."),
    ("The Platform", "Galder Gaztelu-Urrutia", "Iván Massagué, Zorion Eguileor, Antonia San Juan", "Spain", 2019, "TV-MA", "94 min", "Horror Movies, International Movies, Sci-Fi & Fantasy", "Inmates in a vertical prison fight over a platform of food that descends level by level."),
    ("Extraction", "Sam Hargrave", "Chris Hemsworth, Rudhraksh Jaiswal, Randeep Hooda", "United States, India", 2020, "R", "117 min", "Action & Adventure", "A mercenary tries to rescue a kidnapped crime lord's son in Dhaka."),
    ("The Old Guard", "Gina Prince-Bythewood", "Charlize Theron, KiKi Layne, Matthias Schoenaerts", "United States", 2020, "R", "125 min", "Action & Adventure, Sci-Fi & Fantasy", "A group of immortal mercenaries protects the world while a new member joins them."),
    ("Enola Holmes", "Harry Bradbeer", "Millie Bobby Brown, Henry Cavill, Sam Claflin", "United Kingdom", 2020, "PG-13", "123 min", "Action & Adventure, Dramas", "Sherlock's teenage sister searches for her missing mother and gets drawn into a mystery."),
    ("Da 5 Bloods", "Spike Lee", "Delroy Lindo, Jonathan Majors, Chadwick Boseman", "United States", 2020, "R", "155 min", "Dramas", "Four Vietnam War veterans return to Vietnam to recover a fallen squad leader and buried treasure."),
    ("Okja", "Bong Joon-ho", "Tilda Swinton, Paul Dano, Seo-hyun Ahn", "South Korea, United States", 2017, "TV-MA", "120 min", "Action & Adventure, Dramas, International Movies", "A girl fights to save her giant animal friend from a powerful corporation."),
    ("Klaus", "Sergio Pablos", "Jason Schwartzman, J.K. Simmons, Rashida Jones", "Spain", 2019, "PG", "97 min", "Children & Family Movies, Comedies", "A postman and a reclusive toymaker form an unlikely friendship in a feuding town."),
    ("The Two Popes", "Fernando Meirelles", "Anthony Hopkins, Jonathan Pryce, Juan Minujín", "United Kingdom, Italy, Argentina, United States", 2019, "PG-13", "125 min", "Comedies, Dramas", "Two popes with opposing views meet to discuss the future of the Catholic Church."),
    ("Dolemite Is My Name", "Craig Brewer", "Eddie Murphy, Wesley Snipes, Da'Vine Joy Randolph", "United States", 2019, "R", "118 min", "Comedies, Dramas", "Entertainer Rudy Ray Moore creates a blaxploitation hero and a cult film."),
    ("6 Underground", "Michael Bay", "Ryan Reynolds, Mélanie Laurent, Manuel Garcia-Rulfo", "United States", 2019, "R", "128 min", "Action & Adventure, Comedies", "Six people fake their deaths to form a vigilante team that takes on dangerous targets."),
    ("Murder Mystery", "Kyle Newacheck", "Adam Sandler, Jennifer Aniston, Luke Evans", "United States", 2019, "PG-13", "97 min", "Comedies", "A couple on a European vacation becomes the prime suspects in a billionaire's murder."),
    ("The Social Dilemma", "Jeff Orlowski", "Tristan Harris, Jeff Seibert, Bailey Richardson", "United States", 2020, "PG-13", "94 min", "Documentaries", "Tech experts explain how social media is designed to influence its users."),
    ("My Octopus Teacher", "Pippa Ehrlich, James Reed", "Craig Foster", "South Africa", 2020, "G", "85 min", "Documentaries, International Movies", "A filmmaker forms an extraordinary bond with an octopus in a South African kelp forest."),
    ("Crip Camp", "Nicole Newnham, James LeBrecht", "Judith Heumann, James LeBrecht", "United States", 2020, "PG-13", "108 min", "Documentaries", "Campers at a summer camp for teens with disabilities help spark a disability rights movement."),
    ("Mowgli: Legend of the Jungle", "Andy Serkis", "Rohan Chand, Christian Bale, Cate Blanchett", "United States, United Kingdom", 2018, "PG-13", "104 min", "Action & Adventure, Children & Family Movies, Dramas", "A boy raised by wolves must find his place between the jungle and the world of men."),
    ("Lust Stories", "Anurag Kashyap, Zoya Akhtar, Dibakar Banerjee, Karan Johar", "Radhika Apte, Bhumi Pednekar, Vicky Kaushal", "India", 2018, "TV-MA", "124 min", "Dramas, International Movies, Romantic Movies", "Four short films explore love, desire and relationships in modern India."),
    ("Bulbbul", "Anvita Dutt", "Tripti Dimri, Avinash Tiwary, Rahul Bose", "India", 2020, "TV-MA", "94 min", "Dramas, Horror Movies, International Movies", "A woman's past and a series of mysterious deaths haunt a Bengal village."),
    ("Gunjan Saxena: The Kargil Girl", "Sharan Sharma", "Janhvi Kapoor, Pankaj Tripathi, Angad Bedi", "India", 2020, "TV-14", "112 min", "Dramas, International Movies", "A young woman fights to become one of India's first female air force combat pilots."),
    ("Choked: Paisa Bolta Hai", "Anurag Kashyap", "Saiyami Kher, Roshan Mathew, Amruta Subhash", "India", 2020, "TV-MA", "114 min", "Dramas, International Movies", "A bank cashier finds wads of cash in her kitchen drain just as demonetisation hits."),
    ("Eurovision Song Contest: The Story of Fire Saga", "David Dobkin", "Will Ferrell, Rachel McAdams, Pierce Brosnan", "United States", 2020, "PG-13", "123 min", "Comedies, Music & Musicals", "Two small-town musicians get a shot at representing Iceland in Eurovision."),
    ("The Kissing Booth", "Vince Marcello", "Joey King, Joel Courtney, Jacob Elordi", "United States", 2018, "TV-14", "105 min", "Comedies, Romantic Movies", "A teen's secret crush on her best friend's older brother tests their friendship."),
    ("To All the Boys I've Loved Before", "Susan Johnson", "Lana Condor, Noah Centineo, Janel Parrish", "United States", 2018, "TV-14", "100 min", "Comedies, Dramas, Romantic Movies", "A teen's secret love letters are mailed to her crushes without her knowing."),
    ("Beasts of No Nation", "Cary Joji Fukunaga", "Idris Elba, Abraham Attah, Emmanuel Nii Adom Quaye", "United States", 2015, "TV-MA", "137 min", "Dramas", "A young boy is forced to become a child soldier during a civil war in West Africa."),
    ("I Care a Lot", "J Blakeson", "Rosamund Pike, Peter Dinklage, Eiza González", "United Kingdom, United States", 2020, "R", "118 min", "Comedies, Dramas, Thrillers", "A court-appointed guardian exploiting elderly clients meets her match."),
    ("Mank", "David Fincher", "Gary Oldman, Amanda Seyfried, Lily Collins", "United States", 2020, "R", "131 min", "Dramas", "Screenwriter Herman Mankiewicz races to finish the script for Citizen Kane."),
    ("The Trial of the Chicago 7", "Aaron Sorkin", "Eddie Redmayne, Sacha Baron Cohen, Mark Rylance", "United States", 2020, "R", "130 min", "Dramas", "Seven defendants are put on trial after the 1968 Democratic National Convention protests."),
    ("The Mitchells vs. the Machines", "Mike Rianda", "Abbi Jacobson, Danny McBride, Maya Rudolph", "United States", 2021, "PG", "114 min", "Children & Family Movies, Comedies", "A dysfunctional family road trip turns into a fight against a robot uprising."),
    ("Red Notice", "Rawson Marshall Thurber", "Dwayne Johnson, Ryan Reynolds, Gal Gadot", "United States", 2021, "PG-13", "118 min", "Action & Adventure, Comedies", "An FBI profiler teams up with an art thief to catch a rival criminal."),
    ("Don't Look Up", "Adam McKay", "Leonardo DiCaprio, Jennifer Lawrence, Meryl Streep", "United States", 2021, "R", "138 min", "Comedies, Dramas", "Two astronomers try to warn humanity about a comet heading for Earth."),
    ("The Power of the Dog", "Jane Campion", "Benedict Cumberbatch, Kirsten Dunst, Jesse Plemons", "New Zealand, United Kingdom, Canada, Australia", 2021, "R", "126 min", "Dramas", "A charismatic rancher torments his brother's new wife and her son."),
]

SHOWS = [
    ("Stranger Things", None, "Millie Bobby Brown, Finn Wolfhard, Winona Ryder, David Harbour", "United States", 2016, "TV-14", "3 Seasons", "TV Horror, TV Mysteries, TV Sci-Fi & Fantasy", "A group of kids in a small town uncovers supernatural secrets and a government experiment."),
    ("The Crown", None, "Claire Foy, Olivia Colman, Matt Smith, Josh O'Connor", "United Kingdom, United States", 2016, "TV-MA", "4 Seasons", "British TV Shows, TV Dramas", "The reign of Queen Elizabeth II and the political and personal events that shaped it."),
    ("Narcos", None, "Wagner Moura, Boyd Holbrook, Pedro Pascal", "United States, Colombia", 2015, "TV-MA", "3 Seasons", "Crime TV Shows, International TV Shows, TV Dramas", "The rise and fall of drug lord Pablo Escobar and the agents who hunted him."),
    ("Money Heist", None, "Úrsula Corberó, Álvaro Morte, Itziar Ituño", "Spain", 2017, "TV-MA", "4 Seasons", "Crime TV Shows, International TV Shows, Spanish-Language TV Shows", "A mastermind recruits a crew to carry out an ambitious heist on the Royal Mint of Spain."),
    ("Dark", None, "Louis Hofmann, Lisa Vicari, Oliver Masucci", "Germany", 2017, "TV-MA", "3 Seasons", "Crime TV Shows, International TV Shows, TV Sci-Fi & Fantasy", "A missing child sets four families on a hunt for answers across time."),
    ("Sacred Games", None, "Saif Ali Khan, Nawazuddin Siddiqui, Radhika Apte", "India", 2018, "TV-MA", "2 Seasons", "Crime TV Shows, International TV Shows, TV Dramas", "A Mumbai police officer has 25 days to stop a threat to the city."),
    ("Delhi Crime", None, "Shefali Shah, Rasika Dugal, Rajesh Tailang", "India", 2019, "TV-MA", "1 Season", "Crime TV Shows, International TV Shows, TV Dramas", "Police investigate a brutal crime in Delhi in a dramatised account of a real case."),
    ("Jamtara - Sabka Number Ayega", None, "Amit Sial, Aksha Pardasany, Sparsh Shrivastava", "India", 2020, "TV-MA", "1 Season", "Crime TV Shows, International TV Shows, TV Dramas", "Young men in a small Indian town run phishing scams, until a police officer arrives."),
    ("The Witcher", None, "Henry Cavill, Anya Chalotra, Freya Allan", "Poland, United States", 2019, "TV-MA", "1 Season", "TV Action & Adventure, TV Dramas, TV Sci-Fi & Fantasy", "A monster hunter's path crosses with a sorceress and a young princess."),
    ("Squid Game", None, "Lee Jung-jae, Park Hae-soo, Jung Ho-yeon", "South Korea", 2021, "TV-MA", "1 Season", "International TV Shows, TV Action & Adventure, TV Dramas", "Cash-strapped contestants risk their lives in deadly children's games for a huge prize."),
    ("Bridgerton", None, "Phoebe Dynevor, Regé-Jean Page, Jonathan Bailey", "United States", 2020, "TV-MA", "1 Season", "Romantic TV Shows, TV Dramas", "Romance and scandal among London's high society in the Regency era."),
    ("The Queen's Gambit", None, "Anya Taylor-Joy, Bill Camp, Marielle Heller", "United States", 2020, "TV-MA", "1 Season", "TV Dramas", "An orphaned chess prodigy rises to the top while battling addiction."),
    ("Ozark", None, "Jason Bateman, Laura Linney, Sofia Hublitz", "United States", 2017, "TV-MA", "3 Seasons", "Crime TV Shows, TV Dramas, TV Thrillers", "A financial planner moves his family to the Ozarks to launder money for a drug cartel."),
    ("Sense8", None, "Tuppence Middleton, Max Riemelt, Aml Ameen", "United States", 2015, "TV-MA", "2 Seasons", "TV Dramas, TV Mysteries, TV Sci-Fi & Fantasy", "Eight strangers around the world become mentally and emotionally connected."),
    ("Lupin", None, "Omar Sy, Ludivine Sagnier, Clotilde Hesme", "France", 2021, "TV-MA", "1 Season", "Crime TV Shows, International TV Shows, TV Dramas", "A gentleman thief seeks revenge on the family that wronged his father."),
    ("Elite", None, "María Pedraza, Miguel Herrán, Jaime Lorente", "Spain", 2018, "TV-MA", "3 Seasons", "Crime TV Shows, International TV Shows, Spanish-Language TV Shows", "Students from different backgrounds clash at an elite school, and a murder follows."),
    ("Kingdom", None, "Ju Ji-hoon, Bae Doona, Ryu Seung-ryong", "South Korea", 2019, "TV-MA", "2 Seasons", "International TV Shows, Korean TV Shows, TV Horror", "A crown prince investigates a mysterious plague in Joseon-era Korea."),
    ("Master of None", None, "Aziz Ansari, Lena Waithe, Eric Wareheim", "United States", 2015, "TV-MA", "3 Seasons", "TV Comedies, TV Dramas", "An actor in New York navigates dating, career and family life."),
    ("The Umbrella Academy", None, "Elliot Page, Tom Hopper, David Castañeda", "United States", 2019, "TV-14", "2 Seasons", "TV Action & Adventure, TV Comedies, TV Dramas", "Estranged siblings with superpowers reunite to solve the mystery of their father's death."),
    ("Mindhunter", None, "Jonathan Groff, Holt McCallany, Anna Torv", "United States", 2017, "TV-MA", "2 Seasons", "Crime TV Shows, TV Dramas, TV Thrillers", "FBI agents interview imprisoned serial killers to understand how they think."),
    ("Cobra Kai", None, "Ralph Macchio, William Zabka, Xolo Maridueña", "United States", 2018, "TV-14", "3 Seasons", "TV Action & Adventure, TV Comedies, TV Dramas", "Decades after the All Valley Karate Tournament, the rivalry between two dojos is revived."),
    ("Making a Murderer", None, "Steven Avery, Brendan Dassey, Dean Strang", "United States", 2015, "TV-MA", "2 Seasons", "Crime TV Shows, Docuseries", "A documentary series following a Wisconsin man's conviction and the case against him."),
    ("Our Planet", None, "David Attenborough", "United Kingdom", 2019, "TV-G", "1 Season", "British TV Shows, Docuseries, Science & Nature TV", "A nature documentary on the planet's wildlife and the impact of climate change."),
    ("Never Have I Ever", None, "Maitreyi Ramakrishnan, Poorna Jagannathan, Richa Moorjani", "United States", 2020, "TV-14", "2 Seasons", "TV Comedies", "An Indian-American teenager tries to reinvent her social life after a difficult year."),
    ("Sex Education", None, "Asa Butterfield, Gillian Anderson, Emma Mackey", "United Kingdom", 2019, "TV-MA", "3 Seasons", "British TV Shows, TV Comedies, TV Dramas", "A teen with a sex therapist mother starts an advice clinic at school."),
    ("The Haunting of Hill House", None, "Michiel Huisman, Carla Gugino, Henry Thomas", "United States", 2018, "TV-MA", "1 Season", "TV Dramas, TV Horror, TV Mysteries", "Siblings haunted by their childhood in a notorious house confront their past."),
    ("Love, Death & Robots", None, None, "United States", 2019, "TV-MA", "2 Seasons", "TV Sci-Fi & Fantasy, TV Horror, TV Comedies", "An anthology of short animated stories spanning sci-fi, fantasy, horror and comedy."),
    ("Peaky Blinders", None, "Cillian Murphy, Paul Anderson, Helen McCrory", "United Kingdom", 2013, "TV-MA", "5 Seasons", "British TV Shows, Crime TV Shows, TV Dramas", "A gangster family in 1900s Birmingham rises through crime and politics."),
    ("Breaking Bad", None, "Bryan Cranston, Aaron Paul, Anna Gunn", "United States", 2008, "TV-MA", "5 Seasons", "Crime TV Shows, TV Dramas, TV Thrillers", "A chemistry teacher turns to making methamphetamine after a cancer diagnosis."),
    ("Friends", None, "Jennifer Aniston, Courteney Cox, Lisa Kudrow", "United States", 1994, "TV-14", "10 Seasons", "Classic & Cult TV, TV Comedies", "Six friends navigate life and love in New York City."),
]

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def date_added(release_year):
    """SIMULATED date: same year as release for recent titles, 2016-2020 for older licensed ones."""
    year = release_year if release_year >= 2015 else random.randint(2016, 2020)
    return f"{random.choice(MONTHS)} {random.randint(1, 28)}, {year}"


rows = []
for kind, data in (("Movie", MOVIES), ("TV Show", SHOWS)):
    for title, director, cast, country, year, rating, duration, genres, desc in data:
        rows.append({
            "show_id": f"s{len(rows) + 1}", "type": kind, "title": title, "director": director,
            "cast": cast, "country": country, "date_added": date_added(year),
            "release_year": year, "rating": rating, "duration": duration,
            "listed_in": genres, "description": desc, "is_sample": True,
        })

random.shuffle(rows)
for i, r in enumerate(rows, 1):
    r["show_id"] = f"s{i}"

pd.DataFrame(rows).to_csv("data/netflix_titles.csv", index=False)
print(f"Created data/netflix_titles.csv with {len(rows)} real titles "
      f"({len(MOVIES)} movies, {len(SHOWS)} TV shows)")
