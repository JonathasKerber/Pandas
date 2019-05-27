dataframeExamples.py shows some basic methods of Pandas DataFrame based on the following: https://www.youtube.com/watch?v=e60ItwlZTKM

pandasExample.py is a example of how to load a large csv dataset. You should change lines 13 and 14 with the path and name of your dataset.

#   How to load large files in python

In order to load very big files, we need to load chunks of it and then concatenate these chunks. We load the dataset in pieces, and after all of the pieces are being loaded, we reconstruct the whole dataset by regrouping the loaded pieces in one whole dataframe.

#   1.  Create a Connector to a Database

#   2.  Build the Database (load the CSV file) by chunking it

2.1 It's useful to know the number of lines your dataset has (it will tell us the number of registers stored). In GNU/Linux OS, you can use 'wc' command as follows:
    ```
    wc -l  <filename>
    ```
Depending on the size of your file, it may take some seconds until you get a response at your terminal.

2.2 It's recommended to not load an entire large dataset if you don't have to in order to process your data. Instead, do your processing over the loaded chunk and store the results in a buffer.

2.3 If you DO HAVE to load the whole thing, buffer the chunks in a list inside your loading loop. OUTSIDE the loop, you should run 
    ```
    df = pd.contat(<your_buffer>)
    ```
in order to have your dataset loaded into a single dataframe. NEVER run 'pd.concat' inside the loop; it will signicantly affect your program's performance.

#   3.  Construct the Pandas DataFrame from the Dataset by calling SQL query.
3.1 You might get some reading errors due the enconding of your dataset. If that occurs you can use 
    ```
    file -i <filename>
    ```
at your terminal to find out what codec was used at your data file. After that, you should call read_csv with the argument 
    ```
    enconding=<yourFileEnconding>
    ```

#   4.  Rather than running some raw SQL query, you can run its equivalent call in pandas.
