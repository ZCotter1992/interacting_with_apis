# Test Module Interacting with APIs: Mean Lyrics Calculator
# Zach Cotter


# Importing required modules

import interacting_with_apis
import requests
import pytest


# Displaying test module instructions for the user to follow.

print("\n\n------------------------------------------------------------------------------------"
      "\nWELCOME\n"
      "You have chosen '-s' to see examples of mocked user input.\n"
      "Please press enter when prompted for input to run the"
      " tests. \nPassed tests are indicated by a green dot."
      " Failed tests are indicated by a red 'F'. \nThere are 9 tests in total.\n"
      "Results will be calculated and displayed after tests are conducted, this can take a moment.\n"
      "Press 'ctrl+c' to abort at any time.\n"
      "------------------------------------------------------------------------------------")


# Creating instances of normal, abnormal and extreme data to use as mock inputs during testing.

artists_name_normal = "abba"
artists_name_abnormal = '1'
artists_name_extreme = ""

song_name_normal = "waterloo"
song_name_abnormal = 1
song_name_extreme = ""

option_name_normal = "artist"
option_name_abnormal = 1
option_name_extreme = ""

analysed_songs_normal = 1
analysed_songs_abnormal = "artist"
analysed_songs_extreme = ""

artist_id_normal = "d87e52c5-bb8d-4da8-b941-9f4928627dc8"
artist_id_abnormal = 1
artist_id_extreme = ""

song_id_normal = "6bb16b15-5e54-3c22-879c-b46fcab750d6"
song_id_abnormal = 1
song_id_extreme = ""

# Defining OVH endpoint url

url = "https://api.lyrics.ovh/v1/"

# Creating instances of normal, abnormal and extreme data to use as mock inputs during testing continued...

uri_artist_search_normal = "https://musicbrainz.org/ws/2/artist?fmt=json&query=" + \
                               artists_name_normal
uri_artist_search_abnormal = "https://musicbrainz.org/ws/2/artist?fmt=json&query=" + \
                                 artists_name_abnormal
uri_artist_search_extreme = "https://musicbrainz.org/ws/2/artist?fmt=json&query=" + \
                                artists_name_extreme

artist_data_normal = requests.get(uri_artist_search_normal).json()
artist_data_abnormal = requests.get(uri_artist_search_abnormal).json()
artist_data_extreme = requests.get(uri_artist_search_extreme).json()

# Item artist["id"] retrieved by get_artist_info should always be returned without exception as url encoder
# should convert input to string. Efficacy of URL encoder is also tested.

uri_artist_works_normal = "https://musicbrainz.org/ws/2/work?artist=" + artist_id_normal + \
                                  "&fmt=json&limit=100"
uri_artist_works_abnormal = "https://musicbrainz.org/ws/2/work?artist=" + str(artist_id_abnormal) + \
                                    "&fmt=json&limit=100"
uri_artist_works_extreme = "https://musicbrainz.org/ws/2/work?artist=" + artist_id_extreme + \
                                   "&fmt=json&limit=100"
uri_artist_recordings = "https://musicbrainz.org/ws/2/recording?work=" + song_id_normal + \
                                "&fmt=json&limit=100"

# Giving a test example of song lyrics uri.

uri_song_lyrics = "https://api.lyrics.ovh/v1/abba/waterloo"

# Creating instances of normal, abnormal and extreme data to use as mock inputs during testing continued...

artist_info_connection = requests.get(uri_artist_search_normal)
artist_works_connection = requests.get(uri_artist_works_normal)
artist_recordings_connection = requests.get(uri_artist_recordings)
song_lyrics_connection = requests.get(uri_song_lyrics)


def test_connections():

    # Testing API connection by checking response code (200 indicates response received).

    assert artist_info_connection.status_code == 200
    assert artist_works_connection.status_code == 200
    assert artist_recordings_connection.status_code == 200
    assert song_lyrics_connection.status_code == 200


def test_url_encoder():

    # Testing whether url encoder converts input to string datatype.

    assert isinstance(interacting_with_apis.url_encoder(url), str)


def test_uri_search():

    # Testing whether artist search returns string datatype for normal, abnormal and extreme data input.

    assert isinstance(uri_artist_search_normal, str)
    assert isinstance(uri_artist_search_abnormal, str)
    assert isinstance(uri_artist_search_extreme, str)

    # Testing whether artist search raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        requests.get(uri_artist_search_normal)
        requests.get(uri_artist_search_abnormal)
        requests.get(uri_artist_search_extreme)
        assert False


def test_artist_num_choice():

    # Testing whether artist number choice raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.artist_num_choice(option_name_normal)
        interacting_with_apis.artist_num_choice(option_name_abnormal)
        interacting_with_apis.artist_num_choice(option_name_extreme)
        assert False


def test_analysed_songs_num():

    # Testing whether user input for number of songs to average across raises exception for normal,
    # abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.analysed_songs_num(analysed_songs_normal)
        interacting_with_apis.analysed_songs_num(analysed_songs_abnormal)
        interacting_with_apis.analysed_songs_num(analysed_songs_extreme)
        assert False


def test_get_artist_info():

    # Testing whether retrieving artist info raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.get_artist_info(artists_name_normal)
        interacting_with_apis.get_artist_info(artists_name_abnormal)
        interacting_with_apis.get_artist_info(artists_name_extreme)
        assert False


def test_get_artist_works():

    # Testing whether retrieving artist works raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.get_artist_works()
        requests.get(uri_artist_works_normal)
        requests.get(uri_artist_works_abnormal)
        requests.get(uri_artist_works_extreme)
        assert False


def test_get_artist_recordings():

    # Testing whether retrieving artist recordings raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.get_artist_recordings(song_id_normal)
        interacting_with_apis.get_artist_recordings(song_id_abnormal)
        interacting_with_apis.get_artist_recordings(song_id_extreme)
        assert False


def test_get_song_lyrics():

    # Testing whether retrieving song lyrics raises exception for normal, abnormal and extreme data input.

    with pytest.raises(Exception):
        interacting_with_apis.get_song_lyrics(artists_name_normal, song_name_normal)
        interacting_with_apis.get_song_lyrics(artists_name_abnormal, song_name_abnormal)
        interacting_with_apis.get_song_lyrics(artists_name_extreme, song_name_extreme)
        assert False
