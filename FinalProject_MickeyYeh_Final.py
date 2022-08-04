import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px  # iteractive plot
# from geopy import geocoders
# import geopy.geocoders as geocoders
from geopy.geocoders import Nominatim


def boston_district(dataFile):
    if "A1" == dataFile:
        return "Downtown & Charlestown"
    elif "A15" == dataFile:
        return "Downtown & Charlestown"
    elif "A7" == dataFile:
        return "East Boston"
    elif "B2" == dataFile:
        return "Roxbury"
    elif "B3" == dataFile:
        return "Mattapan"
    elif "C6" == dataFile:
        return "South Boston"
    elif "C11" == dataFile:
        return "Dorchester"
    elif "D4" == dataFile:
        return "South End"
    elif "D14" == dataFile:
        return "Brighton"
    elif "E5" == dataFile:
        return "West Roxbury"
    elif "E13" == dataFile:
        return "Jamaica Plain"
    elif "E18" == dataFile:
        return "Hyde Park"
    else:
        return None


def web_title_text(title="Boston Crime Data", text="This website shows you the 2021 crime data in Boston."):

    # Title/Heading
    st.title(title)
    # Subheading
    st.write(text)


def header_description(header="None", description=""):
    return header, description


def interactive_plot(dataframe):
    # simple scatter plot
    scatterplot_header, scatterplot_description = header_description("Data Scatter Plot", "Select X and Y axis.")
    st.header(scatterplot_header)
    st.write(scatterplot_description)
    # selection box
    x_axis_val = st.selectbox("Select X-Axis Value", options=dataframe.columns)
    y_axis_val = st.selectbox("Select Y-Axis Value", options=dataframe.columns)
    # plot
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)
    st.header("")


upload_file = st.file_uploader("Upload Your File Here(one only)", accept_multiple_files=False, key='test')  # one file ata time!
# wrap and see if file has been uploaded
if upload_file:
    if upload_file.name == "bostoncrime2021_7000_sample(1).csv":
        dataFileName = upload_file.name
        BostonCrimeData = pd.read_csv(dataFileName, skipinitialspace=True)  # skipinitialspace=True to get rid of extra white spaces in data
        # BostonCrimeData = pd.read_csv(dataFileName, skipinitialspace=True, header=None)  # header=None means no header
        df = BostonCrimeData

        # modify district name
        df["DISTRICT_New"] = df["DISTRICT"].apply(boston_district)

        # cleaning data-1 drop unused columns
        df.drop('OFFENSE_CODE_GROUP', axis=1, inplace=True)
        df.drop('UCR_PART', axis=1, inplace=True)

        # change coordinates
        # pydeck expects input data in (X, Y) format and data given position is specified in lat-lon, which is (Y, X)
        newCol_dict = {}
        newCol_list = []
        a = 0
        for i in range(len(df)):
            longitude = df['Long'][i]
            latitude = df['Lat'][i]
            newCol_list.append(longitude)
            newCol_list.append(latitude)
            newCol_dict[df['INCIDENT_NUMBER'][i]] = (newCol_list[a], newCol_list[a+1])
            a += 2

        # add new columns from dictionary # dict key will be added
        df['Location_New'] = newCol_dict.values()

        # # drop rows and columns with Null/NaN values
        df_clean1 = df.dropna()

        #drop any rows that have 0 in the Lat column
        df_clean2 = df_clean1[df_clean1.Lat != 0]

        # sort data by INCIDENT_NUMBER col
        df_clean_sorted = df_clean2.sort_values(by=['INCIDENT_NUMBER'])

    else:
        df = pd.read_csv(upload_file)
        df_clean = df.dropna()
        # sort data
        """
        [inplace=True] 
        keyword in a pandas method changes the default behaviour such that 
        the operation on the dataframe doesn’t return anything, it instead ‘modifies the 
        underlying data’ (more on that later). It mutates the actual object which you apply it to.
    
        [inplace=False] 
        (which is the default behaviour) the dataframe operation returns a copy 
        of the dataframe, leaving the original data intact.
        """
        df_clean_sorted = df.sort_index(inplace=False)

    # Title/Heading
    web_title_text(upload_file.name, "You can start visualizing your data")

    # Data Statistics
    data_header, data_description = header_description("Data Statistics", "Quick view of your dataset.")
    st.header(data_header)
    st.write(data_description)
    st.write(df_clean_sorted.describe())


    ##### Graph 1 #####
    map_header, map_description = header_description("World Map", "Move to orange points on the map to see crime data.")
    st.header(map_header)
    st.write(map_description)

    # user input to get desired location
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")

    view_city = st.text_input('View City:', 'Boston')
    view_location = geolocator.geocode(view_city)

    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_clean_sorted,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=1,
        radius_max_pixels=10,
        line_width_min_pixels=1,
        get_position="Location_New",
        get_radius=5,
        get_fill_color=[255, 140, 0],
        get_line_color=[0, 0, 0],
        )

    view_state = pdk.ViewState(latitude=view_location.latitude, longitude=view_location.longitude, zoom=12, bearing=0, pitch=0)

    # Render
    st.pydeck_chart(pdk.Deck(
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{OCCURRED_ON_DATE}\nDistrict: {DISTRICT}\n{STREET}\n{OFFENSE_DESCRIPTION}"}))
    # r.to_html("scatterplot_layer.html")
    st.header("")


    ##### Graph 2 #####
    interactive_plot(df_clean_sorted)


    ##### Graph 3 #####
    pie_header, pie_description = header_description("Pie Chart", "")
    st.header(pie_header)
    st.write(pie_description)

    # select columns you want for the pie chart
    values = st.selectbox("Select Pie Chart Value", options=df_clean_sorted.columns)

    labels = df["DISTRICT_New"]
    fig = px.pie(df_clean_sorted, values=values, names='DISTRICT_New',
                 #title='Population of American continent',
                 hover_data=['DISTRICT_New'])  #, labels=labels)

    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig)



