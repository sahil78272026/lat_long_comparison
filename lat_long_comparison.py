import pandas as pds
from math import radians, cos, sin, asin, sqrt


if __name__ == "__main__":
        def haversine(lon1, lat1, lon2, lat2):
            """
            Calculate the great circle distance in kilometers between two points 
            on the earth (specified in decimal degrees)
            """
            # convert decimal degrees to radians 
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

            # haversine formula 
            dlon = lon2 - lon1 
            dlat = lat2 - lat1 
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a)) 
            r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
            return(c * r)

filePath ='D:\\lat_long.xlsx'

# lat1 = pds.read_excel(filePath,sheet_name="Sheet1", usecols="B")
df = pds.read_excel(filePath, header=None) # will read first sheet by default

lat1 = [x for x in df[1]]
long1 = [x for x in df[2]]
lat2 = [x for x in df[5]]
long2 = [x for x in df[6]]

newDist = []
for i in range(len(lat1)):
        dist = haversine(float(long1[i]),float(lat1[i]),float(long2[i]),float(lat2[i]))
        newDist.append(dist)

newDist.sort
print(newDist)


"""print(lat1)
print(long1)
print(lat2)
print(long2)"""

# haversine(float(long1[1]),float(lat1[1]),float(long2[1]),float(lat2[1]))
