import unittest
from news_scraper import parse_bbc_headlines


class TestParseHeadlines(unittest.TestCase):

    def test_parse_html_file(self):
        fd = open('bbc_raw_test.html')
        result = ["Trump hails 'perfect' Syria strikes", "'We heard rumble like thunder'",
                  'Were the Syria air strikes legal?', 'PM has chosen which way to jump on Syria',
                  "'No alternative' to Syria strikes - May", 'Moment missiles fired from ship',
                  'Western powers strike Syria targets', "UK 'confident' of Syria air strike success",
                  'Rugby players Jackson and Olding sacked', 'Three female jockeys seek National history',
                  'Film fans mourn director Milos Forman', "Crowds gather for Winnie Mandela's funeral",
                  'England reach first Commonwealth final', 'England reach first Commonwealth final',
                  'Trump lawyer under criminal investigation', 'Kenya elephant rescuer Sheldrick dies',
                  "FBI deputy director 'misled investigators'", 'Police officer inhales drugs during arrest',
                  'French court freezes Johnny Hallyday assets', "Fugitive among Europe's 'most wanted'",
                  'Last-second winner sends England into netball final', "England's relay double, Wales add to tally",
                  'England take double 4x100m relay gold', 'Spectacular buzzer beater sends Canada to basketball final',
                  'Some of the best news photos from the past week', "Pinstickers' guide to the Grand National",
                  "'I lost seven stone to save my liver'", 'Britain, France, US launch Syria air strikes',
                  'How I fled North Korea', 'The dog getting over its bad image',
                  "Will Western strikes sway Syria's Assad?", 'Why are polls and Facebook ads at odds in Ireland?',
                  'Coffee: Who grows, drinks and pays the most?', 'Gut instinct: Why I put my poo in the post',
                  'What Winnie Mandela meant to me', 'Why India woke up so late to a brutal rape',
                  'Man made football mascot in stag do prank', 'Queen and Attenborough share a joke',
                  'Cat and dog travel buddies capture hearts', 'Inside the White House Bible Study group',
                  'Quiet horror movie shames snack-eaters', 'Sprinting sisters race for the top',
                  'Hellblade: Bafta for first-time actress', "It 2 'to begin shooting this summer'",
                  'Coachella being sued over artist ban', 'Khloe Kardashian becomes a mum',
                  'Scottish Cup semi-final: Motherwell 3-0 Aberdeen - Main with third',
                  'Premier League: Tadic gives Southampton lead against Chelsea',
                  'Build-up to the Grand National at Aintree',
                  'County Championship - Lancashire make poor start against Notts',
                  'Premier League: Build-up for four games, inc. Burnley v Leicester',
                  'Sheff Utd host play-off rivals Millwall, plus EFL build-up']

        self.assertEqual(parse_bbc_headlines(fd), result)


if __name__ == '__main__':
    unittest.main()
