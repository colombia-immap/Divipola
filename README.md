# Divipola
to add the divipola codes to a database. 
# Instructions
First it is required to upload the database to be joined, it is necessary that the database has some unique data in common so that they can be joined. 

After uploading the databases, a single column is generated since in Colombia the municipalities have the same name despite being in different departments. 

So a column was created through the concatenation of the names of the departments and municipalities, so that they are unique. 

Already created the unique column with which the union will be made, it is necessary to clean the base, which we do: eliminating all the characters  as well as converting our texts in lowercase to mitigating the possible errors. 

Next, we apply a check on the names of the departments and municipalities to see that no code is missing. 

If so, an error message will appear saying "Adjust the Department" or "Adjust the municipality". 

Below are two tests with which you can check the possible error manually. 

Usually what happens is that a name is written completely different in one of the bases or there is a typing error in the database. So a manual check is required. But to simplify the work the test is sorted in alphabetical order. 

Finally after making the correct merge without any error, the required columns are selected and the dataset is exported.

- The Divipola Code is in the folder uploaded and the final excel. 
