# Jesus Minjares
# Pandas lecture 
import numpy as np
import pandas as pd

flows = pd.read_csv("NetFlow.csv")

flows['DURATION'] = (pd.to_datetime(flows['TIMESTAMP_END']) - pd.to_datetime(flows['TIMESTAMP_START'])).dt.total_seconds()  # /np.timedelta64(1000, 'ms')

max_val = flows['DURATION'].max()

long_flows = flows[flows['DURATION'] > int(max_val)]

googleFlows = flows[flows['CLASS']].str.contains('Google')

google_total_bytes = googleFlows['BYTES'].sum()

google_ip = '192.0.0.0'

toGoogleFlows = googleFlows[googleFlows['SRC_IP'].str.contains(google_ip)


totalTime = pd.to_datetime(flows['TIMESTAMP_END'].max()) - pd.to_datetime(flows['TIMESTAMP_START'].min()).dt.total_seconds()
print(flows.head)

flow_mode = flows['DST_IP'].mode()

most_flow = flows[~flows['SRC_IP']].str.contains(flow_mode)]['SRC_IP'].mode()


flows["TROUGHPUT"] = (flows['BYTES'] * 8 ) / flows['DURATION'] # bit/sec



# normalize data
flows['DURATION_NORM'] = ( flows['DURATION']  - flows['DURATION'].max() ) / (flows['DURATION'].max() - flows['DURATION'].min())
flows['THROUGHPUT_NORM'] = ( flows['TROUGHPUT']  - flows['TROUGHPUT'].max() ) / (flows['TROUGHPUT'].max() - flows['TROUGHPUT'].min())


