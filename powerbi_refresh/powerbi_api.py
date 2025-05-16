import requests

def refresh_dataset(group_id, dataset_id, access_token):
    """
    Triggers a Power BI dataset refresh via REST API.
    """
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/refreshes"
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.post(url, headers=headers)
    if resp.status_code == 202:
        print("Power BI dataset refresh triggered.")
    else:
        print("Refresh failed:", resp.text)
