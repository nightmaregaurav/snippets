/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    String serverAddress;
    int serverPort;
    public Client (String serverAddress, int serverPort){
        // Hostname the server is using
        this.serverAddress = serverAddress;
        // Port the server is using
        this.serverPort = serverPort;
    }
    
    public Remote getStub(String skeletonPath) throws NotBoundException, MalformedURLException, RemoteException{
        // Creation of Remote object using object fetched from RMI Registry
        return Naming.lookup("rmi://" + this.serverAddress + ":" + this.serverPort + skeletonPath);
    }
    public static void main(String[] args) {
        try {
            String serverAddress = "localhost";
            int serverPort = 5000;
            // Creating client object
            Client client = new Client(serverAddress, serverPort);
            
            // Getting stub object from remote skeleton
            AdderSkeleton stub1 = (AdderSkeleton) client.getStub("/adder");
            // Action
            System.out.println(stub1.add(1,2));
            
            // Getting stub object from remote skeleton
            SubtractorSkeleton stub2 = (SubtractorSkeleton) client.getStub("/subtractor");
            // Action
            System.out.println(stub2.sub(1,2));
        } catch (NotBoundException | MalformedURLException | RemoteException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
