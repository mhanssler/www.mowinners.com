""""If I make a file here, as long as it is in this space, I can push it to Github. So Each time I am done with something, i nee
need to push it!"""

import pandas as pd

data = r'C:\Users\mhans\PycharmProjects\www.mowinners.com\cities.csv'
df = pd.read_csv(data)
print(df.head)
#frame = pd.DataFrame(data)
#print(frame)
