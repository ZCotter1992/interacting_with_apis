# Interacting with APIs: Mean Lyrics Calculator
# Zach Cotter


# Importing required modules.

import requests
import matplotlib.pyplot as plt


# Declaring functions & global variables.


# Converting user artist name input into url.

def url_encoder(url):
    return url.replace("/", " ")


# The endpoint data for the artist's info and for song lyrics.

retrieve_artist_info_endpoint = "https://musicbrainz.org/ws/2/artist?fmt=json&query="
retrieve_song_lyric_end_point = "https://api.lyrics.ovh/v1/"


# Getting user input to select an artist from top ten related artist search results returned.

def artist_num_choice(option_name):

    try:
        return int(input("\nPlease enter the number listed for your " + option_name +
                         " above. \nIf no artists are listed above, please press "
                         "'Enter' to return to beginning of search.\n\n"
                         "Enter artist number: "))

    # Handling errors so user can only input integers relating to top ten results returned.

    except ValueError:
        print("\nPlease search again and enter the number of one of the artists shown in search "
              "results (1-10).")


# Getting artist info by using url artist search url concatenated with url-encoded user input
# of artist name.

def get_artist_info(artists_name):

    try:
        # Get the artist's data from the API, extract data as json, assign a number to the artist
        # search result.

        uri_artist_search = retrieve_artist_info_endpoint + url_encoder(artists_name)
        artist_data = requests.get(uri_artist_search).json()
        artist_num = 1

    # Handling errors to prompt user to check internet connection if data cannot be retrieved from artist
    # data API.

    except Exception:
        print("\nUnable to connect to Musicbrainz. Please check your internet connection.")

    try:
        # Display the top ten results retrieved from artist data json and display any retrieved
        # disambiguation info for displayed artist.

        for items in artist_data["artists"][:10]:
            print(artist_num, items["name"])
            if "disambiguation" in items.keys():
                print(items["disambiguation"])

            artist_num += 1

        switch_case = artist_num_choice("artist")
        if switch_case <= 10:

            return artist_data["artists"][switch_case-1]

        # Prompting user to only enter a number 1-10 corresponding to displayed artist search results.

        else:
            print("\nPlease search again and enter the number of one of the artists shown in search "
                  "results (1-10).")

    # Handling errors to prompt user if there is a difficulty finding related artist information due
    # to an issue with the key being searched.

    except KeyError:
        print("\nUnable to find artist, please try again or search for a different artist.")

    # Handling errors to prompt user if there is a difficulty finding related artist information due
    # to incompatibility between data type of search and data type of info retrieved.

    except TypeError:
        print("\nProblem retrieving artist data, please try again or search for a different artist.")

    # Handling errors to prompt user if there is a difficulty finding related artist information due
    # to an invalid artist number being selected (>10).

    except IndexError:
        print("\nInvalid artist number selected, please try searching again.")

    # Handling errors to prompt user if there is a difficulty finding related artist information due
    # to a connectivity issue such that results cannot be retrieved to match entered search terms.

    except UnboundLocalError:
        print("\nProblem with internet connectivity during search.")


# Getting artist works info by using artist works search url concatenated with url-encoded user input of
# artist name.

def get_artist_works():

    try:
        # Retrieving artist works and extracting data as json.

        uri_artist_works = "https://musicbrainz.org/ws/2/work?artist=" + artist["id"] + "&fmt=json&limit=100"
        artist_works_data = requests.get(uri_artist_works).json()
        return artist_works_data

    # Handling errors to prompt user to check internet connection if data cannot be retrieved from
    # artist works data API.

    except Exception:
        print("\nUnable to connect to Musicbrainz. Please check your internet connection.")


# Getting artist recording info by using artist recordings search url concatenated with song id
# extracted from works json.

