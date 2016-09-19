HW2
Assignment1: show_bus_locations_cc5219.py

Write a Python script to retrieve and report information about active vehicle for a bus line

Use the command:

python show_bus_locations.py <MTA_KEY> <BUS_LINE>

Assignment2:get_bus_info_cc5219.py

Use the command:

python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv

Thanks to Yao Wang's help with the following part:
df = pd.DataFrame({'Latitude': [lat], 'Longitude': [lon], 'Stop Name': stopname, 'Stop Status': busstatus})
    bus_info = bus_info.append(df)
    df = df.reset_index(drop=True)
    bus_info.to_csv(filename)

and taught me how to write pandas into csv as well as copy data into pandas

Assignment3:HW2_Assignment3_cc5219.ipynb

Read CSV files with pandas

Thanks to Yao Wang again with the following part:

data2 = data[['Neversink Elevation','Rondout Storage']]

And here is a problem that every time I use data.drop[('Neversink Date')] it has an error as labels ['Neversink Date'] not contained in axis.

And also thanks Yuxuan Han for the command"os.chdir"

