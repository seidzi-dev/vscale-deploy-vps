import requests
import config
import json
import argparse


def getDataFromAPI(endpoint, headersDict):
    try:
        jsonResponse = requests.get(
            config.apiEndpoint + endpoint,
            headers = headersDict
        ).json()
        return jsonResponse
    except:
        print("[*] Request or Token Error")
        exit()

def banner(accountName,accountBalance):
    print(r"""
                                 .-.
                                (o o) boo BLYAT!
                                | O \
                                \   \
                                `~~~'
                            [[Account name: %s]]
                               [[Balance: %s]]
    
    """ % (accountName, accountBalance))

def parseServersInfo(serversJson):
    result = []
    for server in serversJson:
        result.append({
            'srvid': server['ctid'],
            'srvname': server['name'],
            'srvstatus': server['status'],
            'srvip': server['public_address']['address']
        })
    if not result:
        print("[*] No servers found.")
        exit()
    else:
        return result


if __name__ == '__main__':
    #Get accountName and accountBalance from API
    accountNameJson = getDataFromAPI('account', {'X-Token': config.apiToken})
    accountBalanceJson = getDataFromAPI('billing/balance', {'X-Token': config.apiToken})
    banner(accountNameJson['info']['name'], accountBalanceJson['balance'])
    print(parseServersInfo(getDataFromAPI('scalets',{'X-Token': config.apiToken})))


    

