#   IN ORDER TO LOAD VERY BIG FILES, WE NEED TO LOAD CHUNKS OF IT AND THEN CONCATENATE THESE CHUNKS. WE LOAD THE DATASE IN PIECES, AND AFTER ALL OF THE PIECES ARE BEING LOADED, WE RECONSTRUCT THE WHOLE DATASET BY REGROUPING THE LOADED PIECES IN ONE WHOLE DATAFRAME

#   HOW TO LOAD LARGE FILES WITH PYTHON
#   1.  Create a Connector to a Database

#   2.  Build the Databse (Load the CSV File) by Chunking it

    #   2.1 It's useful to know the number of lines your dataset has (it will tell us the number of registers stored). In GNU/Linux OS, you can use 'wc' command as follows:
    #   wc -l  <filename>
    #   Depending on the size of your file, it may take some seconds until you get a response at your terminal.

    #   2.2 It's recommended TO NOT load an entire large dataset if you don't have to in order to process your data. Instead, do your processing over the loaded chunk and store the results in a buffer.

    #   2.3 If you DO HAVE to load the whole thing, buffer the chunks in a list inside your loading loop. OUTSIDE the loop, you should run 'df = pd.contat(<your_buffer>)' in order to have your dataset loaded into a single dataframe. NEVER run 'pd.concat' inside the loop; it will signicantly affect your program's performance.

#   3.  Construct the Pandas DataFrame for research purpose from the Database by calling SQL query.
    #   3.1 You might get some reading errors due the enconding of your dataset. If that occurs you can use 'file -i <filename>' at your terminal to find out what codec was used at your data file.
    After that, you should call read_csv with the argument 'enconding=<yourFileEnconding>'.

#   4.  Rather than running some raw SQL query, you can run its equivalent call in pandas.