def get_artist_recordings(song_id):

    try:
        # Get the recording for each work of the artist and extract json.

        uri_artist_recordings = "https://musicbrainz.org/ws/2/recording?work=" + song_id + \
                                "&fmt=json&limit=100"
        artist_recordings_data = requests.get(uri_artist_recordings).json()
        return artist_recordings_data

    # Handling errors to prompt user to check internet connection if data cannot be retrieved from
    # artist recordings API.

    except Exception:
        print("\nUnable to connect to Musicbrainz. Please check your internet connection.")


# Get the lyric data from API using artist name search and songs associated with artist.

def get_song_lyrics(artists_name, song_name):

    try:
        # Getting artist song lyrics info by using ovh lyrics search url concatenated with url
        # encoded artist name search user input and song name and extract lyrics json.

        uri_song_lyrics = "https://api.lyrics.ovh/v1/" + url_encoder(artists_name) + "/" + \
                          url_encoder(song_name)
        artist_lyrics_data = requests.get(uri_song_lyrics).json()
        return artist_lyrics_data

    # Handling errors to prompt user to check internet connection if data cannot be retrieved from
    # artist song data API.

    except Exception:
        print("\nUnable to connect to Musicbrainz. Please check your internet connection.")


# Main application loop


# While loop is "y", run application (allows user t0 choose whether to search again at conclusion
# of loop iteration).


