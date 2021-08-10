import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "wQU9d01May9VDgNFpTyq0nZBtDPedxfoHPMV60qvqDft"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspartate_Aminotransferase","Total_Protiens","Albumin","Albumin_and_Globulin_Ratio"]], "values": [[65,0,0.7,0.1,187,16,18,6.8,3.3,0.9]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/c2086673-696f-447b-85a5-dc8139633290/predictions?version=2021-08-06', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]
print(pred)

if(pred == 1):
    print("Patient is suffering from Liver disease")
else:
    print("Patient is not suffering from Liver disease")