from email import message
import threading
import socket

host ='127.0.0.1'
port =59000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients =[]
aliases =[]

#Broadcasting the message
def broadcast(message):
    for client in clients:
        client.send(message)

#Display Client details
def displayAllClients(client):
    
    message =""
    for alias in aliases:
        message = message +" , "+ str(alias.decode('utf-8'))
    print(message)
    client.send(message.encode('utf-8'))



#Display Client details
def sendHelpManual(client,message):
    client.send(message.encode('utf-8'))

#Direct Message.
def directmessage(client, message,name):
    message = message.strip()
    sent =False
    for alias in aliases:
        x = str(alias.decode('utf-8'))
        print('Value of x is' ,x)
        if message.startswith(x):
            sent = True
            m = message.split(x)
            index = aliases.index(alias)
            c = clients[index]
            c.send((name+":"+m[1]).encode('utf-8'))
            break
    if(sent == False):
        print(type(message))
        client.send(message.encode('utf-8'))


#Function to Handle Client's Connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            message= str(message.decode('utf-8'))
            switch = message.replace('"','').split(":")
            print(switch[1].strip())
            if switch[1].strip()== "/quit":
                index = clients.index(client)
                alias = aliases[index]
                clients.remove(client)
                aliases.remove(alias)
                broadcast(f'{alias} quit the chat room '.encode('utf-8'))
                break
            elif switch[1].strip() == "/help":
                helpMessage ="help      Manual \n"+"quit     Quitting system \n"+"users     list all clients \n"+"/bc     broadcasting message to all users \n"+"/dm     sending the direact message to neccessary clients \n"
                sendHelpManual(client,helpMessage)
            elif switch[1].strip() =="/users":
                displayAllClients(client)
            elif switch[1].strip().startswith("/bc"):
                mess =switch[1].split("/bc")
                broadcast(str(switch[0]+" : "+ mess[1]).encode('utf-8'))
            elif switch[1].strip().startswith("/dm"):
                mess =switch[1].split('/dm')
                sendToName = aliases[clients.index(client)]
                sendToName = str(sendToName.decode('utf-8'))
                directmessage(client, mess[1] ,sendToName)
            
        except:
          index = clients.index(client)
          clients.remove(client)
          client.close()
          alias = aliases[index]
          broadcast(f'{alias} has left the chat room! and lost the connection '.encode('utf-8'))
          aliases.remove(alias)
          break

#Main Function to receive a client connection.
def receive():
    while True:
        print('Server is running and listening ....')
        client ,address = server.accept()
        print(f'Connection is established with {str(address)}')
        client.send('alias ?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now Connected!'.encode('utf-8'))

        thread = threading.Thread(target= handle_client ,args=(client ,))
        thread.start()


if __name__ == "__main__":
    receive()