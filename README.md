# interacting_with_apis

Interacting with APIs AireLogic Tech Test

Zach Cotter

Hello and thank you for taking the time to evaluate this tech test. To run the code please follow the instructions below.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

DOWNLOADING / INSTALLING PREREQUISITES (CLI)

You can also view the list of dependencies by looking at the 'dependencies.docx' file.

In order to run the files please first consult the list of dependencies; necessary python modules to download. They are the following.

1) requests
('pip install requests' in shell / cmd prompt, if you are using PyCharm ensure module in installed by hovering over the import statement and pressing Alt+Shift+Enter)
   
2) matplotlib
('pip install matplotlib' in shell / cmd prompt, if you are using PyCharm ensure module in installed by hovering over the import statement and pressing        Alt+Shift+Enter)

3) pytest
('pip install pytest' in shell / cmd prompt, if you are using PyCharm ensure module in installed by hovering over the import statement and pressing Alt+Shift+Enter)

Please ensure you check your Python Interpreter/path to see if the installed prerequisites are included. If you are using PyCharm you can go to:
File -> Settings -> [project_name (e.g. 'interacting_with_apis'] -> Python Interpreter

Please also ensure the .py files are contained within a single folder / project. The test module will be unable to funtion properly otherwise.

An internet connection is required to access artist and song information, allowing the .py files to function.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

RUNNING THE TEST MODULE (CLI)

To run the test module 'test_interacting_with_apis.py', cd / change directory to the location of the .py file in shell / cmd prompt, e.g. for Windows:
'cd C:\Users\[User]\PycharmProjects\interacting_with_apis\'

Then run the tests with the following command, the tests will run automatically:
'pytest test_interacting_with_apis.py'

Please note that you can also use the following command and follow the displayed instructions to see examples of mocked input as part of the testing:
'pytest test_interacting_with_apis.pys -s'

Please allow a moment or two for test results to be calculated and displayed.

Press ctrl+c to abort at any time.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

RUNNING THE PROGRAM INTERACTING WITH APIS: MEAN LYRICS CALCULATOR (CLI)

To run the program 'interacting_with_apis.py', cd / change directory to the location of the .py file in shell / cmd prompt, e.g. for Windows:
'cd C:\Users\[User]\PycharmProjects\interacting_with_apis\'

Then run the .py file with the following command:
'python interacting_with_apis.py'

Follow the instructions displayed to interact with the program. Basic sequence of instructions should be:
Enter artist name -> Enter number of a displayed artist result -> Enter number of songs to average across -> (After results are displayed) Enter 'y' to search again.

Please allow a moment or two for test results to be calculated and displayed. Results should include a plotted bar graph, please close ('x') this graph when done reading to continue with CLI program.

Press ctrl+c to abort at any time.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

SOME RECOMMENDED SEARCHES

Of course you can search for any artist you like, however it is not guaranteed that an artist will be found in the MusicBrainz database, or that song lyrics will necessarily be retrieved from OVH.

If an artist is not found or if lyrics are not retrieved, please follow the displayed instructions.

The formula for the recommended searches is as follows:
artist, artist number, number of songs to average across

1) Abba, 1, 6
2) Spice Girls, 1, 11
3) Queen, 1, 7
4) Black Veil Brides, 1, 13

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

TEST LOG

You can view the results of running the unit testing module test_interacting_with_apis.py by reading the file 'test_log_interacting_with_apis.docx'. Here you will find a table of testing results and changes made.

