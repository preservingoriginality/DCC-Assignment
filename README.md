Firstly we use the Fitz library to get all the information from the electoral bond pdf into a csv file. For this I have used Command  prompt, which is safe secure and it directly connects to the server. We import the library than we generate a document out of that 
![Screenshot 2024-04-16 181359](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/3fb6055b-505b-44f3-ac76-c6c0a35d3dc9)
Then we get all the information from the  table by using page.find tables. From there we get a huge list from every page.Thereafter from every page we geta huge list, which we append to a more bigger list 


![Screenshot 2024-04-16 162914](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/bf1c9437-d615-4a8b-b906-7aa22c925377)


Then from that big list we make a pandas dataframe which is easily converted to the csv file
![Screenshot 2024-04-16 174304](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/7578cab3-fc85-4441-8e52-8ca777f3318e)

Similarly we do the same procedure for the next pdf
![Screenshot 2024-04-16 181420](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/5bc74ba2-e213-4302-bb3d-87c21caec966)
![Screenshot 2024-04-16 181818](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/c3a2b581-435a-4de5-95e0-db6b97cfefc0)

After getting the csv files we upload them on MySQL
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/640bb2cd-dddb-4e21-a76c-8f60e352c80d)

After uploading this sql we create the front end using simply html and we use flask for making the backend.
Here, main1.py is the backend code for the whole website pages.
Index.html is the front page and other html webpages are being the subsidiary pages.


Here  I required to change a  llot of names in the sql files columns index so  that the variables follow all the variable laws of all languages.  I have tried to integrate chartjs graph using the code given at their official websites; but that didnt went well. HOWEVer all the tabular data is being properly acquired through this project.I havent used css elements due to time constraints; however I am successful utilising html corely. 
Following are the snips from the website generated

for accesing this webpage, you firstly need to save all the files in the pc together, then run main1.py and also you can use any browser to type 127.0.0.5000/ and you can easily access this. Here option for 
main page
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/014697af-3586-44e8-ad20-8c980199d238)

Search by bond number
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/e906ebe7-934f-44d8-9a51-bc3a58647983)
result
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/074165f5-b2ab-4109-818e-44554d7f75ef)


party statistics
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/ee47bed9-94d1-4967-945b-3db9927d51d0)
result
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/d8598c91-7ee9-468b-963d-6e7d9965e5e6)
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/d984946e-d591-41ac-9c22-7a0774d63e21)

company statistics
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/e840f35d-f57e-45f3-8985-eed1f51e7829)
result
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/5f003a92-7b13-42d6-9348-dd474c39da73)

party donors
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/011f8493-30cf-4bc8-8658-27eb73ca94f6)
result
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/3d7c30d8-9b43-4836-adf3-251749b9382a)

company donations
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/7ebaa27e-c8ef-43d2-bf44-b68fb43bcf70)
results
![image](https://github.com/preservingoriginality/DCC-Assignment/assets/167908457/2e3b6dd8-134b-4dc9-82a9-611928ab41de)













