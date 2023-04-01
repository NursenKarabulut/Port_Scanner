import argparse
import socket
import threading

def connection_scan(target_ip, target_port):
    #If succesful, the port is open.If not , the port is closed.

     try:
         conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         conn_socket.connect((target_ip, target_port))
         conn_socket.send(b'Banner_qwery\r\n')
         print("[+] {}/tcp open".format(target_port))
     except OSError:
         print("[-] {}/tcp closed".format(target_port))
     finally:
         conn_socket.close() #Ensure the connection is closed.



def port_scan(target, port_num):
    # Scan indicated ports for status.
    # First , it attempts to resolve the ip address of a provided hostname , then enumerates through the ports.
     try:
         target_ip = socket.gethostbyname(target)
         print("[*] Scan Results for: {}".format(target_ip))
         connection_scan(target_ip,int(port_num))
     except OSError:
         print("[^] Cannot resolve {}: Unkown host".format(target))
         return # Exit scan if target ip is not resolved


def argument_parser():
      #Allow user to specify target host and port.
      parser = argparse.ArgumentParser(description="TCP port scanner.Accepts a hostname/IP address and list of ports to scan.Attempts to identify the service running on a port.")

      parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
      parser.add_argument("-p", "--ports", nargs="?", help="Comma-seperated port list, such as '25,80,8080'")

      var_args = vars(parser.parse_args()) #Convert arguments namespace to dictionary.

      return var_args

if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",")
        for port in port_list:
            port_scan(host, port)
    except AttributeError:
        print("Error.Please provide the command-line arguments before running.")







