from time import sleep
import os
import requests
import config
import json


def sendRequest(endpoint, method):
    if method == 'GET':
        try:
            jsonResponse = requests.get(
                config.apiEndpoint + endpoint,
                headers = {'X-Token': config.apiToken}
            )
            return jsonResponse.json()
        except:
            print("[*] Request or Token Error")
            print("[*] Status: " + jsonResponse.status_code)
            exit()

def menu():
    print(r"""
______________________________________________________________________________________
                                 .-.
                                (o o) boo BLYAT!
                                | O \
                                \   \
                                `~~~'

                                [[MENU]]
                            [1] Available Servers
                            [2] Balance
                            [3] Backups
                            [4] Create Server
                            [5] Delete Server 
                            [6] SSH to Server
                            [7] Exit
_____________________________________________________________________________________
    """)

def parseServersInfo(request):
    result = []
    for server in request:
        result.append({
            'srvid': server['ctid'],
            'srvname': server['name'],
            'srvstatus': server['status'],
            'srvip': server['public_address']['address']
        })
    if not result:
        print("[*] No servers found.")
        exit()
    return result

if __name__ == '__main__':
    menu()
    switch = input("[*] >> ")
    if switch == '1':
        availableServers = parseServersInfo(sendRequest('scalets','GET'))
        for server in availableServers:
            print("[*] ServerID: " + str(server['srvid']) + '\n' +
                  "[*] ServerName: " + str(server['srvname']) + '\n' +
                  "[*] ServerStatus: " + str(server['srvstatus']) + '\n' +
                  "[*] ServerIP: " + str(server['srvip'])
            )
            print(r"""
_____________________________________________________________________________________
            """)
    elif switch == '2':
        balance = str(sendRequest('billing/balance','GET')['balance'])
        print("[*] Current Balance: " + balance)
    else:
        print("[*] Error.")
    


    