if __name__ == "__main__":

    program_loop = "y"

    while program_loop == "y":

        try:
            # Get user input to search for an artist or band name.

            artist_name = input("\nHello. Welcome to the Interacting with APIs: Mean Lyrics Calculator."
                                "\nPlease search for an artist to see the mean number of lyrics in \ntheir "
                                "songs.\nTop 10 search results will be displayed below.\n\n"
                                "Enter artist name to search: ")

            # Get artist information based on data retrieved from search.

            artist = get_artist_info(artist_name)

            # Get works by artist ID and the top 10 songs by the artist based on song id.

            artist_song_data_list = get_artist_works()

            # Create a list to hold artist recordings data.

            artist_recordings_data_list = []

            try:
                # Get user input as an integer to select how many songs to average across.

                analysed_songs_num = int(input("\nHow many songs would you like to average lyrics across?"
                                               "\nIf no artist number was selected during search please "
                                               "press 'Enter' to skip and search again.\n\n"
                                               "Number of songs to average?: "))

            # Allows user to skip choosing number of songs to average and display a prompt for this.
            # Also gives exception if invalid data entered into search.

            except ValueError:
                print("Enter button pressed, restarting search.")

            # Create a counter to track the number of analysed songs against the user input number of
            # songs to average across.

            analysed_songs_counter = 0

            # Create a counter to track the number of analysed songs against the list of artist works.

            song_index_counter = 0

            # Create a list to contain collected lyric data.

            artist_collected_data = []

            try:
                print("\n\nCalculating results, please wait...\n(Note: This will take longer with more songs"
                      " and speeds are variable with internet connectivity).")
                while analysed_songs_counter < analysed_songs_num and \
                        song_index_counter < len(artist_song_data_list["works"]):

                    # Retrieve the artist song id from works in artist song data list.

                    item = artist_song_data_list["works"][song_index_counter]
                    artist_song_id = item["id"]
                    artist_recordings = get_artist_recordings(artist_song_id)

                    # Create a list to store song recording data.

                    song_recording_data = []

                    # Retrieve song lyrics from ovh based on song titles.

                    item["lyrics"] = get_song_lyrics(artist_name, item["title"])

                    # If lyrics are found for a song, increase the counter for the number of analysed songs
                    # and add song title and lyrics to a dictionary.

                    if "recordings" in artist_recordings.keys() and len(item["lyrics"]["lyrics"]) > 0:
                        analysed_songs_counter += 1
                        collected_lyric_data = {"title": item["title"], "lyrics": item["lyrics"]}
                        artist_collected_data.append(collected_lyric_data)

                    # Continue through to end of "works" in artist song data list.

                    if analysed_songs_counter >= len(artist_song_data_list["works"]):
                        continue

                    # Increase value of song index.

                    song_index_counter += 1

                # Create int to store number of lyrics.

                num_of_lyrics = 0

                # Get the length of the list of artist collected data.

                num_of_songs = len(artist_collected_data)

                # Ensure words are separated by spaces in artist songs.

                for item in artist_collected_data:
                    new_lyrics = item["lyrics"]["lyrics"].replace("  ", " ")
                    new_lyrics = new_lyrics.replace("\n", " ")
                    new_lyrics = new_lyrics.replace("\r", " ")

                    # Split the words in artist songs based on spaces into a lyric count entry.

                    new_lyrics = new_lyrics.split(" ")
                    item["lyric_count"] = len(new_lyrics)
                    num_of_lyrics += item["lyric_count"]

                # Calculate the average (mean) number of lyrics in songs as an integer based on the stored
                # number of lyrics divided by the stored number of songs in artist collected data.

                num_mean_lyrics = int(num_of_lyrics / num_of_songs)

                # Display the results of the calculation to the user.

                print("\n\nThe artist statistics are:")
                print("\nAverage (mean) lyrics within a song = " + (str(num_mean_lyrics)))

                # Generate bar charts showing song titles and lyric counts for songs in artist collected data

                song_titles = [collected_data["title"] for collected_data in artist_collected_data]
                lyrics_num = [collected_data["lyric_count"] for collected_data in artist_collected_data]

                # Configuring and displaying the bar chart.

                plt.ylabel('Average (mean) number of lyrics in song')
                plt.xticks(rotation=45)
                plt.bar(song_titles, lyrics_num)
                plt.show()

                # Reaching the end of main application loop and displaying option to search again or
                # exit application to the user.

                program_loop = input("\n\nSearching completed, please enter lowercase 'y' to search again"
                                     " or enter any other character to exit the application. \n\n"
                                     "Continue?: ")

                # If user chooses not to continue, exits the application and displays a closing message
                # to the user.

                if program_loop != "y":
                    print("\n\nThank you for using the Interacting with APIs: Mean Lyrics Calculator! "
                          "Exiting now.\n")
                    exit()

            # Handling errors to prompt user if there is a difficulty finding related artist information due
            # to an issue with the key being searched. Displays specifically if user has specified a low
            # number of songs to average across (<4).

            except KeyError:
                if analysed_songs_num <= 4:
                    print("\nWhoops! Looks like there aren't many lyrics available for this artist. "
                          "Please enter a lower number of songs or try searching for a different artist.")

                # Handling errors to prompt user if there is a difficulty finding related artist information
                # due to an issue with the key being searched.Displays specifically if user has specified more
                # than 4 songs to average across.

                else:
                    print("\nUnable to acquire lyrics for number of songs specified. Please enter a "
                          "lower number of songs for this artist or try searching for a different artist.\n\n")

            # Handling errors to prompt user that no songs were found for the artist search.

            except ZeroDivisionError:
                print("\nUnable to find songs for this artist. Please search for a different artist.\n\n")

            # Handling errors to prompt user that lyrics were unable to be found for the number of songs
            # specified for artist.

            except Exception:
                print("\nUnable to calculate number of lyrics across songs. Please try again.\n(Note: "
                      "Specifying a lower number of songs to average across improves performance).\n\n")

            # Handling errors to prompt user that application cannot retrieve data from APIs due
            # to connectivity issues.

            except ConnectionError:
                print("\nProblem connecting to Musicbrainz and OVH.")

        # Handling errors to prompt user that there has been a problem retrieving lyric data from songs.

        except TypeError:
            print("\nCannot acquire results right now, please try again with a different number of songs "
                  "or search for a different artist.\n")

        # Handling errors to prompt user that application cannot retrieve data from APIs due
        # to connectivity issues.

        except ConnectionError:
            print("\nUnable to connect to Musicbrainz. Please check your internet connection.")
